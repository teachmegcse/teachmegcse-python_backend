from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
import pdfplumber
from tkinter import filedialog, Tk
import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import cv2
from joblib import load
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import requests
import easyocr
import numpy as np

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))
outputPath = f"{BASE_PATH}/resources/images/test_images"
CUSTOM_CONFIG = r"--oem 3 --psm 6"
READER = easyocr.Reader(["en"])


def predict(data: str, model: str) -> str:
    """Takes a text string from a question and a model name that references the level and subject, and returns a predicted chapter label.

    Args:
        data (str): The text string from the question.
        model (str): The name of the model to use for prediction.

    Returns:
        str: The predicted chapter label.
    """
    pipeline = load(f"{BASE_PATH}/resources/sci-kit/{model}")
    data = formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]


def process_image(image_path: str) -> str:
    """Takes an image path, processes the image using OCR, and returns the extracted text.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image (using easyocr).

    """
    img = cv2.imread(image_path)
    results = READER.readtext(img, detail=0)
    return "\n".join(results)


def select_files() -> list:
    """Opens a file dialog for the user to select PDF files and returns a list of the selected past papers.

    Args:
    Returns:
        list: A list of past paper paths for the selected PDF files.

    """
    root = Tk()
    filetypes = [("PDF Files", "*.pdf")]
    files = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    return list(files)


def makeImages(pdf_path: str) -> None:
    """Takes a PDF path, converts the PDF into images, and saves the images in a specified output directory (outputPath).
      It also skips pages that contain certain predefined strings like "blank page" or "important values".

    Args:
    pdf_path (str): The path to the PDF file to be processed.

    Returns:
        None: The function does not return anything, but it saves the processed images to the specified output directory.
    """
    images = convert_from_path(pdf_path)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)

    path = f"{outputPath}/currentPdfImages"
    os.makedirs(path, exist_ok=True)

    skip_strings = [
        "blank page",
        "important values",
        "guidance for chemical equations",
        "next page",
        "marking principle",
        "correct answer only",
        "use this page for any rough working",
        "test and test result",
        "reactions of cations",
        "reactions of aqueous anions",
        "reactions of aqueous cations",
    ]

    current_index = 1

    with pdfplumber.open(pdf_path) as plumber:
        for x in range(1, number_of_pages):
            try:
                page = plumber.pages[x]
                text = (page.extract_text() or "").lower()
            except Exception as exc:
                print(f"[WARN] Page {x + 1} → pdfplumber extract_text failed: {exc}")
                text = ""

            matched = [s for s in skip_strings if s in text]

            if matched:
                print(f"[SKIPPED] Page {x + 1} → matched: {', '.join(matched)}")
                continue

            images[x].save(f"{path}/{current_index}.jpg", "JPEG")
            print(f"[SAVED] Page {x + 1} → image {current_index}.jpg")

            current_index += 1


def formatText(text: str) -> str:
    """Takes a text string, processes it by converting to lowercase, removing punctuation and digits,
      removing Cambridge command words, tokenizing, and stemming the words.
      (used before chapter prediction to keep only the most relevant information for the model and reduce noise in the data)

    Args:
        text (str): The input text string from the question to be processed.

    Returns:
        str: The processed text string after formatting and removing noise.

    """
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


def strip_images(mode: str) -> None:
    """Takes a mode (either "qp" for question paper or "ms" for mark scheme)
      and crops the images in the currentPdfImages directory accordingly
        to remove irrelevant information such as page numbers, headers, and footers.

    Args:
    mode (str): The mode indicating whether the images are from a question paper ("qp")
      or a mark scheme ("ms"), which determines the cropping dimensions.

    Returns:
        None: The function does not return anything, but it modifies the images in place by cropping them and saving the stripped version back to the same location.
    """
    pages = os.listdir(f"{outputPath}/currentPdfImages")
    for i in range(len(pages)):
        with PIL.Image.open(f"{outputPath}/currentPdfImages/{pages[i]}") as im:
            if mode == "qp":
                im_crop = im.crop((0, 150, 1654, 2200))
            else:
                im_crop = im.crop((100, 200, 2300, 1500))
            im_crop.save(f"{outputPath}/currentPdfImages/{pages[i]}")


