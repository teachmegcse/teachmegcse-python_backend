from PIL import Image
import json
from fpdf import FPDF
from zipfile import ZipFile
import os

maxHeight = 2260
basePath = r"D:\python_projects\teachmegcse"
questionsJson=f"{basePath}/json_files/physics_db_classified_test.json"
outputdirectory=f"{basePath}/python_files/classified/pdfs"

def create_zip_archive(files, output_dir, zip_filename):
    zip_path = os.path.join(output_dir, zip_filename)
    with ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    return zip_path

Answers = []
classifiedPdf = FPDF("portrait","pt",[1600, maxHeight])
answerPdf = FPDF("portrait","pt",[1600, maxHeight])
questionNumX = 80 # is for the X coordinate for the question number
questionImageX = 160 # is for the X coordinate for the Image
currentYClassified = 100
currentYAnswers = 100
currentQuestionNum = 1
questionData = json.load(open(questionsJson,'r'))

level = questionData[0]["Level"]
subject = questionData[0]["Subject"]
imagelocation=f"{basePath}/images/unsorted/{subject}/p1/"
numOfChapters = len([x for x in questionData if x['Subject'] == str(subject)])

classifiedPdf.add_page()
classifiedPdf.set_font("helvetica",size=45,style="B")
classifiedPdf.set_xy(800, 2180)
classifiedPdf.cell(0, 10, str(classifiedPdf.page_no()), 'C')
for currentChapterNum in range(1, numOfChapters + 1):
    numOfQuestionsInChapter = len([x for x in questionData if x['Chapter'] == str(currentChapterNum)])
    questionDataInChapter = [x for x in questionData if x['Chapter'] == str(currentChapterNum)]

    for questionNum in range(numOfQuestionsInChapter):
        currentQuestionObject = questionDataInChapter[questionNum]
        currentImage = Image.open(f"{imagelocation}/{currentQuestionObject['questionName']}")
        currentImageCropped = currentImage.crop((0, 0, currentImage.width, currentImage.height - 10))

        if currentImage.height + currentYClassified + 100 > maxHeight:
            classifiedPdf.add_page()
            currentYClassified = 100
            classifiedPdf.set_xy(800, 2180)
            classifiedPdf.cell(0, 10, str(classifiedPdf.page_no()), 'C')

        classifiedPdf.set_xy(questionNumX, currentYClassified)
        classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
        classifiedPdf.set_xy(questionImageX, currentYClassified)
        classifiedPdf.image(currentImageCropped, questionImageX, currentYClassified, 1420, currentImageCropped.height)
        Answers.append({"questionNum" : currentQuestionNum, "Answer": currentQuestionObject['Answer'], "Source" : currentQuestionObject['pdfName']})
        currentYClassified += currentImage.height + 100
        currentQuestionNum += 1

answerPdf.add_page()
answerPdf.set_font("helvetica",size=45,style="B")
for answer in range(len(Answers)):
    currentAnswerObject = Answers[answer]
    if currentYAnswers + 100 > maxHeight:
        answerPdf.add_page()

    answerPdf.set_xy(questionNumX, currentYAnswers)
    answerPdf.cell(w=10, txt=f"{currentAnswerObject['questionNum']})  Answer: {currentAnswerObject['Answer']},  Source: {currentAnswerObject['Source']}")
    currentYAnswers += 70
answerPdf.output(f"{outputdirectory}/{subject}_{level}_answers.pdf")
classifiedPdf.output(f"{outputdirectory}/{subject}_{level}_classified.pdf")

files = [f"{outputdirectory}/{subject}_{level}_answers.pdf", f"{outputdirectory}/{subject}_{level}_classified.pdf"]
zip_path = create_zip_archive(files, outputdirectory, "multiple_files.zip")
