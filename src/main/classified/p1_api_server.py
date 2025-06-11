import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
from fpdf import FPDF
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

class QuestionsList(BaseModel):
    questionData: List[Question]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

def is_all_white(image):
    image_array = np.array(image)
    return np.all(image_array == (255, 255, 255))

def create_zip_archive(files, output_dir, zip_filename):
    zip_path = os.path.join(output_dir, zip_filename).replace("\\", "/")
    logger.info(f"Creating zip archive at {zip_path}")
    with ZipFile(zip_path, 'w') as zipf:
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
    logger.info(f"Received request to generate PDF for {len(questionData.questionData)} questions")
    questionData = questionData.questionData
    maxHeight = 2260
    basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
    outputdirectory = f"{basePath}/resources/pdfs/classified"

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
    imagelocation = f"{basePath}/resources/images/{level2}/{subject}"

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
        currentImage = Image.open(f"{imagelocation}/p{currentQuestionObject.paperNumber}/{currentQuestionObject.questionName}")
        currentImageCropped = currentImage.crop((0, 0, currentImage.width, currentImage.height - 10))

        if currentImage.height + currentYClassified + 100 > maxHeight:
            classifiedPdf.add_page()
            currentYClassified = 100

        classifiedPdf.set_xy(questionNumX, currentYClassified)
        classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")

        temp_image_path = f"{basePath}/resources/images/temp/temp_{currentQuestionNum}.jpg"
        currentImageCropped.save(temp_image_path, format="JPEG")
        classifiedPdf.image(temp_image_path, questionImageX, currentYClassified, 1420, currentImageCropped.height)
        os.remove(temp_image_path)

        Answers.append({"questionNum": currentQuestionNum, "Answer": currentQuestionObject.Answer, "Source": currentQuestionObject.pdfName, "type": "MCQ"})
        currentYClassified += currentImageCropped.height + 100
        currentQuestionNum += 1

    if longdData:
        currentYClassified = 100
        for currentQuestionObject in longdData:
            currentImagePath = f"{imagelocation}/long/{currentQuestionObject.questionName}"
            if not os.path.exists(currentImagePath):
                logger.error(f"Image not found: {currentImagePath}")
                raise HTTPException(status_code=404, detail=f"Image not found: {currentImagePath}")
            Answers.append({"questionNum": currentQuestionNum, "Answer": currentQuestionObject.MSName, "Source": currentQuestionObject.pdfName, "type": "Long"})
            currentImage = Image.open(currentImagePath)
            modifier = 2000
            if currentImage.height > modifier:
                currentIndex = 0
                while True:
                    if (currentIndex + 1) * modifier > currentImage.height:
                        croppedImage = currentImage.crop((0, currentIndex * modifier, currentImage.width, currentImage.height))
                        if not is_all_white(croppedImage):
                            classifiedPdf.add_page()
                            classifiedPdf.set_xy(questionNumX, currentYClassified)
                            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")

                            temp_image_path = f"{basePath}resources/images/temp/temp_{currentQuestionNum}_part.jpg"
                            croppedImage.save(temp_image_path, format="JPEG")
                            classifiedPdf.image(temp_image_path, questionImageX, currentYClassified, 1420, croppedImage.height)
                            os.remove(temp_image_path)
                        break
                    else:
                        croppedImage = currentImage.crop((0, currentIndex * modifier, currentImage.width, (currentIndex + 1) * modifier))
                        if not is_all_white(croppedImage):
                            classifiedPdf.add_page()
                            classifiedPdf.set_xy(questionNumX, currentYClassified)
                            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")

                            temp_image_path = f"{basePath}/resources/images/temp/temp_{currentQuestionNum}_part_{currentIndex}.jpg"
                            croppedImage.save(temp_image_path, format="JPEG")
                            classifiedPdf.image(temp_image_path, questionImageX, currentYClassified, 1420, croppedImage.height)
                            os.remove(temp_image_path)
                        currentIndex += 1
            else:
                classifiedPdf.add_page()
                classifiedPdf.set_xy(questionNumX, currentYClassified)
                classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")

                temp_image_path = f"{basePath}/resources/images/temp/temp_{currentQuestionNum}.jpg"
                currentImage.save(temp_image_path, format="JPEG")
                classifiedPdf.image(temp_image_path, questionImageX, currentYClassified, 1420, currentImage.height)
                os.remove(temp_image_path)

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
        answerPdf.cell(w=10, txt=f"{currentQuestionNum})  Answer: {answer['Answer'] or 'N/A'},  Source: {answer['Source'] or 'Unknown'}")
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
            temp_image_pSath = f"{imagelocation}/temp_rotated_image_{currentQuestionNum}.jpg"
            rotated_image.save(temp_image_path, format="JPEG")

            # Add the rotated image and question number to the PDF
            answerPdf.add_page()
            answerPdf.set_xy(questionImageX, currentYAnswers - 30)
            answerPdf.cell(w=10, txt=f"{currentQuestionNum})")  # Print answer number

            answerPdf.image(temp_image_path, questionImageX, currentYAnswers + 10, 1420, rotated_image.height)
            currentQuestionNum += 1

            # Remove the temporary file
            os.remove(temp_image_path)
        except Exception as e:
            logger.error(f"Error processing answer image {currentAnswerPath}: {e}")

    classifiedPdf.output(f"{outputdirectory}/questions.pdf")
    answerPdf.output(f"{outputdirectory}/answers.pdf")

    files = [f"{outputdirectory}/answers.pdf", f"{outputdirectory}/questions.pdf"]
    zip_path = create_zip_archive(files, outputdirectory, "multiple_files.zip")

    return FileResponse(zip_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=600)
