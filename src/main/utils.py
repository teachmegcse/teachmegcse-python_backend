from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import cv2
import pytesseract
from joblib import load
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import requests

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))
outputPath = f"{BASE_PATH}/resources/images/test_images"
CUSTOM_CONFIG = r"--oem 3 --psm 6"


def predict(data, model):
    pipeline = load(f"{BASE_PATH}/resources/sci-kit/{model}")
    data = formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]

def process_image(image_path):
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img, config=CUSTOM_CONFIG)

def select_files():
    root = Tk()
    filetypes = [("PDF Files", "*.pdf")]
    files = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    return list(files)

def makeImages(pdf_path):
    images = convert_from_path(pdf_path)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{outputPath}/currentPdfImages"
    if not os.path.exists(path):
        os.makedirs(path)
    current_index = 1
    for x in range(1, number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        text = page.extract_text()
        text = text.lower()
        if x >= 1:
            # Skip if page contains any of these strings
            skip_strings = [
                "blank page",
                "important values",
                "periodic table",
                "guidance for chemical equations",
                "next page",
                "marking principle",
                "correct answer only",
            ]
            if not any(s in text for s in skip_strings):
                images[x].save(f"{outputPath}/currentPdfImages/{current_index}.jpg", "JPEG")
                current_index += 1

def formatText(text):
    stemmer = PorterStemmer()

    # Convert all text to lowercase
    text = text.lower()

    # Remove punctuation, digits, and non-alphabetic characters
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)

    # Remove Cambridge command words
    text = text.replace("analyse", "")
    text = text.replace("assess", "")
    text = text.replace("calculate", "")
    text = text.replace("comment", "")
    text = text.replace("compare", "")
    text = text.replace("consider", "")
    text = text.replace("contrast", "")
    text = text.replace("define", "")
    text = text.replace("describe", "")
    text = text.replace("develop", "")
    text = text.replace("discuss", "")
    text = text.replace("evaluate", "")
    text = text.replace("explain", "")
    text = text.replace("give", "")
    text = text.replace("identify", "")
    text = text.replace("justify", "")
    text = text.replace("outline", "")
    text = text.replace("predict", "")
    text = text.replace("sketch", "")
    text = text.replace("state", "")
    text = text.replace("suggest", "")
    text = text.replace("summarise", "")
    text = text.replace("benefit", "")
    text = text.replace("drawback", "")
    text = text.replace("advantage", "")
    text = text.replace("disadvantage", "")
    text = text.replace("understand", "")
    text = text.replace("use", "")
    text = text.replace("notes and guidance", "")
    text = text.replace("candidates should be able to", "")
    text = text.replace("show", "")
    text = text.replace("understanding", "")

    # Tokenize text into words
    words = word_tokenize(text)
    # Stem words
    words = [stemmer.stem(w) for w in words]

    # Join the processed words back into a single string
    return " ".join(words)

def strip_images(mode):
    pages = os.listdir(f"{outputPath}/currentPdfImages")
    for i in range(len(pages)):
        with PIL.Image.open(f"{outputPath}/currentPdfImages/{pages[i]}") as im:
            if mode == 'qp':
                im_crop = im.crop((0, 150, 1654, 2200))
            else:
                im_crop = im.crop((100, 200, 2300, 1500))
            im_crop.save(f"{outputPath}/currentPdfImages/{pages[i]}")

def take_screenshot(
    y1, y2, unique_filename
):
    if (y2 - y1) > 300:
        with PIL.Image.open(f"{outputPath}/final/final.jpg") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{outputPath}/questions/{unique_filename}.jpg")
            print(f"Saved question {unique_filename}")
    else:
        print(
            f"Skipping question {unique_filename} - too small ({y2 - y1} pixels)"
        )

def clean_images(level_folder_name, subject, paper_number):
    questions = os.listdir(
        f"{BASE_PATH}/resources/images/{level_folder_name}/{subject}/{paper_number}"
    )
    for i in range(len(questions)):
        im = Image.open(
            f"{BASE_PATH}/resources/images/{level_folder_name}/{subject}/{paper_number}/{questions[i]}"
        )
        pix = im.load()
        flag = False
        if flag == False:
            for y in range(im.height - 2, 1, -2):
                for x in range(im.width - 2, 1, -2):
                    value = pix[x, y]
                    if value != (255, 255, 255):
                        value2 = pix[x + 1, y]
                        if value2 != (255, 255, 255):
                            flag = True
                            break
                if flag:
                    break
        cleaned_image = im.crop((0, 0, 1500, y + 10))
        cleaned_image.save(
            f"{BASE_PATH}/resources/images/{level_folder_name}/{subject}/{paper_number}/{questions[i]}"
        )

def merge_all_images():
    pages = os.listdir(f"{outputPath}/currentPdfImages")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))

    # First pass to get total height
    total_height = 0
    for page_file in pages:
        with PIL.Image.open(f"{outputPath}/currentPdfImages/{page_file}") as im:
            total_height += im.height

    dst = PIL.Image.new("RGB", (1654, total_height), color="white")
    current_height = 0

    # Second pass to merge images
    for page_file in pages:
        image_path = f"{outputPath}/currentPdfImages/{page_file}"
        with PIL.Image.open(image_path) as im:
            dst.paste(im, (0, current_height))
            current_height += im.height

    dst.save(f"{outputPath}/final/final.jpg")
    return current_height

def extract_paper_number(filename):
    try:
        base_name = filename.split(".")[0]

        parts = base_name.split("_")

        if len(parts) >= 4:
            return int(parts[3][0])
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_dimensions_from_api(image_path):
    with open(image_path, "rb") as img:
        files = {"file": img}
        response = requests.post("http://127.0.0.1:8000/predict", files=files)
        if response.status_code == 200:
            coordinates = response.json()
            return coordinates
        else:
            print(f"API response text: {response.text}")
            raise Exception(
                f"API request failed with status code {response.status_code}"
            )

def cleanup():
    for filename in os.listdir(f"{outputPath}/currentPdfImages"):
        file_path = os.path.join(f"{outputPath}/currentPdfImages", filename)
        if os.path.isfile(file_path):  # only delete files
            os.remove(file_path)
            
    for filename in os.listdir(f"{outputPath}/final"):
        file_path = os.path.join(f"{outputPath}/final", filename)
        if os.path.isfile(file_path):  # only delete files
            os.remove(file_path)

    for filename in os.listdir(f"{outputPath}/questions"):
            file_path = os.path.join(f"{outputPath}/questions", filename)
            if os.path.isfile(file_path):  # only delete files
                os.remove(file_path)