from pdf2image import convert_from_path
import PIL
from PIL import Image
import numpy as np
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import json
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

paperNumber = 4
start = 1
subject = 'phy'
subject2 = 'physics'
level = 'A2'
db = open(f'{subject}_db_p{paperNumber}.json', 'w')
db.write("[")
db.close()

current_question_num = 1

root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 2  # Default is 0
startPixel = 180  # Default is 180

files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
output1Path = r"D:\python_projects\teachmegcse\python_files\makep1\testImages"
heightsArr = [0 for _ in range(100)]

def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin", thread_count=multiprocessing.cpu_count())
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    
    batch_size = 5
    for x in range(startPage, number_of_pages, batch_size):
        batch_end = min(x + batch_size, number_of_pages)
        for page_num in range(x, batch_end):
            if page_num >= startPage:
                page = reader.pages[page_num]
                if page.extract_text().find("BLANK PAGE") == -1:
                    images[page_num].save(f"{output_path}/{i}/{page_num}.jpg", 'JPEG', quality=85, optimize=True)

def strip_images(folder_num):
    pages = sorted(os.listdir(f"{output1Path}/{folder_num}"))
    for page in pages:
        img_path = f"{output1Path}/{folder_num}/{page}"
        with Image.open(img_path) as im:
            img_array = np.array(im)
            cropped_array = img_array[startPixel:2200, :1654]
            im_crop = Image.fromarray(cropped_array)
            im_crop.save(img_path, 'JPEG', quality=85, optimize=True)

def clean_images():
    questions = os.listdir(f"{output1Path}/questions")
    for question in questions:
        img_path = f"{output1Path}/questions/{question}"
        with Image.open(img_path) as im:
            img_array = np.array(im)
            non_white = np.any(img_array != 255, axis=1)
            last_row = np.where(non_white)[0][-1]
            cleaned_array = img_array[:last_row+1, :1500]
            cleaned_image = Image.fromarray(cleaned_array)
            cleaned_image.save(img_path, 'JPEG', quality=85, optimize=True)

def merge_all_images(folder_num):
    pages = sorted(os.listdir(f"{output1Path}/{folder_num}"), key=lambda x: int(x.split(".")[0]))
    height = (len(pages) - 1) * (2200 - startPixel)
    dst_array = np.zeros((height, 1654, 3), dtype=np.uint8)
    current_height = 0
    
    for i in range(1, len(pages)):
        image_path = f"{output1Path}/{folder_num}/{pages[i]}"
        with Image.open(image_path) as image:
            img_array = np.array(image)
            h = 2200 - startPixel
            dst_array[current_height:current_height + h] = img_array
            current_height += h
    
    dst = Image.fromarray(dst_array)
    dst.save(f"{output1Path}/final/final{folder_num}.jpg", 'JPEG', quality=85, optimize=True)
    heightsArr[folder_num] = current_height

def get_dimensions(current_page, prev_pixel, stop_value):
    with Image.open(f"{output1Path}/final/{current_page}") as im:
        img_array = np.array(im)
        column = img_array[prev_pixel:stop_value, 147]
        non_white = np.where(~np.all(column == 255, axis=1))[0]
        if len(non_white) > 0:
            return prev_pixel + non_white[0] - 30
        return stop_value

def take_screenshot(y1, y2, current_question_num, file_name):
    if (y2 - y1) > 300 :
        with Image.open(f"{output1Path}/final/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output1Path}/questions/{subject}_{current_question_num}.jpg")

def process_file(file_tuple):
    index, file = file_tuple
    makeImages(output1Path, file, index)
    strip_images(index)
    merge_all_images(index)
    current_y = 0
    stop_value = heightsArr[index] - 2
    while current_y <= stop_value:
        end_y = get_dimensions(f"final{index}.jpg", current_y, stop_value)
        take_screenshot(current_y, end_y, current_question_num, f"final{index}.jpg")
        current_y = end_y
        if os.path.isfile(f"D:\\python_projects\\teachmegcse\\python_files\\makep1\\testimages\\questions\\{subject}_{current_question_num}.jpg") == True:
            answerObject = {
            "questionName" : f"{subject}_{current_question_num}",
            "questionNum" : current_question_num - start + 1,
            "Subject":subject2,
            "Level":level,
            "paperNumber":paperNumber,
            "pdfName":files[index][-18:]
            }
            answerObjectFormatted = json.dumps(answerObject)
            with open(f'{subject}_db_p{paperNumber}.json', 'a') as db:
                db.write(answerObjectFormatted)
                db.write(",\n")
            current_question_num += 1
    start = current_question_num

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        executor.map(process_file, enumerate(files))

with open(f'{subject}_db_p{paperNumber}.json', 'a') as db:
    db.write("]")