import os
import cv2 
import pytesseract
import re
import predictData
from PyPDF2 import PdfReader
import shutil

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
custom_config = r'--oem 3 --psm 6'

allLabels = ['Utility', 'Indifference curves and budget lines', 
             'Efficiency and market failure', 'Private costs and benefits, externalities and social costs and benefits ',
               'Types of cost, revenue and profit, short-run and long-run production',
               'market structures', 'Growth and survival of firms',
               'objectives and policies of firms', 'Government policies to achieve efficient resource allocation',
                'Equity and redistribution of income and wealth', 'Labour market forces and government intervention', 'The circular flow of income',
               'Economic growth and sustainability', 'Employment/unemployment', 'Money and banking', 'Government macroeconomic policy objectives',
               'balance of payments', 'Economic development', 'levels of development']

model = 'a2eco'
type = 'jpg'

inputPath = r"C:\Users\donat\Documents\python_projects\temp\\"
outputPath = r"C:\Users\donat\Documents\python_projects\js_test\Classified\sorted\test\9708"  # output path should be like r".../9618/p3"


lst = os.listdir(inputPath) # your directory path
number_files = len(lst)

for i in range(number_files):
    if os.path.isfile(f"{inputPath}\\{lst[i]}") == True:
        print(f'{lst[i]}')
        questionName = lst[i]

        if type == 'jpg':
            img = cv2.imread(f'{inputPath}\{lst[i]}')
            questionText = pytesseract.image_to_string(img, config=custom_config)
            print(questionText)

        elif type == 'pdf':
            reader = PdfReader(f"{inputPath}\{questionName}")
            num_pages = len(reader.pages)
            questionText = ''
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                questionText += page.extract_text()

        questionText = re.sub(r'[^\w\s]', '', questionText)
        questionText = questionText.lower()
        chapter = predictData.predict(questionText, model)
        print(predictData.printLabel(questionText, model))

        for k in range(len(allLabels)):
            if allLabels[k] == chapter:
                chapterNum = k + 1
                chapter = str(chapter)
                chapter = chapter.strip(""" [''] """)
                chapterName = f"{chapterNum} {chapter}"
                chapterPath = os.path.join(outputPath,chapterName)

                if not os.path.exists(chapterPath):
                    os.makedirs(chapterPath)
                shutil.copy2(f'{inputPath}{questionName}', os.path.join(chapterPath, questionName))
