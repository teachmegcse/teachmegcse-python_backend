from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
from pathConst import BASE_PATH, POPPLER_PATH, TESSERACT_PATH

def select_files():
    root = Tk()
    filetypes = [("PDF Files", "*.pdf")]
    files = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    return list(files)

def strip_images(output_path):
    pages = os.listdir(output_path)
    for page in pages:
        if page.endswith('.jpg'):
            image_path = os.path.join(output_path, page)
            with PIL.Image.open(image_path) as im:
                im_crop = im.crop((0, 200, 2339, 1500))
                im_crop.save(image_path)

def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    current_index = 1
    for x in range(1, number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        text = page.extract_text()
        text = text.lower()
        if x >= 1:
            # Skip if page contains any of these strings
            skip_strings = ["blank page", "important values", "periodic table", "next page", "guidance", "marking principle"]
            if not any(s in text for s in skip_strings):
                images[x].save(f"{output_path}/pdf_{i}_page_{current_index}.jpg", 'JPEG')
                current_index += 1

if __name__ == "__main__":
    files = select_files()
    output_path = f"{BASE_PATH}/python_files/makep1/testImages"
    for i in range(len(files)):
        makeImages(output_path, files[i], i)
    strip_images(output_path)