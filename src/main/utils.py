from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
import pypdfium2 as pdfium
from tkinter import filedialog, Tk
import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import json
import cv2
from joblib import load
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import easyocr
import numpy as np
import shutil
import threading
from functools import lru_cache, wraps

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))
outputPath = f"{BASE_PATH}/resources/images/test_images"
CUSTOM_CONFIG = r"--oem 3 --psm 6"
READER = easyocr.Reader(["en"])
# EasyOCR isn't safe to call from several threads at once, so all OCR goes through read_text()
OCR_LOCK = threading.Lock()
# pypdfium2 isn't safe to call from several threads at once either (PDFs are processed in parallel, see PDF_WORKERS),
# so every use of it goes through this lock. Re-entrant, as the text-layer functions call each other
PDFIUM_LOCK = threading.RLock()
# Number of PDFs processed at the same time (override with the PDF_WORKERS environment variable)
PDF_WORKERS = int(os.environ.get("PDF_WORKERS", 4))


def read_text(image, **kwargs) -> list:
    """Thread-safe wrapper around READER.readtext, takes the same arguments."""
    with OCR_LOCK:
        return READER.readtext(image, **kwargs)


def load_json_db(path: str) -> list:
    """Reads a JSON DB (a list of records), treating a missing or empty file as an empty DB, e.g. one cleared to start
    over."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return json.loads(content) if content.strip() else []


def make_work_dir(name: str) -> str:
    """Creates an empty scratch folder (with currentPdfImages and questions subfolders) for processing a single PDF,
    so PDFs processed in parallel never read or overwrite each other's page or question images.

    Args:
    name (str): A name unique to the PDF being processed (e.g. its filename without .pdf).

    Returns:
        str: The path to the scratch folder, to pass as work_dir to the other helpers.
    """
    work_dir = f"{outputPath}/work/{name}"
    shutil.rmtree(work_dir, ignore_errors=True)
    os.makedirs(f"{work_dir}/currentPdfImages")
    os.makedirs(f"{work_dir}/questions")
    return work_dir


def predict(data: str, model: str) -> str:
    """Takes a text string from a question and a model name that references the level and subject, and returns a predicted chapter label.

    Args:
        data (str): The text string from the question.
        model (str): The name of the model to use for prediction.

    Returns:
        str: The predicted chapter label.
    """
    pipeline = _load_pipeline(model)
    data = formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]


@lru_cache(maxsize=None)
def _load_pipeline(model: str):
    # Loading a joblib pipeline from disk is slow, so each model is only loaded once per run
    return load(f"{BASE_PATH}/resources/sci-kit/{model}")


def process_image(image_path: str) -> str:
    """Takes an image path, processes the image using OCR, and returns the extracted text.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image (using easyocr).

    """
    img = cv2.imread(image_path)
    results = read_text(img, detail=0)
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


# Pages containing any of these are left out: blank and rough-working pages, data/reference pages
# (periodic table, qualitative analysis notes, important values) and mark scheme guidance pages
SKIP_STRINGS = [
    "blank page",
    "important values",
    "guidance for chemical equations",
    "next page",
    "marking principle",
    "correct answer only",
    "use this page for any rough working",
    "test and test result",
    "reactions of cations",
    "reactions of anions",
    "reactions of aqueous anions",
    "reactions of aqueous cations",
    "notes for use in qualitative analysis",
    "the periodic table of elements",
    "the periodic table of the elements",
]
# Mark scheme guidance pages can show marks like "[1]" in their examples, so these skip a page even with marks on it
MARK_SCHEME_GUIDANCE = {"marking principle", "correct answer only", "guidance for chemical equations"}
# A mark like "[2]" or "[Total: 7]", only ever printed next to a question. A page with one is kept even when it also
# has a skip string, e.g. the end of a question on the same page as the "Important values" box (9701 s23 42) or the
# copyright notice (0625 w22 53), or a page saying "... on the next page" (0620 m18 32)
MARK_BRACKET = re.compile(r"\[\s*(total\s*:?\s*)?\d+\+?\s*\]", re.I)


def page_skip_reason(text: str) -> str | None:
    """Takes the text of a page and returns why it should be left out, or None if it should be kept.

    Args:
    text (str): The text of the page.

    Returns:
        str | None: A short reason like "matched: blank page" or "copyright page", or None to keep the page.
    """
    text = " ".join(text.lower().split())
    has_marks = MARK_BRACKET.search(text) is not None
    matched = [s for s in SKIP_STRINGS if s in text]
    if matched and (not has_marks or any(s in MARK_SCHEME_GUIDANCE for s in matched)):
        return f"matched: {', '.join(matched)}"
    # Some papers end with a page holding only the copyright acknowledgements. Question pages can have the same
    # notice as a footer (and the notice can come first in the page's text), so the notice is removed and the page
    # is only left out when (almost) nothing else is left. The notice always ends "... university of cambridge."
    if not has_marks and ("permission to reproduce items" in text or "to avoid the issue of disclosure" in text):
        rest = re.sub(
            r"(permission to reproduce items|to avoid the issue of disclosure).*?university of cambridge\s*\.", "", text
        )
        rest = re.sub(r"©\s*ucles\s*\d{4}|\d{4}/\d{2}/[a-z]/[a-z]/\d{2}", "", rest)
        if len(re.findall(r"[a-z]", rest)) < 30:
            return "copyright page"
    return None


def makeImages(pdf_path: str, work_dir: str = outputPath) -> None:
    """Takes a PDF path, converts the PDF into images, and saves the images in a specified output directory (outputPath).
      It also skips the first page and pages that aren't questions (see page_skip_reason), like blank pages,
      the periodic table or the qualitative analysis notes.

    Args:
    pdf_path (str): The path to the PDF file to be processed.
    work_dir (str): The folder whose currentPdfImages subfolder the pages are saved to (see make_work_dir).

    Returns:
        None: The function does not return anything, but it saves the processed images to the specified output directory.
    """
    images = convert_from_path(pdf_path, thread_count=os.cpu_count() or 1)
    number_of_pages = len(images)

    path = f"{work_dir}/currentPdfImages"
    os.makedirs(path, exist_ok=True)

    current_index = 1

    # pypdfium2 rather than pdfplumber, as pdfplumber can't read the text of some recent papers (it comes out as "(cid:44)...")
    with PDFIUM_LOCK:
        document = pdfium.PdfDocument(pdf_path)
        try:
            texts = []
            for x in range(number_of_pages):
                try:
                    texts.append(document[x].get_textpage().get_text_range())
                except Exception as exc:
                    print(f"[WARN] Page {x + 1} → text extraction failed: {exc}")
                    texts.append("")
        finally:
            document.close()

    for x in range(1, number_of_pages):
        reason = page_skip_reason(texts[x])
        if reason:
            print(f"[SKIPPED] Page {x + 1} → {reason}")
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


def strip_images(mode: str, work_dir: str = outputPath) -> None:
    """Takes a mode (either "qp" for question paper or "ms" for mark scheme)
      and crops the images in the currentPdfImages directory accordingly
        to remove irrelevant information such as page numbers, headers, and footers.

    Args:
    mode (str): The mode indicating whether the images are from a question paper ("qp")
      or a mark scheme ("ms"), which determines the cropping dimensions.
    work_dir (str): The folder whose currentPdfImages subfolder holds the pages (see make_work_dir).

    Returns:
        None: The function does not return anything, but it modifies the images in place by cropping them and saving the stripped version back to the same location.
    """
    pages = os.listdir(f"{work_dir}/currentPdfImages")
    for i in range(len(pages)):
        with PIL.Image.open(f"{work_dir}/currentPdfImages/{pages[i]}") as im:
            if mode == "qp":
                im_crop = im.crop((0, 150, 1654, 2200))
            else:
                im_crop = im.crop((100, 200, 2300, 1500))
            im_crop.save(f"{work_dir}/currentPdfImages/{pages[i]}")


def take_screenshot(
    y1: int,
    y2: int,
    unique_filename: str,
    type: str,
    page: int,
    mode: str,
    work_dir: str = outputPath,
    merged: PIL.Image.Image | None = None,
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
    work_dir (str): The folder holding the pages and where the question is saved, in its questions subfolder (see make_work_dir).
    merged (PIL.Image.Image | None): For "long" questions, the in-memory merged image from merge_all_images to crop from
        instead of final/final.jpg.

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
        image_path = f"{work_dir}/final/final.jpg"
    else:
        image_path = f"{work_dir}/currentPdfImages/{page}"

    try:
        im = merged if (type == "long" and merged is not None) else PIL.Image.open(image_path)
        try:
            # Crop the region
            if mode == "qp":
                im_crop = im.crop((100, y1, 1600, y2))
            else:
                im_crop = im.crop((0, y1, 2300, y2))
        finally:
            if im is not merged:
                im.close()

        # Save to questions folder
        save_path = f"{work_dir}/questions/{unique_filename}.jpg"
        im_crop.save(save_path)

        print(f"Saved question {unique_filename}")

        return True
    except Exception as e:
        print(f"Error saving question {unique_filename}: {e}")
    return False


def _last_content_row(im: PIL.Image.Image) -> int:
    """Finds the lowest row containing content, using the same sampling as the original per-pixel loop:
    every 2nd row/column scanning up from the bottom, stopping at the first row where a pixel and its
    right neighbour are both non-white. Rows are checked in growing blocks with numpy so it stays fast
    without losing the early exit when content reaches the bottom of the image.
    """
    lowest, highest = im.height - 2, 2 + (im.height % 2)  # sampled rows: lowest, lowest-2, ..., highest
    first_x = 2 + (im.width % 2)  # sampled columns: first_x, first_x+2, ..., width-2
    bottom, block = lowest, 32
    while bottom >= highest:
        top = max(highest, bottom - block + 2)
        region = np.asarray(im.crop((0, top, im.width, bottom + 1)).convert("RGB"))[::2]
        nonwhite = (region != 255).any(axis=2)
        hits = (nonwhite[:, first_x:-1:2] & nonwhite[:, first_x + 1 :: 2]).any(axis=1)
        found = np.flatnonzero(hits)
        if found.size:
            return top + 2 * int(found[-1])
        bottom, block = top - 2, block * 2
    return highest


def clean_image(
    level_folder_name: str, subject: str, paper_number: str, image_name: str, mode: str
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
    clean_image_file(
        f"{BASE_PATH}/resources/images/{level_folder_name}/{subject}/{paper_number}/{image_name}",
        mode,
    )


def clean_image_file(image_path: str, mode: str) -> None:
    """Same as clean_image, but takes the path of the image to clean directly (e.g. a question still in a work_dir)."""
    im = PIL.Image.open(image_path)
    y = _last_content_row(im)
    if mode == "qp":
        cleaned_image = im.crop((0, 0, 1500, y + 10))
    else:
        cleaned_image = im.crop((0, 0, 2300, y + 10))
    cleaned_image.save(image_path)


def merge_all_images(
    mode: str, work_dir: str = outputPath, save: bool = True
) -> PIL.Image.Image:
    """Merges all the page images in the currentPdfImages directory into a single long image and saves it to the final folder as final.jpg.
     The images are merged vertically in the order of their page numbers (sorted by filename).
     This is used to create a single image of the entire question paper for easier cropping of long questions that may span multiple pages

     Args:
        mode (str): "qp" or "ms", which determines the width of the merged image.
        work_dir (str): The folder whose currentPdfImages subfolder holds the pages (see make_work_dir).
        save (bool): Whether to also save the merged image as final/final.jpg. Pass False when processing PDFs in parallel
            and hand the returned image to take_screenshot(merged=...) instead.

    Returns:
        PIL.Image.Image: The merged image.

    """
    pages = os.listdir(f"{work_dir}/currentPdfImages")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))

    # First pass to get total height
    total_height = 0
    for page_file in pages:
        with PIL.Image.open(f"{work_dir}/currentPdfImages/{page_file}") as im:
            total_height += im.height

    if mode == "qp":
        dst = PIL.Image.new("RGB", (1654, total_height), color="white")
    else:
        dst = PIL.Image.new("RGB", (2300, total_height), color="white")
    current_height = 0

    # Second pass to merge images
    for page_file in pages:
        image_path = f"{work_dir}/currentPdfImages/{page_file}"
        with PIL.Image.open(image_path) as im:
            dst.paste(im, (0, current_height))
            current_height += im.height

    if save:
        os.makedirs(f"{work_dir}/final", exist_ok=True)
        dst.save(f"{work_dir}/final/final.jpg")
    return dst


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


def cleanup() -> None:
    """Cleans up the output directories by deleting all files in the currentPdfImages, final and questions folders.
        This is used to reset the state before processing a new PDF to avoid any interference from previous runs.

    Args:        None: The function does not take any arguments, but it processes the files in the specified output directories.
    Returns:        None: The function does not return anything, but it deletes the files in the specified output directories to clean up the state for the next run.

    """
    dirs = [
        f"{outputPath}/currentPdfImages",
        f"{outputPath}/final",
        f"{outputPath}/questions",
    ]

    for d in dirs:
        if not os.path.isdir(d):
            continue
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


# Finding questions from a PDF's text layer instead of the YOLO detection server (see makep4/question_numbers.py).
# Question papers: question numbers are printed in the left margin at a fixed size, so they're found by looking for
# the numbers 1, 2, 3, ... in order at that position, with the number of "[Total: N]" markers as a cross-check.
# Mark schemes: each question starts at the first row of the table's Question column numbered with it
# ("2", "2(a)", "2(a)(i)", ...). Both use the same page handling as makep4-ai.py and p4_ms_maker_ai.py
# (makeImages -> strip_images -> merge_all_images -> take_screenshot -> clean_image_file).

TOTAL = re.compile(r"\[\s*Total\s*:?\s*\d+\+?\s*\]", re.I)
# Question numbers line up with the "© UCLES" footer (0.1-0.9pt to its right, the footer is usually 49.6pt from the
# left edge but some papers have a wider margin) and are 7-9.5pt tall (graph axis labels etc. are smaller)
DEFAULT_FOOTER_X = 49.6
NUMBER_X_FROM_FOOTER = (-1.5, 2.5)
NUMBER_HEIGHT_RANGE = (7, 9.5)
# How far left of the footer to look for text before a question number on its line. Papers from 2024 have a vertical
# "DO NOT WRITE IN THIS MARGIN" strip about 40pt left of the footer, which isn't part of the line
NUMBER_LINE_LOOKBACK = 25
# A question number at the top of a page is accepted further right, as a few pages are typeset indented
# (e.g. 0610 w20 42 Q3)
TOP_OF_PAGE_Y = (58, 70)
TOP_OF_PAGE_MAX_X = 120
# 9701 paper 3: the "Qualitative analysis" instructions above a question's number belong to that question
SECTION_HEADINGS = ["Qualitative analysis"]

# Must match how makeImages (pdf2image's default 200 DPI) and strip_images ("qp": y 150 to 2200) make the pages
SCALE = 200 / 72
STRIP_TOP, STRIP_BOTTOM = 150, 2200
# Space left above the question number, about the margin YOLO's boxes have above it
PADDING_PX = 14
# take_screenshot crops question images from x = 100
CROP_LEFT = 100
# get_question_texts reads from here down (in points), below most of the barcode 2024+ papers print at the top of
# each page, and stops above the copyright notice on the last page (found by position, as its text can come first)
TEXT_TOP = 59
COPYRIGHT_NOTICES = ["Permission to reproduce items", "To avoid the issue of disclosure"]
# ... and down to here, a little below the band strip_images keeps, as a question's "[Total: N]" is sometimes printed
# just below it (e.g. 0625 s24 32 Q5 at 793pt), but never into a "© UCLES" footer at the bottom of the page
TEXT_BOTTOM = 800
# The barcode's text (",\x01\x01\x01\x01\t\x01...,") and any other control characters
BARCODE_TEXT = re.compile(r",[\x00-\x1f]+,|[\x00-\x09\x0b\x0c\x0e-\x1f]")

# Part labels: letters start 63-76pt from the left edge (usually 71-73), roman numerals (right-aligned) 80-100pt, so "(i)" in the
# letter column is the letter after (h). Inline references like "... in (b)(i)." in the instructions start further right
PART_LABEL = re.compile(r"\(([a-z]{1,4})\)")
PART_LETTERS = set("abcdefghijk")
ROMAN_NUMERALS = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}
LETTER_X_RANGE = (63, 76)
ROMAN_X_RANGE = (80, 100)
# Margin around a part label's box
PART_PADDING_PX = 6
# Wider than any page, to read the whole line a label is on
KEY_LINE_WIDTH = 2000

# Mark schemes: question numbers like "1", "1(a)" or "10(b)(ii)" start the rows of the table's Question column.
# Must match how strip_images ("ms": y 200 to 1500) and split_mark_scheme in p4_ms_maker_ai.py stack the pages
MS_STRIP_TOP, MS_PAGE_HEIGHT = 200, 1300
# Question numbers start 0-20pt right of the "Question" header's left edge, the Answer
# column's text (including numbered marking points like "1 globular protein ;") starts 55pt or more right of it
MS_COLUMN_FROM_HEADER = (-10, 35)
# Used when a mark scheme has no "Question" header at all (in points from the left of the displayed page)
MS_DEFAULT_COLUMN = (50, 100)
# Some mark schemes start a new table (with its own header row) for each question. A question whose first row is
# directly under a header starts at the header instead, so the header isn't left at the bottom of the previous
# question's image (in points between the header's text and the row's text)
MS_HEADER_GAP = 40
# How close (in points) characters must be to count as one number ("10"), and how far left of the Question column
# to look for text that would mean a number isn't the first thing on its line
MS_DIGIT_GAP = 4
MS_LINE_LOOKBACK = 30



def _pdfium_locked(func):
    """Runs func while holding PDFIUM_LOCK (see there)."""

    @wraps(func)
    def locked(*args, **kwargs):
        with PDFIUM_LOCK:
            return func(*args, **kwargs)

    return locked


def _numbers(textpage, max_gap: float = 3) -> list:
    """Groups consecutive digits on the same line (at most max_gap points apart) into numbers, returning
    (text, [left, bottom, right, top], next) in PDF points (origin at the bottom left of the page), where next is the
    character after the number."""
    numbers, current, box = [], "", None
    for i in range(textpage.count_chars()):
        char = textpage.get_text_range(i, 1)
        left, bottom, right, top = textpage.get_charbox(i)
        if char.isdigit() and current and 0 <= left - box[2] < max_gap and abs(bottom - box[1]) < 2:
            current += char
            box = [box[0], bottom, right, top]
        else:
            if current:
                numbers.append((current, box, char))
            current, box = (char, [left, bottom, right, top]) if char.isdigit() else ("", None)
    if current:
        numbers.append((current, box, ""))
    return numbers


def _footer_x(textpage) -> float:
    """Returns how far the "© UCLES" footer is from the left edge of the page (DEFAULT_FOOTER_X when there's none)."""
    # The last page's copyright notice also mentions "(UCLES)", so only a match with the © two characters before it counts
    searcher = textpage.search("UCLES")
    while (match := searcher.get_next()) is not None:
        if match[0] >= 2 and textpage.get_text_range(match[0] - 2, 1) == "©":
            return textpage.get_charbox(match[0] - 2)[0]
    return DEFAULT_FOOTER_X


def _footer_top(textpage, page_height: float) -> float | None:
    """Returns how far the "© UCLES" footer is from the top of the page (None when there's none). Papers from 2024
    print it at the top of the page, older ones at the bottom."""
    searcher = textpage.search("UCLES")
    while (match := searcher.get_next()) is not None:
        if match[0] >= 2 and textpage.get_text_range(match[0] - 2, 1) == "©":
            return page_height - textpage.get_charbox(match[0] - 2)[3]
    return None


@_pdfium_locked
def find_question_starts(pdf_path: str) -> tuple[list, int]:
    """Finds the question numbers 1, 2, 3, ... in a question paper.

    Args:
    pdf_path (str): The path to the question paper.

    Returns:
        tuple[list, int]: [(page_index, y), ...] where y is how far the question starts from the top of the page
          in points, one per question in order, and the number of "[Total: N]" markers in the paper.
          The first page and pages left out by makeImages (see page_skip_reason) are never used.
    """
    document = pdfium.PdfDocument(pdf_path)
    starts, expected, totals = [], 1, 0
    try:
        for page_index in range(1, len(document)):
            page = document[page_index]
            textpage = page.get_textpage()
            text = textpage.get_text_range()
            totals += len(TOTAL.findall(text))
            if page_skip_reason(text):
                continue
            page_height = page.get_size()[1]

            headings = []
            for heading in SECTION_HEADINGS:
                searcher = textpage.search(heading, match_case=True)
                while (match := searcher.get_next()) is not None:
                    headings.append(page_height - textpage.get_charbox(match[0])[3])

            footer_x = _footer_x(textpage)

            previous_y = 0
            for number, (left, bottom, right, top), next_char in sorted(_numbers(textpage), key=lambda n: -n[1][3]):
                in_column = NUMBER_X_FROM_FOOTER[0] <= left - footer_x <= NUMBER_X_FROM_FOOTER[1]
                at_top_of_page = TOP_OF_PAGE_Y[0] <= page_height - top <= TOP_OF_PAGE_Y[1] and left <= TOP_OF_PAGE_MAX_X
                if not (in_column or at_top_of_page):
                    continue
                # Nothing before it on its line, so the "2" of "Step 2" or "Fig. 1.2" isn't taken for a question
                if textpage.get_text_bounded(max(0, footer_x - NUMBER_LINE_LOOKBACK), bottom + 1, left - 0.5, top - 1).strip():
                    continue
                # Numbered method steps in practical papers ("2. Label 3 test-tubes ...") are in the same column
                if next_char == ".":
                    continue
                if not (NUMBER_HEIGHT_RANGE[0] <= top - bottom <= NUMBER_HEIGHT_RANGE[1]):
                    continue
                if int(number) != expected:
                    continue
                y = page_height - top
                # Start at a section heading between the previous question on this page and this number
                above = [h for h in headings if previous_y <= h < y]
                starts.append((page_index, min(above) if above else y))
                previous_y = y
                expected += 1
    finally:
        document.close()
    return starts, totals


def _page_offsets(document) -> tuple[dict, int]:
    """Returns where each page kept by makeImages starts in the merged image of the stripped pages
    ({page_index: y}), and the merged image's height."""
    page_offsets, current_height = {}, 0
    for page_index in range(1, len(document)):
        page = document[page_index]
        if page_skip_reason(page.get_textpage().get_text_range()):
            continue
        page_offsets[page_index] = current_height
        rendered_height = round(page.get_size()[1] * SCALE)
        current_height += min(STRIP_BOTTOM, rendered_height) - STRIP_TOP
    return page_offsets, current_height


@_pdfium_locked
def get_text_coordinates(pdf_path: str) -> tuple[list, int]:
    """Where each question starts, as split_question_paper in makep4-ai.py crops them: the y coordinate of each
    question's start in the merged image of the stripped pages, followed by the merged image's height.

    Returns:
        tuple[list, int]: The coordinates, and the number of "[Total: N]" markers to check the question count against.
    """
    starts, totals = find_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        page_offsets, merged_height = _page_offsets(document)
    finally:
        document.close()

    coordinates = [
        page_offsets[page_index] + max(0, int(y * SCALE) - STRIP_TOP - PADDING_PX) for page_index, y in starts
    ]
    coordinates.append(merged_height)
    return coordinates, totals


@_pdfium_locked
def get_question_texts(pdf_path: str) -> list:
    """Reads each question's text from the region its image is cropped from (see get_text_coordinates): from its
    start to the next question's start (or the end of the paper), on the pages kept by makeImages, within the band
    strip_images keeps. Unlike splitting the paper's text at its "[Total: N]" markers, this also works for questions
    without a marker (e.g. 9701 s21 43 Q9, the planning question 1 of 9702 paper 5).

    Returns:
        list: The text of each question, in question order (the same order as find_question_starts).
    """
    starts, _ = find_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        kept_pages = [
            page_index
            for page_index in range(1, len(document))
            if not page_skip_reason(document[page_index].get_textpage().get_text_range())
        ]
        band_top, band_bottom = max(STRIP_TOP / SCALE, TEXT_TOP), TEXT_BOTTOM
        padding = PADDING_PX / SCALE
        # Where each question starts and the next one (or the end of the last kept page) begins, as (page, y)
        boundaries = [(page_index, max(band_top, y - padding)) for page_index, y in starts]
        if kept_pages:
            boundaries.append((kept_pages[-1], band_bottom))

        texts = []
        for (start_page, start_y), (end_page, end_y) in zip(boundaries, boundaries[1:]):
            pieces = []
            for page_index in kept_pages:
                if not start_page <= page_index <= end_page:
                    continue
                page = document[page_index]
                textpage = page.get_textpage()
                page_width, page_height = page.get_size()
                top = start_y if page_index == start_page else band_top
                bottom = min(end_y if page_index == end_page else band_bottom, page_height)
                footer = _footer_top(textpage, page_height)
                # A few points above it, as the "[Turn over" on the same line is printed a little higher
                if footer is not None and footer > page_height / 2:
                    bottom = min(bottom, footer - 4)
                for phrase in COPYRIGHT_NOTICES:
                    notice = textpage.search(phrase).get_next()
                    if notice:
                        bottom = min(bottom, page_height - textpage.get_charbox(notice[0])[3] - 1)
                if bottom <= top:
                    continue
                # From just left of the question numbers, leaving out the "DO NOT WRITE IN THIS MARGIN" strips 2024+
                # papers print down the outer edge of each page (on the left or the right)
                margin = max(0, _footer_x(textpage) - NUMBER_LINE_LOOKBACK)
                # get_text_bounded takes PDF coordinates, with y measured up from the bottom of the page
                pieces.append(
                    textpage.get_text_bounded(margin, page_height - bottom, page_width - margin, page_height - top)
                )
            texts.append(BARCODE_TEXT.sub("", "\n".join(pieces)))
    finally:
        document.close()
    return texts


def _part_labels(textpage, page_height: float) -> list:
    """Finds the part labels on a page: letters like "(a)" and roman numerals like "(ii)" at the left margin.
    "(b)(i)" gives two labels. Returns (top, bottom, left, right, text) for each, with y from the top of the page
    in points."""
    labels = []
    # Papers with a wider margin have their part columns shifted by the same amount as the footer
    shift = _footer_x(textpage) - DEFAULT_FOOTER_X
    # Index of the last character of the previous label kept, so the "(i)" of "(b)(i)" is kept too
    previous_label_end = None
    for i in range(textpage.count_chars()):
        if textpage.get_text_range(i, 1) != "(":
            continue
        match = PART_LABEL.match(textpage.get_text_range(i, 7))
        if not match:
            continue
        # A label starts its line, or follows another label. This leaves out references like "3(b)(i)" or "in (b)(i)."
        before = textpage.get_text_range(i - 1, 1) if i > 0 else ""
        if before.strip() and previous_label_end != i - 1:
            continue
        # Leaves out references that wrapped onto a new line, like "(g) and (h)."
        following = textpage.get_text_range(i + len(match.group(0)), 12).strip(" \x07")
        if re.match(r"(and|or)\b|[,.;:]", following):
            continue
        label = match.group(1)
        left, bottom, _, top = textpage.get_charbox(i)
        # Leaves out the rows of dichotomous keys, like "(a) beak is longer than the head ... go to 2"
        if "go to" in textpage.get_text_bounded(0, bottom + 1, KEY_LINE_WIDTH, top - 1):
            continue
        in_letter_column = LETTER_X_RANGE[0] <= left - shift <= LETTER_X_RANGE[1]
        in_roman_column = ROMAN_X_RANGE[0] <= left - shift <= ROMAN_X_RANGE[1]
        # Roman numerals are occasionally printed in the letter column too (e.g. 9701 w20 34 Q2 (c)(v))
        if (label in PART_LETTERS and in_letter_column) or (
            label in ROMAN_NUMERALS and (in_roman_column or in_letter_column)
        ):
            end = i + len(match.group(0)) - 1
            right = textpage.get_charbox(end)[2]
            labels.append((page_height - top, page_height - bottom, left, right, match.group(0)))
            previous_label_end = end
    return labels


@_pdfium_locked
def find_question_parts(pdf_path: str) -> list:
    """Finds the part labels of every question, in the format makep4-ai.py stores in
    questionParts: [{"coordinates": [x1, y1, x2, y2], "text": "(a)"}, ...] in pixels of the question image
    (as saved by split_question_paper_from_text, before clean_image_file trims its bottom).

    Returns:
        list: One list of parts per question, in question order.
    """
    coordinates, _ = get_text_coordinates(pdf_path)
    question_parts = [[] for _ in range(len(coordinates) - 1)]
    document = pdfium.PdfDocument(pdf_path)
    try:
        page_offsets, _ = _page_offsets(document)
        for page_index, offset in page_offsets.items():
            page = document[page_index]
            for top, bottom, left, right, text in _part_labels(page.get_textpage(), page.get_size()[1]):
                y1 = offset + int(top * SCALE) - STRIP_TOP - PART_PADDING_PX
                y2 = offset + int(bottom * SCALE) - STRIP_TOP + PART_PADDING_PX
                # The question whose region the label starts in
                question = next((i for i in range(len(question_parts)) if coordinates[i] <= y1 < coordinates[i + 1]), None)
                if question is None:
                    continue
                start = coordinates[question]
                question_parts[question].append({
                    "coordinates": [
                        int(left * SCALE) - CROP_LEFT - PART_PADDING_PX,
                        y1 - start,
                        int(right * SCALE) - CROP_LEFT + PART_PADDING_PX,
                        y2 - start,
                    ],
                    "text": text,
                })
    finally:
        document.close()
    for parts in question_parts:
        parts.sort(key=lambda part: (part["coordinates"][1] // 10, part["coordinates"][0]))
    return question_parts


def split_question_paper_from_text(pdf_path: str, out_dir: str) -> list:
    """Splits a question paper into one cleaned image per question, saved as <pdf name>_q<number>.jpg in out_dir,
    with each question's parts (see find_question_parts) saved to <pdf name>_parts.json, keyed by image name.

    Returns:
        list: The paths of the saved question images, in question order.
    """
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    coordinates, totals = get_text_coordinates(pdf_path)
    question_count = len(coordinates) - 1
    if question_count == 0:
        print(f"[WARN] {pdf_name}: no question numbers found in the text layer")
        return []
    if question_count != totals:
        print(f"[WARN] {pdf_name}: {question_count} question numbers found, but {totals} [Total] markers")

    work_dir = make_work_dir(f"text-{pdf_name}")
    makeImages(pdf_path, work_dir)
    strip_images(mode="qp", work_dir=work_dir)
    merged = merge_all_images(mode="qp", work_dir=work_dir, save=False)

    question_parts = find_question_parts(pdf_path)

    os.makedirs(out_dir, exist_ok=True)
    saved = []
    parts_by_image = {}
    for i in range(question_count):
        local_filename = f"q{i + 1}"
        if not take_screenshot(
            coordinates[i], coordinates[i + 1], local_filename, "long", 0, mode="qp", work_dir=work_dir, merged=merged
        ):
            continue
        image_path = f"{work_dir}/questions/{local_filename}.jpg"
        clean_image_file(image_path, mode="qp")
        destination = f"{out_dir}/{pdf_name}_q{i + 1}.jpg"
        shutil.copy(image_path, destination)
        saved.append(destination)
        parts_by_image[os.path.basename(destination)] = question_parts[i]
    shutil.rmtree(work_dir, ignore_errors=True)
    with open(f"{out_dir}/{pdf_name}_parts.json", "w", encoding="utf-8") as f:
        json.dump(parts_by_image, f, indent=2)
    print(f"{pdf_name}: saved {len(saved)} questions to {out_dir}")
    return saved


def _displayed_box(page, box: tuple) -> tuple:
    """Converts a character box from get_charbox (PDF points, before the page's rotation) to (left, top, right, bottom)
    in points from the top left of the page as displayed, which is how pdf2image renders it. Mark scheme pages
    are often landscape pages stored rotated by 90 degrees."""
    left, bottom, right, top = box
    media_left, media_bottom, media_right, media_top = page.get_mediabox()
    rotation = page.get_rotation()
    if rotation == 90:
        return bottom - media_bottom, left - media_left, top - media_bottom, right - media_left
    if rotation == 180:
        return media_right - right, bottom - media_bottom, media_right - left, top - media_bottom
    if rotation == 270:
        return media_top - top, media_right - right, media_top - bottom, media_right - left
    return left - media_left, media_top - top, right - media_left, media_top - bottom


def _ms_question_column(page, textpage) -> tuple | None:
    """Returns the (left, right) range of the table's Question column on a mark scheme page from its "Question"
    header, or None when the page has no header."""
    match = textpage.search("Question", match_case=True, match_whole_word=True).get_next()
    if not match:
        return None
    header_left = _displayed_box(page, textpage.get_charbox(match[0]))[0]
    return header_left + MS_COLUMN_FROM_HEADER[0], header_left + MS_COLUMN_FROM_HEADER[1]


def _ms_column_numbers(page, textpage, column: tuple) -> list:
    """Finds the numbers that start a line of a mark scheme page's Question column: "2", "2(a)", "2(a)(i)", ...
    Lines are found from the characters' positions rather than the text's line breaks, as some pages store their
    characters out of reading order (e.g. 0625 s17 42 page 9).

    Returns:
        list: (top, number, bare) for each, where top is in points from the top of the displayed page and bare is
          True when the number isn't followed by a part label like "(a)".
    """
    characters = []
    for i in range(textpage.count_chars()):
        char = textpage.get_text_range(i, 1)
        if char.strip():
            characters.append((char, _displayed_box(page, textpage.get_charbox(i))))

    def same_line(a: tuple, b: tuple) -> bool:
        # Overlapping vertically by at least half the shorter character, so subscripts like the "2" of "H2" count
        overlap = min(a[3], b[3]) - max(a[1], b[1])
        return overlap >= 0.5 * min(a[3] - a[1], b[3] - b[1])

    numbers = []
    for char, box in characters:
        left, top, _, _ = box
        if not char.isdigit() or not column[0] <= left < column[1]:
            continue
        line = sorted(
            (other for other in characters if other[1] is not box and same_line(other[1], box)), key=lambda c: c[1][0]
        )
        # Nothing before it on its line in or just left of the column, so it starts the line (and isn't the "0" of "10")
        if any(column[0] - MS_LINE_LOOKBACK <= other[1][2] <= left + 0.5 for other in line):
            continue
        number, right = char, box[2]
        after = [other for other in line if other[1][0] >= right - 0.5]
        while after and after[0][0].isdigit() and after[0][1][0] - right < MS_DIGIT_GAP:
            number, right = number + after[0][0], after[0][1][2]
            after = after[1:]
        if len(number) > 2:
            continue
        numbers.append((top, int(number), not after or after[0][0] != "("))
    return numbers


def _ms_header_tops(page, textpage) -> list:
    """Returns how far each "Question" table header on a mark scheme page is from the top of the displayed page."""
    tops = []
    searcher = textpage.search("Question", match_case=True, match_whole_word=True)
    while (match := searcher.get_next()) is not None:
        tops.append(_displayed_box(page, textpage.get_charbox(match[0]))[1])
    return tops


@_pdfium_locked
def find_ms_question_starts(pdf_path: str) -> list:
    """Finds where each question's rows start in a mark scheme: the first row of the Question column whose number
    is the next question (1, 2, 3, ...), whether it's written "2", "2(a)" or "2(a)(i)".

    Args:
    pdf_path (str): The path to the mark scheme.

    Returns:
        list: [(page_index, y), ...] where y is how far the question's first row starts from the top of the displayed
          page in points (or where the page's table header starts, when the row is right under it), one per question
          in order. The first page and pages left out by makeImages
          (see page_skip_reason) are never used.
    """
    document = pdfium.PdfDocument(pdf_path)
    # Bare numbers (see _ms_column_numbers) seen since the last question's first row
    starts, expected, bare_since_start = [], 1, set()
    try:
        pages = [
            (page_index, document[page_index], document[page_index].get_textpage())
            for page_index in range(1, len(document))
        ]
        pages = [(page_index, page, textpage) for page_index, page, textpage in pages
                 if not page_skip_reason(textpage.get_text_range())]
        columns = [_ms_question_column(page, textpage) for _, page, textpage in pages]
        # Pages without a header (a table continuing from the previous page) use the last header's column, or the
        # first one in the mark scheme when no header came before them
        column = next((c for c in columns if c), MS_DEFAULT_COLUMN)
        for (page_index, page, textpage), page_column in zip(pages, columns):
            column = page_column or column

            header_tops = _ms_header_tops(page, textpage)
            for top, number, bare in sorted(_ms_column_numbers(page, textpage, column)):
                # Numbered rows of a table inside an answer ("1 KMnO4 ...", "2 AgNO3 ...", ...) look like questions
                # without parts, so a bare number is part of such a list when every bare number from 1 up to it
                # already came after the current question's first row. A lone repeated heading row ("3 Tests on
                # solid O") isn't a list
                in_list = bare and expected > 1 and set(range(1, expected)) <= bare_since_start
                if number == expected and not in_list:
                    header_above = [header for header in header_tops if 0 < top - header < MS_HEADER_GAP]
                    starts.append((page_index, header_above[0] if header_above else top))
                    expected += 1
                    bare_since_start = set()
                elif bare:
                    bare_since_start.add(number)
    finally:
        document.close()
    return starts


@_pdfium_locked
def get_ms_text_coordinates(pdf_path: str) -> list:
    """The y coordinate of each question's start in the stacked image of the stripped mark scheme pages that
    split_mark_scheme in p4_ms_maker_ai.py crops from (page j starts at j * 1300), followed by its height.

    Returns:
        list: The coordinates, one per question in order, then the stacked image's height.
    """
    starts = find_ms_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        kept_pages = [
            page_index
            for page_index in range(1, len(document))
            if not page_skip_reason(document[page_index].get_textpage().get_text_range())
        ]
    finally:
        document.close()
    page_position = {page_index: j for j, page_index in enumerate(kept_pages)}

    coordinates = [
        page_position[page_index] * MS_PAGE_HEIGHT + max(0, int(y * SCALE) - MS_STRIP_TOP - PADDING_PX)
        for page_index, y in starts
    ]
    coordinates.append(len(kept_pages) * MS_PAGE_HEIGHT)
    return coordinates


def split_mark_scheme_from_text(pdf_path: str, out_dir: str) -> list:
    """Splits a mark scheme into one cleaned image per question, saved as <pdf name>_q<number>.jpg in out_dir, with the
    same page handling as split_mark_scheme in p4_ms_maker_ai.py.

    Returns:
        list: The paths of the saved mark scheme images, in question order.
    """
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    coordinates = get_ms_text_coordinates(pdf_path)
    question_count = len(coordinates) - 1
    if question_count == 0:
        print(f"[WARN] {pdf_name}: no question numbers found in the text layer")
        return []

    work_dir = make_work_dir(f"text-{pdf_name}")
    makeImages(pdf_path, work_dir)
    strip_images(mode="ms", work_dir=work_dir)
    merged = merge_all_images(mode="ms", work_dir=work_dir, save=False)

    os.makedirs(out_dir, exist_ok=True)
    saved = []
    for i in range(question_count):
        local_filename = f"q{i + 1}"
        if not take_screenshot(
            coordinates[i], coordinates[i + 1], local_filename, "long", "", mode="ms", work_dir=work_dir, merged=merged
        ):
            continue
        image_path = f"{work_dir}/questions/{local_filename}.jpg"
        clean_image_file(image_path, mode="ms")
        destination = f"{out_dir}/{pdf_name}_q{i + 1}.jpg"
        shutil.copy(image_path, destination)
        saved.append(destination)
    shutil.rmtree(work_dir, ignore_errors=True)
    print(f"{pdf_name}: saved {len(saved)} mark schemes to {out_dir}")
    return saved


# MCQ question papers: like the long question papers, each question number starts a line in the left margin, in line
# with the "© UCLES" footer, but several questions share a page and each is cropped from its own page (see
# makep1Final.py), not from the merged pages
MCQ_NUMBER_X_FROM_FOOTER = (-8, 3)
# 2017 papers print the numbers larger (11.2pt) and their digits further apart, e.g. 0620 s17 11
MCQ_NUMBER_HEIGHT_RANGE = (7, 12)
MCQ_DIGIT_GAP = 4.5
# makep1Final.py crops a page's last question down to this y in the stripped page
MCQ_PAGE_END = 2050
# A question that was withdrawn after the exam is replaced by a notice like "Due to an issue with Question 22, the
# question has been removed from the question paper." (e.g. 0455 w21 11), so its number never appears
MCQ_REMOVED = re.compile(r"Question\s+(\d+)\b[^.]{0,60}\bremoved", re.I)


@_pdfium_locked
def find_mcq_question_starts(pdf_path: str) -> list:
    """Finds the question numbers 1, 2, 3, ... in an MCQ question paper.

    Args:
    pdf_path (str): The path to the question paper.

    Returns:
        list: [(question_number, page_index, y), ...] where y is how far the question starts from the top of the page in
          points, in question order. Questions removed from the paper (see MCQ_REMOVED) are left out, so the numbers can
          skip one. The first page and pages left out by makeImages (see page_skip_reason) are never used.
    """
    document = pdfium.PdfDocument(pdf_path)
    starts, expected = [], 1
    try:
        removed = set()
        for page_index in range(1, len(document)):
            removed |= {int(n) for n in MCQ_REMOVED.findall(document[page_index].get_textpage().get_text_range())}

        for page_index in range(1, len(document)):
            page = document[page_index]
            textpage = page.get_textpage()
            if page_skip_reason(textpage.get_text_range()):
                continue
            page_height = page.get_size()[1]
            footer_x = _footer_x(textpage)
            numbers = sorted(_numbers(textpage, MCQ_DIGIT_GAP), key=lambda n: -n[1][3])
            for number, (left, bottom, right, top), next_char in numbers:
                while expected in removed:
                    expected += 1
                in_column = MCQ_NUMBER_X_FROM_FOOTER[0] <= left - footer_x <= MCQ_NUMBER_X_FROM_FOOTER[1]
                # Same as the long papers: a few pages are typeset indented (e.g. 0625 w19 11 Q33)
                at_top_of_page = TOP_OF_PAGE_Y[0] <= page_height - top <= TOP_OF_PAGE_Y[1] and left <= TOP_OF_PAGE_MAX_X
                if not (in_column or at_top_of_page):
                    continue
                # Nothing before it on its line, so the "2" of "Fig. 1.2" isn't taken for a question
                line_start = max(0, footer_x - NUMBER_LINE_LOOKBACK)
                if textpage.get_text_bounded(line_start, bottom + 1, left - 0.5, top - 1).strip():
                    continue
                # Numbered statements inside a question ("2. ...")
                if next_char == ".":
                    continue
                if not MCQ_NUMBER_HEIGHT_RANGE[0] <= top - bottom <= MCQ_NUMBER_HEIGHT_RANGE[1]:
                    continue
                if int(number) != expected:
                    continue
                starts.append((expected, page_index, page_height - top))
                expected += 1
    finally:
        document.close()
    return starts


@_pdfium_locked
def get_mcq_text_coordinates(pdf_path: str) -> dict:
    """Where each question starts in the stripped page image it's on, as makep1Final.py crops them.

    Returns:
        dict: {page image number (as named by makeImages, 1.jpg, 2.jpg, ...): [(question_number, y), ...]}, each page's
          questions in order, with y in pixels of the stripped page.
    """
    starts = find_mcq_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        kept_pages = [
            page_index
            for page_index in range(1, len(document))
            if not page_skip_reason(document[page_index].get_textpage().get_text_range())
        ]
    finally:
        document.close()
    image_number = {page_index: j + 1 for j, page_index in enumerate(kept_pages)}

    coordinates = {}
    for question_number, page_index, y in starts:
        coordinates.setdefault(image_number[page_index], []).append(
            (question_number, max(0, int(y * SCALE) - STRIP_TOP - PADDING_PX))
        )
    return coordinates


def split_mcq_paper_from_text(pdf_path: str, out_dir: str) -> list:
    """Splits an MCQ question paper into one cleaned image per question, saved as <pdf name>_q<number>.jpg in out_dir,
    with the same page handling as makep1Final.py (each question is cropped from its own stripped page, down to the next
    question or MCQ_PAGE_END).

    Returns:
        list: The paths of the saved question images, in question order.
    """
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    coordinates = get_mcq_text_coordinates(pdf_path)
    if not coordinates:
        print(f"[WARN] {pdf_name}: no question numbers found in the text layer")
        return []

    work_dir = make_work_dir(f"text-{pdf_name}")
    makeImages(pdf_path, work_dir)
    strip_images(mode="qp", work_dir=work_dir)

    os.makedirs(out_dir, exist_ok=True)
    saved = []
    for page_number, questions in sorted(coordinates.items()):
        for i, (question_number, y1) in enumerate(questions):
            y2 = questions[i + 1][1] if i + 1 < len(questions) else MCQ_PAGE_END
            local_filename = f"q{question_number}"
            if not take_screenshot(y1, y2, local_filename, "mcq", f"{page_number}.jpg", mode="qp", work_dir=work_dir):
                continue
            image_path = f"{work_dir}/questions/{local_filename}.jpg"
            clean_image_file(image_path, mode="qp")
            destination = f"{out_dir}/{pdf_name}_q{question_number}.jpg"
            shutil.copy(image_path, destination)
            saved.append(destination)
    shutil.rmtree(work_dir, ignore_errors=True)
    print(f"{pdf_name}: saved {len(saved)} questions to {out_dir}")
    return saved
