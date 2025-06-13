"INCOMPLETE - MORE CHANGES LATER"

import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
CUSTOM_CONFIG = r'--oem 3 --psm 6'

from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfReader
from tkinter import filedialog, Tk
import requests
from joblib import load
import cv2
import pytesseract
import shutil
import json
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import io

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
PDF_PATH = rf"{BASE_PATH}/resources/pdfs"

ALL_LABELS = ['Atomic structure', 'Atoms, molecules and stoichiometry', 
             'Chemical bonding', 'States of matter', 'Chemical energetics', 'Electrochemistry', 'Equilibria',
               'Reaction kinetics', 'The Periodic Table: chemical periodicity', 'Group 2', 'Group 17', 'Nitrogen and sulfur', 'introduction to AS Level organic chemistry', 
               'Hydrocarbons', 'Halogen compounds', 'Hydroxy compounds', 'Carbonyl compounds', 'Carboxylic acids and derivatives', 'Nitrogen compounds', 'Polymerisation',
                 'Organic synthesis', 'Analytical techniques']

subject = 'a_chem'
paper_number = 'p1'
code = '9701'
start_chapter = 1
model = 'aschem'
level = 'AS' # A2, AS or IGCSE
level_folder_name = 'a-level' # a-level or igcse
subject2 = 'chemistry' # physics, chemistry, biology
num_of_questions = 40


MODEL_PATH_TEMPLATE = f"{BASE_PATH}/resources/sci-kit/{model}.joblib"
current_question_num = 1
root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 1 # Default is 1
startPixel = 150  # Default is 150
questionObjects = []

files = filedialog.askopenfilenames(filetypes=filetypes)
output1Path = f"{BASE_PATH}/resources/images/test_images"


def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(number_of_pages):
        if x >= startPage:
            images[x].save(f"{output_path}/{i}/{x}.jpg", 'JPEG')

def get_y_coordinates(file_name, folderNum):
    image_path = f"{output1Path}/{folderNum}/{file_name}"
    im = Image.open(image_path)
    # Convert the image to a byte stream
    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, format='JPEG')  # or 'PNG' depending on your image format
    img_byte_arr.seek(0)

    # Prepare files payload with the correct content
    files = {'file': ('image.jpg', img_byte_arr, 'image/jpeg')}
    
    response = requests.post('http://127.0.0.1:8000/predict', files=files)
    response.raise_for_status()  # This raises an error for bad responses (4xx, 5xx)

    y_coordinates = response.json()
    return y_coordinates


def strip_images(folder_num):
    pages = os.listdir(rf"{output1Path}/{folder_num}")
    for i in range(len(pages)):
        img_path = os.path.join(output1Path, str(folder_num), pages[i])
        with Image.open(img_path) as im:
            im_crop = im.crop((0, startPixel, 1654, 2200))
            im_crop.save(img_path)


def clean_images():
        questions = os.listdir(f"{BASE_PATH}/resources/images/{level_folder_name}/{subject2}/{paper_number}")
        for i in range(len(questions)):
            im = Image.open(f"{BASE_PATH}/resources/images/{level_folder_name}/{subject2}/{paper_number}/{questions[i]}")
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
            cleaned_image.save(f"{BASE_PATH}/resources/images/{level_folder_name}/{subject2}/{paper_number}/{questions[i]}")


def take_screenshot(y1, y2, file_name, folderNum):
    global current_question_num
    if (y2 - y1) > 150 :
        with Image.open(f"{output1Path}/{folderNum}/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output1Path}/questions/{subject}_{paper_number}_{current_question_num + (folderNum * num_of_questions)}.jpg")
    else :
        current_question_num -= 1

def predict(data, model):
    pipeline = load(MODEL_PATH_TEMPLATE.format(model=model))
    data = formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]

def process_image(image_path, custom_config=CUSTOM_CONFIG):
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img, config=custom_config)

def extract_answers_from_pdf(code, pdfName):
    pdfName = pdfName.replace('qp', 'ms')
    pdfPath = rf"{PDF_PATH}\{code}\{pdfName}"
    pdf_reader = PdfReader(open(pdfPath, "rb"))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    lines = text.split('\n')
    answers = []
    for line in lines:
        line = line.strip()
        parts = line.split()
        # Check if the line contains a question number followed by an answer
        if len(parts) >= 2 and parts[0].isdigit() and len(parts[1]) == 1 and parts[1].isalpha():
            answer = parts[1]
            answers.append(answer)
    
    return answers

