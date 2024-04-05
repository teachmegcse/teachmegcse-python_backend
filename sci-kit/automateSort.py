import os
import re
import predictData
from PyPDF2 import PdfReader
import shutil
import json

allLabels = ['Physical quantities and units', 'Kinematics', 
             'Dynamics', 'Forces, density and pressure', 'Work, energy and power', 'Deformation of solids', 'Waves',
               'Superposition', 'Electricity', 'D.C. circuits', 'Particle physics']

numOfQuestions = 1578
model = 'asphy'
type = 'jpg'
startChapter = 1 #Default is 1 when AS but not 1 when A2
subject = 'phy'
paperNumber = 'p1'

inputPath = r"D:\python_projects\teachmegcse\images\unsorted\physics\p1\\"
outputPath = r"D:\python_projects\teachmegcse\images\sorted\physics\p1"  # output path should be like r".../9618/p3"

db = open(f"D:/python_projects/teachmegcse/json_files/{subject}_{paperNumber}_mcq_answers.json")
db_filtered = json.load(db)


lst = os.listdir(inputPath) # your directory path
number_files = len(lst)

for i in range(1, numOfQuestions):
    if os.path.isfile(f"{inputPath}\\{lst[i]}"):
        questionName = lst[i]
        questionObject = [x for x in db_filtered if x['questionName'] == questionName]
        if len(questionObject) > 0:

            if type == 'jpg':
                print(lst[i])
                questionText = questionObject[0]['questionText']
                print(questionText)

            elif type == 'pdf':
                reader = PdfReader(f"{inputPath}\{questionName}")
                num_pages = len(reader.pages)
                questionText = ''
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    questionText += page.extract_text()

            chapter = predictData.predict(questionText, model)
            print(predictData.printLabel(questionText, model))

            for k in range(len(allLabels)):
                if allLabels[k] == chapter:
                    chapterNum = startChapter + k
                    chapterPath = os.path.join(outputPath, str(chapterNum))

                    if not os.path.exists(chapterPath):
                        os.makedirs(chapterPath)
                    shutil.copy2(f'{inputPath}{questionName}', os.path.join(chapterPath, questionName))