def take_screenshot(
    y1: int, y2: int, unique_filename: str, type: str, page: int
) -> bool:
    """Takes the y1 and y2 coordinates of the question region (x coordinates are fixed),
      a unique filename for the question image, the type of question (either "mcq" or "long"), and the page number to crop the question from.
      It crops the corresponding region from the correct image (based on type) and saves it to the questions folder with the unique filename.
      It also checks if the height of the cropped region is above a certain threshold (300 pixels for long questions and 100 pixels for MCQs)
        before saving, to filter out any mistakes (they're height is like 30 pixels so obviously wrong).

    Args:
    y1 (int): The y-coordinate of the top of the question region to be cropped.
    y2 (int): The y-coordinate of the bottom of the question region to be cropped.
    unique_filename (str): A unique filename to save the cropped question image as.
    type (str): The type of question, either "mcq" for multiple-choice questions or "long" for long-answer questions,
        which determines the cropping dimensions and source image
    page (int): The page number to crop the question from (used to determine which image to crop from based on type).

    Returns:
     bool: True if the question image was successfully saved, False if it was skipped due to being too small or if there was an error during saving.
    """
    # type can either be mcq or long
    height = y2 - y1

    if type == "long" and height <= 300:
        print(f"Skipping question {unique_filename} - too small ({height} pixels)")
        return False

    if type == "mcq" and height <= 100:
        print(f"Skipping question {unique_filename} - too small ({height} pixels)")
        return False

    # Open the correct image based on type
    if type == "long":
        image_path = f"{outputPath}/final/final.jpg"
    else:
        image_path = f"{outputPath}/currentPdfImages/{page}"

    try:
        with PIL.Image.open(image_path) as im:
            # Crop the region
            im_crop = im.crop((100, y1, 1600, y2))

            # Save to questions folder
            save_path = f"{outputPath}/questions/{unique_filename}.jpg"
            im_crop.save(save_path)

            print(f"Saved question {unique_filename}")

        return True
    except Exception as e:
        print(f"Error saving question {unique_filename}: {e}")
    return False


def clean_image(
    level_folder_name: str, subject: str, paper_number: str, image_name: str
) -> None:
    # level_folder_name is either "IGCSE" or "A-level"
    """Unlike strip_image which removes the same fixed region for all pages before processing,
    this function is for questions where it removes the whitespace at the bottom dynamically to save space

    Args:
    level_folder_name (str): The name of the level folder (e.g., "IGCSE" or "A-level") where the image is located (based on the actual folder structure).
    subject (str): The subject of the paper (e.g., "physics", "chemistry", "biology") where the image is located (based on the actual folder structure).
    paper_number (str): The paper number (e.g., "p1", "p2") where the image is located (based on the actual folder structure).
    image_name (str): The name of the image file to be cleaned.

    Returns:
     None: The function does not return anything, but it modifies the image in place by cropping it and saving the cleaned version back to the same location.
    """
    im = PIL.Image.open(
        f"{BASE_PATH}/resources/images/{level_folder_name}/{subject}/{paper_number}/{image_name}"
    )
    pix = im.load()
    flag = False
    if not flag:
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
            f"{BASE_PATH}/resources/images/{level_folder_name}/{subject}/{paper_number}/{image_name}"
        )


def merge_all_images() -> None:
    """Merges all the page images in the currentPdfImages directory into a single long image and saves it to the final folder as final.jpg.
     The images are merged vertically in the order of their page numbers (sorted by filename).
     This is used to create a single image of the entire question paper for easier cropping of long questions that may span multiple pages

     Args:
        None: The function does not take any arguments, but it processes the images in the currentPdfImages directory

    Returns:
        None: The function does not return anything, but it saves the merged image to the folder called final as final.jpg.

    """
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


def extract_paper_number(filename: str) -> int | None:
    """Extracts the paper number from a given filename string. The filename uses the format A_B_C_D.pdf
    where A is a 4 digit integer that represents the subject and level (e.g., 0625 for IGCSE, 9709 for A-level),
      B is the session and year like m23 so it was released in the march session of 2023,
    C is either "qp" or "ms" to indicate question paper or mark scheme, and D is the paper number and variant number like 23 for paper 2 variant 3.

    Args:
    filename (str): The filename string from which to extract the paper number, following the format A_B_C_D.pdf.
    Returns:
    int: The extracted paper number (first digit of D) as an integer, or None if the paper number cannot be extracted due to an error or unexpected filename format.

    """
    try:
        base_name = filename.split(".")[0]

        parts = base_name.split("_")

        if len(parts) >= 4:
            return int(parts[3][0])
    except Exception as e:
        print(f"Error: {e}")
    return None


def get_dimensions_from_api(image_path: str, mode: str = "long-double") -> list:
    """Takes an image path and sends it to the local YOLO model running from coordinates.py
      to get the predicted bounding box coordinates for the question regions in the image.

    Args:
    image_path (str): The path to the image file to be processed by the API.
    Returns:
        list: A list of bounding box coordinates for the question regions in the image,
          where each bounding box is represented as a list of four integers [x1, y1, x2, y2].

    """
    try:
        with open(image_path, "rb") as img:
            files = {"file": img}
            response = requests.post(
                f"http://127.0.0.1:8000/predict?mode={mode}", files=files
            )
            if response.status_code == 200:
                coordinates = response.json()
                return coordinates
            print(f"API response text: {response.text}")
            raise Exception(
                f"API request failed with status code {response.status_code}"
            )
    except Exception as exc:
        print(f"⚠️ API request failed for {image_path}: {exc}")
        return []


