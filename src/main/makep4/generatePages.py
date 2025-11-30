import os
import sys
import uuid
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
import re

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)
outputPath = f"{BASE_PATH}/resources/images/test_images"

from main.utils import select_files


def delete_numeric_files():
    path = f"{outputPath}/currentPdfImages"
    files = os.listdir(path)

    for f in files:
        if f.endswith(".jpg") and re.fullmatch(r"\d+\.jpg", f):
            os.remove(os.path.join(path, f))

def makeImages(currentImageIndex, pdf_path):
    images = convert_from_path(pdf_path)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{outputPath}/currentPdfImages"
    if not os.path.exists(path):
        os.makedirs(path)
    current_index = 1 + currentImageIndex

    for x in range(1, number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        text = page.extract_text().lower()

        # Skip if page contains unwanted strings
        skip_strings = [
            "blank page",
            "important values",
            "guidance for chemical equations",
            "next page",
            "marking principle",
            "correct answer only",
        ]
        if not any(s in text for s in skip_strings):
            images[x].save(f"{path}/{current_index}.jpg", "JPEG")
            current_index += 1

    return current_index


def rename_all_to_random():
    path = f"{outputPath}/currentPdfImages"
    files = [f for f in os.listdir(path) if f.endswith(".jpg")]

    for old_name in files:
        old_path = os.path.join(path, old_name)
        new_name = f"{uuid.uuid4().hex}.jpg"
        new_path = os.path.join(path, new_name)
        os.rename(old_path, new_path)


files = select_files()

current_index = 0
for file in files:
    num = makeImages(current_index, file)
    current_index = num

rename_all_to_random()

delete_numeric_files()