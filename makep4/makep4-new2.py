from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import json
from p4_ms_maker import make_question_ms

paperNumber = 4
start = 1
subject = 'phy'
subject2 = 'physics'
level = 'A2'
level2 = 'A-level'
db = open(f"D:\\python_projects\\teachmegcse\\json_files\\{subject}_db_p{paperNumber}.json", 'w')
db.write("[")

# Create an empty mark scheme database file
ms_db = open(f"D:\\python_projects\\teachmegcse\\json_files\\{subject}_db_ms_p{paperNumber}.json", 'w')
ms_db.write("[]")
ms_db.close()

current_question_num = 0

root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 2  # Default is 0
startPixel = 180  # Default is 180

files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
output1Path = r"D:\python_projects\teachmegcse\python_files\makep1\testImages"
finalOutputPath = r"D:\python_projects\teachmegcse\images\unsorted"
heightsArr = [0 for _ in range(100)]


def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin")
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(startPage, number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        if x >= startPage:
            if page.extract_text().find("BLANK PAGE") == -1:
                images[x].save(f"{output_path}/{i}/{x}.jpg", 'JPEG')


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
                        flag = True
                        break
                if flag:
                    break
        cleaned_image = im.crop((0, 0, 1500, y))
        cleaned_image.save(f"{finalOutputPath}/{level2}/{subject2}/p{paperNumber}/{questions[i]}")


def merge_all_images(folder_num):
    pages = os.listdir(f"{output1Path}/{folder_num}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    height = (len(pages) - 1) * (2200 - startPixel)
    dst = PIL.Image.new('RGB', (1654, height), color='black')
    current_height = 0
    for i in range(1, len(pages)):
        image_path = f"{output1Path}/{folder_num}/{pages[i]}"
        image = PIL.Image.open(image_path)
        dst.paste(image, (0, current_height, 1654, current_height + (2200 - startPixel)), mask=None)
        current_height += (2200 - startPixel)
    dst.save(f"{output1Path}/final/final{folder_num}.jpg")
    heightsArr[folder_num] = current_height


def get_dimensions(current_page, prev_pixel, stop_value):
    im = PIL.Image.open(f"{output1Path}/final/{current_page}")
    pix = im.load()
    found = False
    i = 80
    while not found and (prev_pixel + i <= stop_value):
        value = pix[147, prev_pixel + i]
        if value != (255, 255, 255):
            found = True
        else:
            i += 2
    return (prev_pixel + i) - 30


def take_screenshot(y1, y2, current_question_num, file_name):
    if (y2 - y1) > 300 :
        with PIL.Image.open(f"{output1Path}/final/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output1Path}/questions/{subject}_{current_question_num}.jpg")


for m in range(len(files)):
    makeImages(output1Path, files[m], m)
    # Process mark scheme first so the images are ready
    ms_filename = files[m][-18:].replace('qp', 'ms')
    make_question_ms(ms_filename, subject2, 9702)
    
    strip_images(m)
    merge_all_images(m)

    current_y = 0
    stop_value = heightsArr[m] - 2
    while current_y <= stop_value:
        end_y = get_dimensions(f"final{m}.jpg", current_y, stop_value)
        take_screenshot(current_y, end_y, current_question_num, f"final{m}.jpg")
        current_y = end_y
        if os.path.isfile(f"{finalOutputPath}/{level2}/{subject2}/p{paperNumber}/{subject}_{current_question_num}.jpg"):
            answerObject = {
                "questionName" : f"{subject}_{current_question_num}.jpg",
                "questionNum" : current_question_num - start + 1,
                "Subject":subject2,
                "Level":level,
                "paperNumber":paperNumber,
                "pdfName":files[m][-18:]
            }
            answerObjectFormatted = json.dumps(answerObject)
            db.write(answerObjectFormatted)
            db.write(",\n")
        current_question_num += 1
    start = current_question_num

    questions_array = os.listdir(f"{output1Path}/questions")
    clean_images()

db.write("]")
db.close()