def formatText(text):
    stemmer=PorterStemmer()

    # Convert all text to lowercase
    text = text.lower()

    # Remove punctuation, digits, and non-alphabetic characters
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    
    # Remove Cambridge command words
    text = text.replace("analyse",""); text = text.replace("assess",""); text = text.replace("calculate","")
    text = text.replace("comment",""); text = text.replace("compare",""); text = text.replace("consider","")
    text = text.replace("contrast",""); text = text.replace("define",""); text = text.replace("describe","")
    text = text.replace("develop",""); text = text.replace("discuss",""); text = text.replace("evaluate","")
    text = text.replace("explain",""); text = text.replace("give",""); text = text.replace("identify","")
    text = text.replace("justify",""); text = text.replace("outline",""); text = text.replace("predict","")
    text = text.replace("sketch",""); text = text.replace("state",""); text = text.replace("suggest","")
    text = text.replace("summarise",""); text = text.replace("benefit",""); text = text.replace("drawback","")
    text = text.replace("advantage",""); text = text.replace("disadvantage",""); text = text.replace("understand","")
    text = text.replace("use",""); text = text.replace("notes and guidance",""); text = text.replace("candidates should be able to","")
    text = text.replace("show",""); text = text.replace("understanding","")

    # Tokenize text into words
    words = word_tokenize(text)
    # Stem words
    words = [stemmer.stem(w) for w in words]

    # Join the processed words back into a single string
    return ' '.join(words)


for m in range(len(files)):
    makeImages(output1Path, files[m], m)
    print(f"Processing {files[m]}...")

    strip_images(m)
    pages = os.listdir(f"{output1Path}/{m}")
    current_file = files[m].rsplit('/', 1)[-1]
    answers = extract_answers_from_pdf(code, current_file)
    current_question_num = 1
    for k in range(len(pages)):
        y_coordinates = get_y_coordinates(f"{k + 1}.jpg", m)
        # Filter boxes where x1 < 250 and extract their y2 (i.e. box[1])
        raw_y2_list  = sorted(box[1] for box in y_coordinates if box[0] < 160)
        threshold = 10  # adjust as needed depending on your use case
        y2_list = []
        for y2 in raw_y2_list:
            if not y2_list or abs(y2 - y2_list[-1]) > threshold:
                y2_list.append(y2)
        if len(y2_list):
            for j in range(len(y2_list)):
                file_name = f"{subject}_{paper_number}_{current_question_num + (m * num_of_questions)}"
                if j == len(y2_list) - 1:
                    take_screenshot(y2_list[j], 2050, f"{k + 1}.jpg", m)
                else:
                    take_screenshot(y2_list[j], y2_list[j + 1], f"{k + 1}.jpg", m)
                if os.path.exists(f"{output1Path}/questions/{file_name}.jpg"):
                    question_text = process_image(f"{output1Path}/questions/{file_name}.jpg", CUSTOM_CONFIG).lower().strip()
                    chapter = predict(question_text, model)
                    chapter_num = start_chapter + ALL_LABELS.index(chapter)

                    shutil.copy(f"{output1Path}/questions/{file_name}.jpg", f"{BASE_PATH}/resources/images/{level_folder_name}/{subject2}/{paper_number}/{file_name}.jpg")
                    print(f"{question_text} \n question number: {current_question_num} \n")
                    answer_object = {
                            "questionName": f"{file_name}.jpg",
                            "Answer": answers[current_question_num - 1],
                            "pdfName": current_file,
                            "questionText": question_text,
                            "Chapter": chapter_num,
                            "Level": level,
                            "paperNumber": int(paper_number[1:]),
                            "Subject": subject2
                        }
                    questionObjects.append(answer_object)
                current_question_num += 1

with open(f"{BASE_PATH}/resources/json/test_images.json", 'w') as f:
    f.write("[\n")
    for obj in questionObjects:
        f.write(json.dumps(obj) + ",\n")
    f.write("]")
          
clean_images()