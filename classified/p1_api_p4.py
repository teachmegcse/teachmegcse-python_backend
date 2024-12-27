import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
from fpdf import FPDF
import tempfile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from zipfile import ZipFile
import uvicorn
import os
from typing import Optional
import numpy as np

# Set up logger
logger = logging.getLogger("uvicorn")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class Question(BaseModel):
    Level: str
    Answer: Optional[str] = None  # Optional for long answers
    MSName: Optional[str] = None  # Optional for MCQ
    Chapter: str
    Subject: str
    pdfName: str
    paperNumber: int
    questionName: str
    questionText: str
    questionNumber: Optional[int] = None  # Optional field
    year: Optional[str] = None  # Optional field


class QuestionsList(BaseModel):
    questionData: List[Question]

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
def is_all_white(image):
    """
    Checks if an image is all white.

    Args:
        image: A PIL Image object.

    Returns:
        True if the image is all white, False otherwise.
    """
    image_array = np.array(image)  # Convert image to a numpy array
    return np.all(image_array == (255, 255, 255))  # Check if all pixels are white (RGB value)

def create_zip_archive(files, output_dir, zip_filename):  # as fastapi does not allow FileResponse with multiple files so we're combining them into 1
    zip_path = os.path.join(output_dir, zip_filename)
    with ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    logger.info(f"Created zip archive: {zip_path}")
    return zip_path

def process_image(currentImagePath, classifiedPdf, questionNumX, currentYClassified, questionImageX, currentQuestionNum, max_height_per_page, temp_files):
    currentImage = Image.open(currentImagePath)
    crop_height = 2050

    for y_start in range(0, currentImage.height, crop_height):
        y_end = min(y_start + crop_height, currentImage.height)

        cropped_image = currentImage.crop((0, y_start, currentImage.width, y_end))

        # Save cropped image to temp file
        temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp_files.append(temp_image_path.name)
        cropped_image.save(temp_image_path.name, format="JPEG")

        # Add cropped part to PDF
        classifiedPdf.add_page()
        classifiedPdf.set_xy(questionNumX, currentYClassified)
        classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
        classifiedPdf.image(temp_image_path.name, questionImageX, currentYClassified, 1420, cropped_image.height)
        temp_image_path.close()

    currentQuestionNum += 1
    return currentQuestionNum

@app.get("/")
async def root():
    logger.info("Received request at root endpoint")
    return {"message": "Hello World"}