def cleanup() -> None:
    """Cleans up the output directories by deleting all files in the currentPdfImages, final, questions, and vision_output_images folders.
        This is used to reset the state before processing a new PDF to avoid any interference from previous runs.

    Args:        None: The function does not take any arguments, but it processes the files in the specified output directories.
    Returns:        None: The function does not return anything, but it deletes the files in the specified output directories to clean up the state for the next run.

    """
    dirs = [
        f"{outputPath}/currentPdfImages",
        f"{outputPath}/final",
        f"{outputPath}/questions",
        f"{BASE_PATH}/resources/images/vision_output_images",
    ]

    for d in dirs:
        for filename in os.listdir(d):
            file_path = os.path.join(d, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)


def get_level_and_chapter(
    formatted_text: str, paper_num: int, paperType: str, currentDefinitionsData: dict
) -> tuple[str, int]:
    """Takes the formatted text of a question, the paper number, the paper type (either "IGCSE" or "A-level"),
      and the current definitions data loaded from the JSON file.

      args:
        formatted_text (str): The formatted text of the question to be used for chapter prediction.
        paper_num (int): The paper number (e.g., 1 or 2) extracted from the filename, used to determine which model to use for A-level papers.
        paperType (str): The type of paper, either "IGCSE" or "A-level", used to determine which model and labels to use for chapter prediction.
        currentDefinitionsData (dict): The definitions data loaded from the JSON file for the current paper code, which contains information about the models and
            labels for chapter prediction based on the paper type and number.

    Returns:
        tuple: A tuple containing the predicted level (e.g., "IGCSE", "AS", "A2")
          and the predicted chapter number (as an integer index based on the labels in the definitions data)
            for the given question text, paper number, and paper type.
    """
    # implicit level = IGCSE as all IGCSE have format 06.. while A-level have 97..
    if paperType == "IGCSE":
        IGModel = currentDefinitionsData["IGmodel"]
        ALL_LABELS = currentDefinitionsData["chapters"]
        level = "IGCSE"
        chapter = predict(formatted_text, IGModel)
        chapter_num = ALL_LABELS.index(chapter) + 1 if chapter in ALL_LABELS else 0
    else:
        ASModel = currentDefinitionsData["ASModel"]
        A2Model = currentDefinitionsData["A2Model"]
        ASpapers = currentDefinitionsData["ASpapers"]
        A2papers = currentDefinitionsData["A2papers"]
        ASLabels = currentDefinitionsData["ASChapters"]
        A2Labels = currentDefinitionsData["A2Chapters"]

        if paper_num in ASpapers:
            level = "AS"
            chapter = predict(formatted_text, ASModel)
            chapter_num = ASLabels.index(chapter) + 1 if chapter in ASLabels else 0
        elif paper_num in A2papers:
            level = "A2"
            chapter = predict(formatted_text, A2Model)
            chapter_num = (
                A2Labels.index(chapter) + 1 + len(ASLabels)
                if chapter in A2Labels
                else 0
            )
    return level, chapter_num


def extract_answers_from_pdf(code: str, pdfName: str) -> list:
    """This function is only for mcq as the answers are like A, B etc while in long the answers are images from the mark scheme
      Takes the paper code and the PDF name, constructs the path to the corresponding mark scheme PDF,
      extracts the text from the mark scheme using PyPDF2, and processes the text
        to extract the answers for each question based on the expected format of the mark scheme
          (where each line contains a question number followed by the answer).

    Args:
    code (str): The paper code (e.g., "0625" for IGCSE, "9709" for A-level) used to determine the path to the mark scheme PDF based on the folder structure.
    pdfName (str): The name of the PDF file for which the answers are to be extracted, used to determine the corresponding mark scheme PDF name by replacing "qp" with "ms".

    Returns:
        list: A list of answers (30 if economics and 40 otherwise) extracted from the mark scheme PDF, where each answer corresponds to a question in the question paper,
          and the answers are extracted based on the expected format of the mark
    """
    pdfName = pdfName.replace("qp", "ms")
    pdfPath = f"{BASE_PATH}/resources/full_pdfs/{code}/{pdfName}"
    pdf_reader = PdfReader(open(pdfPath, "rb"))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    lines = text.split("\n")
    answers = []
    for line in lines:
        line = line.strip()
        parts = line.split()
        # Check if the line contains a question number followed by an answer
        if (
            len(parts) >= 2
            and parts[0].isdigit()
            and len(parts[1]) == 1
            and parts[1].isalpha()
        ):
            answer = parts[1]
            answers.append(answer)

    return answers
