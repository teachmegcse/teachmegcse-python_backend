import numpy as np
from typing import Optional
import uvicorn
from zipfile import ZipFile
from typing import List
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from fpdf import FPDF
from PIL import Image
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException
import logging
import re
import sys
import os
import tempfile

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))

# Set up logger
logger = logging.getLogger("uvicorn")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class QuestionPart(BaseModel):
    # [x1, y1, x2, y2] of the part's label in pixels of the question image, as makep4-ai.py stores them
    coordinates: List[int]
    text: str


class Question(BaseModel):
    Level: str
    Answer: Optional[str] = None
    MSName: Optional[str] = None
    Chapter: str
    Subject: str
    pdfName: str
    paperNumber: int
    questionName: str
    questionText: str
    questionNumber: Optional[int] = None
    year: Optional[str] = None
    questionParts: List[QuestionPart] = Field(default_factory=list)
    # Indexes into questionParts of the parts to keep, the rest are cropped out. Leave out (or empty) for the
    # whole question. See generate_pdf_request.md
    selectedParts: Optional[List[int]] = None


class QuestionsList(BaseModel):
    questionData: List[Question]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def is_all_white(image):
    image_array = np.array(image)
    return np.all(image_array == (255, 255, 255))


ROMAN_NUMERALS = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
# Part labels whose tops are within this many pixels of each other are on the same line, e.g. "(a) (i)"
SAME_LINE_PX = 20
# Long question images taller than this are split over several pages
LONG_PAGE_HEIGHT = 2000


def part_depths(parts: List[QuestionPart]) -> list:
    """The level of each part: 1 for (a), (b), ..., 2 for (i), (ii), ..., None for labels that are neither
    (misread labels like "(8)"), which are not cut at and can't be selected."""
    depths = []
    previous_letter = None
    for part in parts:
        match = re.fullmatch(r"\(?([a-z]+)\)?", part.text.strip())
        name = match.group(1) if match else None
        # (i) after (h) is the letter i, not the numeral
        if name in ROMAN_NUMERALS and not (name == "i" and previous_letter == "h"):
            depths.append(2)
        elif name is not None and len(name) == 1:
            depths.append(1)
            previous_letter = name
        else:
            depths.append(None)
    return depths


def kept_parts(question: Question) -> set:
    """The indexes of the parts of question to keep, from question.selectedParts.

    A part nested in (a), like (a)(i), is only kept if (a) is selected too, so deselecting (a) removes all of it.
    Selecting (a) without any of its nested parts keeps all of (a); selecting (a) and some of its nested parts keeps
    only those, along with the text of (a) before (a)(i).
    """
    parts = question.questionParts
    if not parts:
        raise HTTPException(
            status_code=400, detail=f"selectedParts given for {question.questionName}, which has no questionParts"
        )
    unknown = [index for index in question.selectedParts if not 0 <= index < len(parts)]
    if unknown:
        raise HTTPException(
            status_code=400,
            detail=f"selectedParts {unknown} out of range for {question.questionName}, which has {len(parts)} parts",
        )
    depths = part_depths(parts)
    unlabelled = [index for index in question.selectedParts if depths[index] is None]
    if unlabelled:
        raise HTTPException(
            status_code=400,
            detail=f"selectedParts {unlabelled} of {question.questionName} aren't (a)/(i) style part labels",
        )

    # The (a), (b), ... each (i), (ii), ... is nested in, None for parts that aren't nested
    parents = []
    current_letter = None
    for index, depth in enumerate(depths):
        parents.append(current_letter if depth == 2 else None)
        if depth == 1:
            current_letter = index

    selected = set(question.selectedParts)
    kept = set()
    for index, depth in enumerate(depths):
        parent = parents[index]
        if depth is None:
            continue
        if parent is None:
            if index in selected:
                kept.add(index)
        elif parent in selected:
            any_nested_selected = any(parents[other] == parent for other in selected)
            if index in selected or not any_nested_selected:
                kept.add(index)
    return kept


def crop_to_selected_parts(image: Image.Image, question: Question) -> Image.Image:
    """Crops the parts of a long question that aren't kept (see kept_parts) out of its image and stitches the rest
    back together. A part runs from its label down to the next label, and the question's start (its number and any
    text before the first part) is always kept."""
    parts = question.questionParts
    depths = part_depths(parts)
    kept = kept_parts(question)

    # Group the labels into lines, each running from its top down to the next line's top
    lines = []
    for index in sorted((i for i, depth in enumerate(depths) if depth is not None), key=lambda i: parts[i].coordinates[1]):
        top = min(max(0, parts[index].coordinates[1]), image.height)
        if lines and top - lines[-1]["top"] <= SAME_LINE_PX:
            lines[-1]["parts"].append(index)
        else:
            lines.append({"top": top, "parts": [index]})

    # (top, bottom) of each kept stretch of the image, starting with the question's start. The text after a line like
    # "(a) (i)" belongs to its last label, (i), so the line is kept with that part
    ranges = [(0, lines[0]["top"])] if lines else [(0, image.height)]
    for line_index, line in enumerate(lines):
        bottom = lines[line_index + 1]["top"] if line_index + 1 < len(lines) else image.height
        if max(line["parts"], key=lambda i: parts[i].coordinates[0]) in kept:
            if ranges[-1][1] == line["top"]:
                ranges[-1] = (ranges[-1][0], bottom)
            else:
                ranges.append((line["top"], bottom))
    ranges = [(top, bottom) for top, bottom in ranges if bottom > top]

    stitched = Image.new("RGB", (image.width, sum(bottom - top for top, bottom in ranges)), (255, 255, 255))
    y = 0
    for top, bottom in ranges:
        stitched.paste(image.crop((0, top, image.width, bottom)), (0, y))
        y += bottom - top
    return stitched


