from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image
from fpdf import FPDF
import tempfile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from zipfile import ZipFile
import os
import uvicorn
from pathConst import basePath

class Question(BaseModel):
    Level: str
    Answer: str
    Chapter: str
    Subject: str
    pdfName: str
    paperNumber: int
    questionName: str
    questionText: str

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

def create_zip_archive(files, output_dir, zip_filename): # as fastapi does not allow FileResponse with multiple files so we're combining them into 1
    zip_path = os.path.join(output_dir, zip_filename)
    with ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    return zip_path

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate-pdf/")
async def generate_pdf(questionData: QuestionsList):
    Answers = [] # contains the Question object which has the answer, source and questionNum
    questionData = questionData.questionData
    maxHeight = 2260
    outputdirectory=f"{basePath}/python_files/classified/pdfs"

    classifiedPdf = FPDF("portrait","pt",[1600, maxHeight])
    answerPdf = FPDF("portrait","pt",[1600, maxHeight])
    questionNumX = 80  # is for the X coordinate for the question number
    questionImageX = 160  # is for the X coordinate for the Image
    currentYClassified = 100
    currentYAnswers = 100
    currentQuestionNum = 1

    subject = questionData[0].Subject
    level = questionData[0].Level
    paperNumber = questionData[0].paperNumber
    if level == "A2" or level == "AS":
        level2 = "A-level"
    else :
        level2 = "IGCSE"
    imagelocation=f"{basePath}/images/unsorted/{level2}/{subject}/p{paperNumber}/"

    classifiedPdf.add_page()
    classifiedPdf.set_font("helvetica",size=45,style="B")

    for questionNum in range(len(questionData)): # iterates over all the chapters that are in the json in ascending order
        currentQuestionObject = questionData[questionNum]
        currentImage = Image.open(f"{imagelocation}/{currentQuestionObject.questionName}")
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
        Answers.append({"questionNum" : currentQuestionNum, "Answer": currentQuestionObject.Answer, "Source" : currentQuestionObject.pdfName})
        currentYClassified += currentImageCropped.height + 100
        currentQuestionNum += 1

    answerPdf.add_page() # starts on the answer pdf which is a seperate pdf file
    answerPdf.set_font("helvetica",size=45,style="B")
    for answer in range(len(Answers)):
        currentAnswerObject = Answers[answer]
        if currentYAnswers + 100 > maxHeight:
            answerPdf.add_page()

        answerPdf.set_xy(questionNumX, currentYAnswers)
        answerPdf.cell(w=10, txt=f"{currentAnswerObject['questionNum']})  Answer: {currentAnswerObject['Answer']},  Source: {currentAnswerObject['Source']}")
        currentYAnswers += 70

    answerPdf.output(f"{outputdirectory}/answers.pdf")
    classifiedPdf.output(f"{outputdirectory}/questions.pdf")

    files = [f"{outputdirectory}/answers.pdf", f"{outputdirectory}/questions.pdf"]
    zip_path = create_zip_archive(files, outputdirectory, "multiple_files.zip")

    # Return the PDF for download
    return FileResponse(f"{outputdirectory}/multiple_files.zip")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=600)