import cv2
import pytesseract
import os
import MS2
import json
import re
from tkinter import Tk, filedialog
from joblib import load
import getFormattedTextfromPdf
import shutil
from pathConst import basePath, tesseractPath

# Constants
TESSERACT_CMD = tesseractPath
CUSTOM_CONFIG = r'--oem 3 --psm 6'
JSON_PATH = rf"{basePath}\json_files"
IMAGE_PATH_TEMPLATE = "D:/python_projects/teachmegcse/images/unsorted/{level2}/{subject2}/{paperNumber}/{subject}_{paperNumber}_{qnumber}.jpg"
SORTED_PATH_TEMPLATE = "D:/python_projects/teachmegcse/images/sorted/{level2}/{subject2}/{paperNumber}/{chapterNum}"
MODEL_PATH_TEMPLATE = "D:/python_projects/teachmegcse/python_files/sci-kit/{model}.joblib"

# Labels
ALL_LABELS = ['Utility', 'Indifference curves and budget lines', 
             'Efficiency and market failure', 'Private costs and benefits, externalities and social costs and benefits ',
               'Types of cost, revenue and profit, short-run and long-run production',
               'market structures', 'Growth and survival of firms',
               'objectives and policies of firms', 'Government policies to achieve efficient resource allocation',
                'Equity and redistribution of income and wealth', 'Labour market forces and government intervention', 'The circular flow of income',
               'Economic growth and sustainability', 'Employment/unemployment', 'Money and banking', 'Government macroeconomic policy objectives',
               'balance of payments', 'Economic development', 'levels of development']

# Initialization
root = Tk()
filetypes = [("PDF Files", "*.pdf")]

# Functions
def get_pdf_files():
    files = filedialog.askopenfilenames(filetypes=filetypes)
    return [os.path.basename(f).replace('q', 'm').replace('p', 's', 1).replace('.pdf', '') for f in files]

def predict(data, model):
    pipeline = load(MODEL_PATH_TEMPLATE.format(model=model))
    data = getFormattedTextfromPdf.formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]

def extract_question_number(text):
    question_number = text[:2]
    question_number = re.sub(r'[^\w\s]', '', question_number)
    try:
        return int(question_number)
    except ValueError:
        return None

def process_image(image_path, custom_config):
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img, config=custom_config)

def write_json(f, answer_object):
    answer_object_formatted = json.dumps(answer_object)
    f.write(answer_object_formatted + ",\n")

def main():
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
    pdf_files = get_pdf_files()

    index = 0
    qnumber = 0
    question_number = 0

    subject = 'A_eco'
    subject2 = 'economics'
    paperNumber = 'p3'
    paper_number2 = 3
    model = 'a2eco'
    level = "A2"
    start_chapter = 12 # Default is 1 when AS but not 1 when A2
    level2 = 'A-level' # A-level or IGCSE
    code = '9708'
    num_of_questions = 1425
    num_of_questions_in_paper = 30
    
    json_file_path = os.path.join(JSON_PATH, f'{subject}_{paperNumber}_db.json')
    with open(json_file_path, 'w') as f:
        f.write("[\n")
        
        pdf_name = pdf_files[index]
        answers = MS2.extract_answers_from_pdf(code, pdf_name)
        print(pdf_name, answers, len(answers))

        while qnumber <= num_of_questions:
            image_path = IMAGE_PATH_TEMPLATE.format(
                level2=level2, subject2=subject2, paperNumber=paperNumber, subject=subject, qnumber=qnumber)
            if os.path.isfile(image_path):
                if question_number is not None and question_number % num_of_questions_in_paper == 0 and qnumber > 20 and question_number != 0:
                    index += 1
                    pdf_name = pdf_files[index]
                    answers = MS2.extract_answers_from_pdf(code, pdf_name)
                    print(pdf_name, answers, len(answers))

                question_text = process_image(image_path, CUSTOM_CONFIG).lower().strip()
                question_number = extract_question_number(question_text)

                try:
                    question_answer = answers[question_number - 1] if question_number is not None else ''
                except IndexError:
                    question_answer = ''
                
                chapter = predict(question_text, model)
                chapter_num = start_chapter + ALL_LABELS.index(chapter)
                chapter_path = SORTED_PATH_TEMPLATE.format(
                    level2=level2, subject2=subject2, paperNumber=paperNumber, chapterNum=chapter_num)

                if not os.path.exists(chapter_path):
                    os.makedirs(chapter_path)
                
                shutil.copy2(image_path, os.path.join(chapter_path, f"{subject}_{paperNumber}_{qnumber}.jpg"))

                pdf_name2 = pdf_name.replace('ms', 'qp')

                if question_answer and question_number is not None:
                    answer_object = {
                        "questionName": f"{subject}_{paperNumber}_{qnumber}.jpg",
                        "Answer": question_answer,
                        "pdfName": pdf_name2,
                        "questionText": question_text,
                        "Chapter": str(chapter_num),
                        "Level": level,
                        "paperNumber": paper_number2,
                        "Subject": subject2
                    }
                    write_json(f, answer_object)
                
            qnumber += 1
        
        f.write("]")

if __name__ == "__main__":
    main()