def selected_part_labels(question: Question) -> str:
    """The kept parts as they're printed with the mark scheme, e.g. "(a), (b)(ii)", or "" for the whole question.
    A part with all its nested parts kept is printed on its own."""
    if not question.selectedParts:
        return ""
    parts = question.questionParts
    depths = part_depths(parts)
    kept = kept_parts(question)
    labels = []
    current_letter = None
    nested_all_kept = True
    for index, part in enumerate(parts):
        if depths[index] == 1:
            current_letter = index
            nested = []
            for other in range(index + 1, len(parts)):
                if depths[other] == 1:
                    break
                if depths[other] == 2:
                    nested.append(other)
            nested_all_kept = all(i in kept for i in nested)
            if index in kept and nested_all_kept:
                labels.append(part.text.strip())
        elif depths[index] == 2 and index in kept:
            if current_letter is None:
                labels.append(part.text.strip())
            elif not nested_all_kept:
                labels.append(f"{parts[current_letter].text.strip()}{part.text.strip()}")
    return ", ".join(labels)


def add_image_to_pdf(pdf: FPDF, image: Image.Image, x: int, y: int) -> None:
    temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    image.convert("RGB").save(temp_image_path.name, format="JPEG")
    temp_image_path.close()
    pdf.image(temp_image_path.name, x, y, 1420, image.height)
    os.remove(temp_image_path.name)


def add_long_question(pdf: FPDF, image: Image.Image, question_num: int, x_num: int, x_image: int, y: int) -> None:
    """Adds a long question on a new page, split over more pages (each starting with the question number) if it's
    taller than LONG_PAGE_HEIGHT. Blank pieces are left out."""
    for top in range(0, image.height, LONG_PAGE_HEIGHT):
        piece = image.crop((0, top, image.width, min(top + LONG_PAGE_HEIGHT, image.height)))
        if top > 0 and is_all_white(piece):
            continue
        pdf.add_page()
        pdf.set_xy(x_num, y)
        pdf.cell(w=10, txt=f"{question_num})")
        add_image_to_pdf(pdf, piece, x_image, y)