@app.post("/generate-pdf/")
async def generate_pdf(questionData: QuestionsList):
    logger.info(f"Received request to generate PDF for {len(questionData.questionData)} questions")
    questionData = questionData.questionData
    maxHeight = 2260
    basePath = r"D:\python_projects\teachmegcse"
    outputdirectory = f"{basePath}/python_files/classified/pdfs"

    classifiedPdf = FPDF("portrait", "pt", [1600, maxHeight])
    answerPdf = FPDF("portrait", "pt", [1600, maxHeight])
    questionNumX = 80  # X coordinate for the question number
    questionImageX = 160  # X coordinate for the question image
    currentYClassified = 100
    currentYAnswers = 100
    currentQuestionNum = 1

    subject = questionData[0].Subject
    level = questionData[0].Level
    level2 = "A-level" if level in ["A2", "AS"] else "IGCSE"
    imagelocation = f"{basePath}/images/unsorted/{level2}/{subject}"

    classifiedPdf.set_font("helvetica", size=45, style="B")

    mcqdData = []
    longdData = []
    Answers = []

    temp_files = []  # Track temporary files for cleanup

    try:
        for currentQuestionObject in questionData:
            if currentQuestionObject.MSName is None:
                mcqdData.append(currentQuestionObject)
            else:
                longdData.append(currentQuestionObject)

        logger.info(f"Processing {len(mcqdData)} mcq questions")
        if len(mcqdData) > 0:
            classifiedPdf.add_page()
        for questionNum in range(len(mcqdData)):
            currentQuestionObject = mcqdData[questionNum]
            currentImage = Image.open(f"{imagelocation}/p{currentQuestionObject.paperNumber}/{currentQuestionObject.questionName}")
            currentImageCropped = currentImage.crop((0, 0, currentImage.width, currentImage.height - 10))

            if currentImage.height + currentYClassified + 100 > maxHeight:
                classifiedPdf.add_page()
                currentYClassified = 100
                classifiedPdf.set_xy(800, -2200)
                classifiedPdf.cell(0, 10, str(classifiedPdf.page_no()), 'C') # adds page numbers to the bottom of the page

            classifiedPdf.set_xy(questionNumX, currentYClassified)
            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
            classifiedPdf.set_xy(questionImageX, currentYClassified)
            temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            currentImageCropped.save(temp_image_path.name, format="JPEG")

            # Add the image to the PDF from the temporary file
            classifiedPdf.image(temp_image_path.name, questionImageX, currentYClassified, 1420, currentImageCropped.height)
            temp_image_path.close()
            Answers.append({"questionNum" : currentQuestionNum, "Answer": currentQuestionObject.Answer, "Source" : currentQuestionObject.pdfName, "type": "MCQ"})
            currentYClassified += currentImageCropped.height + 100
            currentQuestionNum += 1

        logger.info(f"Processing {len(longdData)} long-answer questions")
        currentYClassified = 100
        for questionNum in range(len(longdData)):

            currentQuestionObject = longdData[questionNum]
            Answers.append({"questionNum" : currentQuestionNum, "Answer": currentQuestionObject.MSName, "Source" : currentQuestionObject.pdfName, "type": "Long"})
            currentImagePath = f"{imagelocation}/long/{currentQuestionObject.questionName}"

            if not os.path.exists(currentImagePath):
                logger.error(f"Image not found: {currentImagePath}")
                raise HTTPException(status_code=404, detail=f"Image not found: {currentImagePath}")

            currentImage = Image.open(currentImagePath)
            modifier = 2000 # height of each page
            if currentImage.height > modifier:
                currentIndex = 0
                while True:
                    if (currentIndex + 1) * modifier > currentImage.height:
                        currentCroppedImage = currentImage.crop((0, currentIndex * modifier, currentImage.width, currentImage.height))

                        # Check if the cropped image is all white
                        if not is_all_white(currentCroppedImage):
                            classifiedPdf.add_page()
                            classifiedPdf.set_xy(questionNumX, currentYClassified)
                            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
                            temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
                            temp_files.append(temp_image_path.name)
                            currentCroppedImage.save(temp_image_path.name, format="JPEG")
                            classifiedPdf.image(temp_image_path.name, questionImageX, currentYClassified, 1420, currentCroppedImage.height)
                            temp_image_path.close()
                        break
                    else:
                        currentCroppedImage = currentImage.crop((0, currentIndex * modifier, currentImage.width, (currentIndex + 1) * modifier))

                        # Check if the cropped image is all white
                        if not is_all_white(currentCroppedImage):
                            classifiedPdf.add_page()
                            classifiedPdf.set_xy(questionNumX, currentYClassified)
                            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
                            temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
                            temp_files.append(temp_image_path.name)
                            currentCroppedImage.save(temp_image_path.name, format="JPEG")
                            classifiedPdf.image(temp_image_path.name, questionImageX, currentYClassified, 1420, currentCroppedImage.height)
                            temp_image_path.close()
                        currentIndex += 1
            else:
                classifiedPdf.add_page()
                classifiedPdf.set_xy(questionNumX, currentYClassified)
                classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
                classifiedPdf.image(currentImagePath, questionImageX, currentYClassified, 1420, currentImage.height)
            currentQuestionNum += 1

        logger.info("Generating answers PDF")
        mcqAnswers = []
        longAnswers = []
        for answer in Answers:
            if answer["type"] == "MCQ":
                mcqAnswers.append(answer)
            else:
                longAnswers.append(answer)
        if (len(mcqAnswers) > 0):
            answerPdf.add_page()
        answerPdf.set_font("helvetica", size=45, style="B")
        currentQuestionNum = 1
        for answer in range(len(mcqAnswers)):
            currentAnswerObject = mcqAnswers[answer]
            if currentYAnswers + 100 > maxHeight:
                answerPdf.add_page()

            answerPdf.set_xy(questionNumX, currentYAnswers)
            answerPdf.cell(w=10, txt=f"{currentQuestionNum})  Answer: {currentAnswerObject['Answer']},  Source: {currentAnswerObject['Source']}")
            currentYAnswers += 70
            currentQuestionNum += 1
        
        currentYAnswers = 100
        for index, currentAnswerObject in enumerate(longAnswers):
            currentAnswerPath = f"{imagelocation}/long/{currentAnswerObject['Answer']}"

            if not os.path.exists(currentAnswerPath):
                logger.error(f"Answer image not found: {currentAnswerPath}")
                continue  # Skip to the next answer if the image is not found

            try:
                currentAnswerImage = Image.open(currentAnswerPath)

                # Rotate the image 90 degrees counter-clockwise (bottom-to-top text)
                rotated_image = currentAnswerImage.rotate(90, expand=True)

                # Save the rotated image to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image_path:
                    rotated_image.save(temp_image_path.name, format="JPEG")

                # Add the rotated image and question number to the PDF
                answerPdf.add_page()
                answerPdf.set_xy(questionImageX, currentYAnswers - 30)
                answerPdf.cell(w=10, txt=f"{currentQuestionNum})")  # Print answer number, adjust w to align with question number

                answerPdf.image(temp_image_path.name, questionImageX, currentYAnswers + 10, 1420, rotated_image.height)
                currentQuestionNum += 1
            except Exception as e:
                logger.error(f"Error processing answer image {currentAnswerPath}: {e}")
            finally:
                try:
                    os.remove(temp_image_path.name)
                except FileNotFoundError:
                    pass # File may have been deleted already
                except Exception as e:
                    logger.error(f"Error deleting temporary file {temp_image_path.name}: {e}")

            
        

        classified_pdf_path = f"{outputdirectory}/questions.pdf"
        classifiedPdf.output(classified_pdf_path)
        answers_pdf_path = f"{outputdirectory}/answers.pdf"
        answerPdf.output(f"{outputdirectory}/answers.pdf")

        logger.info(f"PDF generated: {classified_pdf_path}")

        files = [classified_pdf_path, answers_pdf_path]
        zip_path = create_zip_archive(files, outputdirectory, "multiple_files.zip")

        return FileResponse(zip_path, filename="multiple_files.zip")
        
    except Exception as e:
        logger.error(f"Error generating PDF: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Cleanup temporary files
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
