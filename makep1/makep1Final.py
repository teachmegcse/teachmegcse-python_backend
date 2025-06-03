import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
TESSERACT_CMD = TESSERACT_PATH
CUSTOM_CONFIG = r'--oem 3 --psm 6'
MODEL_PATH_TEMPLATE = f"{BASE_PATH}/python_files/sci-kit/{model}.joblib"

from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
from pathConst import BASE_PATH, POPPLER_PATH, TESSERACT_PATH
import requests
from joblib import load
from ..sortQuestions.getFormattedTextfromPdf import getFormattedTextfromPdf
from ..sortQuestions import MS2
import cv2
import pytesseract
import shutil
import json

ALL_LABELS = ['Utility', 'Indifference curves and budget lines', 
             'Efficiency and market failure', 'Private costs and benefits, externalities and social costs and benefits ',
               'Types of cost, revenue and profit, short-run and long-run production',
               'market structures', 'Growth and survival of firms',
               'objectives and policies of firms', 'Government policies to achieve efficient resource allocation',
                'Equity and redistribution of income and wealth', 'Labour market forces and government intervention', 'The circular flow of income',
               'Economic growth and sustainability', 'Employment/unemployment', 'Money and banking', 'Government macroeconomic policy objectives',
               'balance of payments', 'Economic development', 'levels of development']

subject = 'IG_bio'
paper_number = 'p1'
code = '0610'
start_chapter = 1
model = 'igbio'
level = "A2"
level2 = 'A-level' # A-level or IGCSE
subject2 = 'biology'


current_question_num = 1
root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 1 # Default is 1
startPixel = 150  # Default is 150
questionObjects = []

files = filedialog.askopenfilenames(filetypes=filetypes)
output1Path = f"{BASE_PATH}/python_files/makep1/testImages"


def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        if x >= startPage:
            if page.extract_text().find("BLANK PAGE") == -1:
                images[x].save(f"{output_path}/{i}/{x}.jpg", 'JPEG')

def get_y_coordinates(file_name, folderNum):
    with PIL.Image.open(f"{output1Path}/{folderNum}/{file_name}") as im:
        files = {'file': im}
        response = requests.post('http://127.0.0.1:8000/predict', files=files)
        y_coordinates = response.json()
        return y_coordinates


def strip_images(folder_num):
    pages = os.listdir(f"{output1Path}/{folder_num}")
    for i in range(len(pages)):
        with PIL.Image.open(f"{output1Path}/{folder_num}/{pages[i]}") as im:
            im_crop = im.crop((0, startPixel, 1654, 2200))
            im_crop.save(f"{output1Path}/{folder_num}/{pages[i]}")


def clean_images():
    questions = os.listdir(f"{output1Path}/questions")
    for i in range(len(questions)):
        im = PIL.Image.open(f"{output1Path}/questions/{questions[i]}")
        pix = im.load()
        flag = False
        if flag == False:
            for y in range(im.height - 2, 1, -2):
                for x in range(im.width - 2, 1, -2):
                    value = pix[x, y]
                    if value != (255, 255, 255):
                        value2 = pix[x+1,y]
                        if value2 != (255, 255, 255):
                            flag = True
                            break
                if flag:
                    break
        cleaned_image = im.crop((0, 0, 1500, y + 10))
        cleaned_image.save(f"{output1Path}/questions/{questions[i]}")


def take_screenshot(y1, y2, file_name, folderNum):
    global current_question_num
    if (y2 - y1) > 150 :
        with PIL.Image.open(f"{output1Path}/{folderNum}/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output1Path}/questions/{subject}_{paper_number}_{current_question_num}.jpg")
    else :
        current_question_num -= 1

def predict(data, model):
    pipeline = load(MODEL_PATH_TEMPLATE.format(model=model))
    data = getFormattedTextfromPdf.formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]

def process_image(image_path, custom_config):
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img, config=custom_config)


for m in range(len(files)):
    makeImages(output1Path, files[m], m)

    strip_images(m)
    pages = os.listdir(f"{output1Path}/{m}")
    sorted_files = sorted(pages, key=lambda x: int(x.split('.')[0]))

    answers = MS2.extract_answers_from_pdf(code, files[m])
    current_question_num = 1
    for k in range(len(pages)):
        y_coordinates = get_y_coordinates(sorted_files[k], m)
        if len(y_coordinates) > 1:
            for j in range(len(y_coordinates) - 1):
                take_screenshot(y_coordinates[j], y_coordinates[j + 1], sorted_files[k], m)
                question_text = process_image(f"{output1Path}/questions/{subject}_{paper_number}_{current_question_num}.jpg", CUSTOM_CONFIG).lower().strip()
                chapter = predict(question_text, model)
                chapter_num = start_chapter + ALL_LABELS.index(chapter)
                shutil.copy(f"{output1Path}/questions/{subject}_{paper_number}_{current_question_num}.jpg", f"{BASE_PATH}/images/sorted/{level2}/{subject2}/{chapter_num}/{subject}_{paper_number}_{current_question_num}.jpg")
                answer_object = {
                        "questionName": f"{subject}_{paper_number}_{current_question_num}.jpg",
                        "Answer": answers[current_question_num],
                        "pdfName": m,
                        "questionText": question_text,
                        "Chapter": str(chapter_num),
                        "Level": level,
                        "paperNumber": paper_number[1:],
                        "Subject": subject2
                    }
                questionObjects.append(answer_object)
                current_question_num += 1

with open(f"{BASE_PATH}/python_files/makep1/{subject}_{paper_number}_db.json", 'w') as f:
    f.write("[\n")
    for obj in questionObjects:
        f.write(json.dumps(obj) + ",\n")
    f.write("]")
          
clean_images()