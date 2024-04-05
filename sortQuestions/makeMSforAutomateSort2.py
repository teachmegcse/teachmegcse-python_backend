import cv2 
import pytesseract
import os
import MS2
import json
import re
from tkinter import *
from tkinter import filedialog
from joblib import load
import getFormattedTextfromPdf
import shutil

root = Tk()
filetypes = [("PDF Files", "*.pdf")]

allLabels = ['Motion, forces and energy', 'Thermal physics', 
             'Waves', 'Electricity and magnetism', 'Nuclear physics', 'Space physics']

def predict (data, model):
    pipeline = load(f"D:/python_projects/teachmegcse/python_files/sci-kit/{model}.joblib")
    data = getFormattedTextfromPdf.formatText(data)
    test_data = [data]
    predicted_labels = pipeline.predict(test_data)
    return predicted_labels

numOfQuestionsInPaper = 40
code = '0625'
subject = 'IG_phy' # actual name for images filename
subject2 = 'physics'
numOfQuestions = 1547
paperNumber = 'p2'
model = 'IGphy'
level = "IGCSE"
startChapter = 1 #Default is 1 when AS but not 1 when A2
paperNumber2 = 2
level2 = 'IGCSE' # used only for paths


qnumber= 0
questionNumber = 0
pytesseract.pytesseract.tesseract_cmd = r"D:\python_projects\Tesseract-OCR\tesseract.exe"
jsonPath = r"D:\python_projects\teachmegcse\json_files"
custom_config = r'--oem 3 --psm 6'
index = 0
path = f"D:/python_projects/teachmegcse/images/unsorted/{level2}/{subject2}/{paperNumber}"

files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
for i in range(len(pdf_files)):
    pdf_files[i] = pdf_files[i][-13:]
    string = pdf_files[i]
    string = string.replace('q', 'm')
    string = string.replace('p', 's', 1)
    string = string.replace('.pdf', '')
    pdf_files[i] = string


f = open(f'{jsonPath}\{subject}_{paperNumber}_db.json', 'w')
f.write("[")


while (qnumber) < (numOfQuestions + 1):
    pdfName = pdf_files[index]
    answers = MS2.getAnswers(code, pdfName)
    

    if os.path.isfile(f'{path}\{subject}_{paperNumber}_{qnumber}.jpg')==True:
        if (type(questionNumber) == int):
            if (questionNumber % numOfQuestionsInPaper) == 0 and (qnumber > 20) and (questionNumber != 0):
                index += 1
                pdfName = pdf_files[index]
                answers = MS2.getAnswers(code, pdfName)
        QuestionName=f'{subject}_{paperNumber}_{qnumber}.jpg'
        path2 = f"{path}\{QuestionName}"   
        img = cv2.imread(path2)
        questionText = pytesseract.image_to_string(img, config=custom_config)
        questionNumber = questionText[:2]
        questionNumber = re.sub(r'[^\w\s]', '', questionNumber)
        try:
            questionNumber = int(questionNumber)
        except:
            questionNumber = ''
        
        questionText = questionText.lower()
        questionText = questionText.strip()
        try:
            questionAnswer = answers[int(questionNumber) - 1]
        except:
            questionAnswer = ''
        pdfName1 = f"{code}_{pdfName[:3]}_qp{pdfName[6:]}"
        chapter = predict(questionText, model)
        for k in range(len(allLabels)):
                if allLabels[k] == chapter:
                    chapterNum = startChapter + k
                    chapterPath = os.path.join(f"D:/python_projects/teachmegcse/images/sorted/{level2}/{subject2}/{paperNumber}", str(chapterNum))

                    if not os.path.exists(chapterPath):
                        os.makedirs(chapterPath)
                    shutil.copy2(f'{path}/{QuestionName}', os.path.join(chapterPath, QuestionName))

        if (questionAnswer != '') and (questionNumber != ''):
            answerObject = {
            "questionName" : f"{QuestionName}",
            "Answer": f"{questionAnswer}",
            "pdfName":f"{pdfName1}",
            "questionText":f"{questionText}",
            "Chapter" : f"{chapterNum}",
            "Level" : level,
            "paperNumber": paperNumber2,
            "Subject" : subject2
            }
            answerObjectFormatted = json.dumps(answerObject)
            f.write(answerObjectFormatted)
            f.write(""",
""")
            
    qnumber+=1

f.write("]")
f.close()