def create_zip_archive(files, output_dir, zip_filename):
    zip_path = os.path.join(output_dir, zip_filename).replace("\\", "/")
    logger.info(f"Creating zip archive at {zip_path}")
    with ZipFile(zip_path, "w") as zipf:
        for file in files:
            if os.path.exists(file):
                logger.info(f"Adding file {file} to zip")
                zipf.write(file, os.path.basename(file))
            else:
                logger.error(f"File not found: {file}")
    return zip_path


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/generate-pdf/")
async def generate_pdf(questionData: QuestionsList):
    logger.info(
        f"Received request to generate PDF for {
            len(questionData.questionData)
        } questions"
    )
    questionData = questionData.questionData
    maxHeight = 2260
    outputdirectory = f"{BASE_PATH}/resources/pdfs/classified"
    os.makedirs(outputdirectory, exist_ok=True)

    classifiedPdf = FPDF("portrait", "pt", [1600, maxHeight])
    answerPdf = FPDF("portrait", "pt", [1600, maxHeight])
    questionNumX = 80
    questionImageX = 160
    currentYClassified = 100
    currentYAnswers = 100
    currentQuestionNum = 1

    subject = questionData[0].Subject
    level = questionData[0].Level
    level2 = "A-level" if level in ["A2", "AS"] else "IGCSE"
    imagelocation = f"{BASE_PATH}/resources/images/{level2}/{subject}"

    classifiedPdf.set_font("helvetica", size=45, style="B")

    mcqdData = []
    longdData = []
    Answers = []

    for currentQuestionObject in questionData:
        if currentQuestionObject.MSName is None:
            mcqdData.append(currentQuestionObject)
        else:
            longdData.append(currentQuestionObject)

    if mcqdData:
        classifiedPdf.add_page()
    for currentQuestionObject in mcqdData:
        currentImage = Image.open(
            f"{imagelocation}/p{currentQuestionObject.paperNumber}/{currentQuestionObject.questionName}"
        )
        currentImageCropped = currentImage.crop(
            (0, 0, currentImage.width, currentImage.height - 10)
        )

        if currentImage.height + currentYClassified + 100 > maxHeight:
            classifiedPdf.add_page()
            currentYClassified = 100

        classifiedPdf.set_xy(questionNumX, currentYClassified)
        classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")

        # Save image to temporary file and add to PDF
        temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        currentImageCropped.save(temp_image_path.name, format="JPEG")
        temp_image_path.close()
        classifiedPdf.image(
            temp_image_path.name,
            questionImageX,
            currentYClassified,
            1420,
            currentImageCropped.height,
        )
        os.remove(temp_image_path.name)

        Answers.append(
            {
                "questionNum": currentQuestionNum,
                "Answer": currentQuestionObject.Answer,
                "Source": currentQuestionObject.pdfName,
                "type": "MCQ",
            }
        )
        currentYClassified += currentImageCropped.height + 100
        currentQuestionNum += 1

    for currentQuestionObject in longdData:
        currentImagePath = f"{imagelocation}/long/{currentQuestionObject.questionName}"
        if not os.path.exists(currentImagePath):
            logger.error(f"Image not found: {currentImagePath}")
            raise HTTPException(status_code=404, detail=f"Image not found: {currentImagePath}")
        with Image.open(currentImagePath) as currentImage:
            if currentQuestionObject.selectedParts:
                currentImage = crop_to_selected_parts(currentImage, currentQuestionObject)
            add_long_question(classifiedPdf, currentImage, currentQuestionNum, questionNumX, questionImageX, 100)

        Answers.append(
            {
                "questionNum": currentQuestionNum,
                "Answer": currentQuestionObject.MSName,
                "Source": currentQuestionObject.pdfName,
                "type": "Long",
                "parts": selected_part_labels(currentQuestionObject),
            }
        )
        currentQuestionNum += 1

    logger.info("Generating answers PDF")
    mcqAnswers = []
    longAnswers = []

    # Categorize answers into MCQ and Long
    for answer in Answers:
        if answer["type"] == "MCQ":
            mcqAnswers.append(answer)
        else:
            longAnswers.append(answer)

    # Add MCQ answers to the PDF
    if len(mcqAnswers) > 0:
        answerPdf.add_page()
    answerPdf.set_font("helvetica", size=45, style="B")
    currentQuestionNum = 1

    # Process MCQ answers
    for answer in mcqAnswers:
        if currentYAnswers + 100 > maxHeight:
            answerPdf.add_page()
            currentYAnswers = 100

        answerPdf.set_xy(questionNumX, currentYAnswers)
        answerPdf.cell(
            w=10,
            txt=f"{currentQuestionNum})  Answer: {answer['Answer'] or 'N/A'},  Source: {
                answer['Source'] or 'Unknown'
            }",
        )
        currentYAnswers += 70
        currentQuestionNum += 1

    # Reset Y position for Long answers
    currentYAnswers = 100

    # Process Long answers
    for currentAnswerObject in longAnswers:
        logger.info(f"Processing Long answer: {currentAnswerObject}")
        currentAnswerPath = f"{imagelocation}/long/{currentAnswerObject['Answer']}"

        if not os.path.exists(currentAnswerPath):
            logger.error(f"Answer image not found: {currentAnswerPath}")
            continue  # Skip to the next answer if the image is not found

        try:
            # Open and process the image
            currentAnswerImage = Image.open(currentAnswerPath)

            # Rotate the image 90 degrees counter-clockwise
            rotated_image = currentAnswerImage.rotate(90, expand=True)

            # Save the rotated image to a temporary file
            temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            rotated_image.save(temp_image_path.name, format="JPEG")
            temp_image_path.close()

            # Add the rotated image and question number to the PDF
            answerPdf.add_page()
            answerPdf.set_xy(questionImageX, currentYAnswers - 30)
            # Print answer number
            parts = f"  Parts: {currentAnswerObject['parts']}" if currentAnswerObject["parts"] else ""
            answerPdf.cell(w=10, txt=f"{currentQuestionNum}){parts}")

            # Scale it to fit the page (keeping its proportions) so the edges aren't cut off
            imageY = currentYAnswers + 10
            scale = min(1420 / rotated_image.width, (maxHeight - imageY - 60) / rotated_image.height)
            imageWidth = rotated_image.width * scale
            answerPdf.image(
                temp_image_path.name,
                questionImageX + (1420 - imageWidth) / 2,
                imageY,
                imageWidth,
                rotated_image.height * scale,
            )
            currentQuestionNum += 1

            # Remove the temporary file
            os.remove(temp_image_path.name)
        except Exception as e:
            logger.error(f"Error processing answer image {currentAnswerPath}: {e}")

    classifiedPdf.output(f"{outputdirectory}/questions.pdf")
    answerPdf.output(f"{outputdirectory}/answers.pdf")

    files = [f"{outputdirectory}/answers.pdf", f"{outputdirectory}/questions.pdf"]
    zip_path = create_zip_archive(files, outputdirectory, "multiple_files.zip")

    return FileResponse(zip_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=600)
