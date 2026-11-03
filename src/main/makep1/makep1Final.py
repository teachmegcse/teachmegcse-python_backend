# Need to figure out how to skip pages with formula sheets and add clean_images()

import os
import shutil
import json
import math
import re
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)
definitionsPath = f"{BASE_PATH}/main/definitions.json"
outputPath = f"{BASE_PATH}/resources/images/test_images"

from main.utils import (
    select_files,
    DEFAULT_FROM_YEAR,
    makeImages,
    get_level_and_chapter,
    clean_image,
    formatText,
    strip_images,
    take_screenshot,
    cleanup,
    extract_answers_from_pdf,
    extract_paper_number,
    make_work_dir,
    get_mcq_text_coordinates,
    get_mcq_question_texts,
    get_mcq_page_ends,
    load_json_db,
    MCQ_PAGE_END,
    PDF_WORKERS,
)

with open(definitionsPath, "r") as db:
    definitionsData = json.load(db)


def next_file_index(codes: set, db_paths: dict) -> int:
    """Returns the file index to continue from (filenames are {subject}_p{paper}_{question + index * questions per
    paper}.jpg), so a new run never reuses (and overwrites) the image of a question already in one of the DBs."""
    index = 0
    for code in codes:
        highest = 0
        for record in load_json_db(db_paths[code]):
            match = re.search(r"_(\d+)\.jpg$", record.get("questionName", ""))
            if match:
                highest = max(highest, int(match.group(1)))
        index = max(index, math.ceil(highest / definitionsData[code]["mcqNumberOfQuestions"]))
    return index


def process_pdf(currentFileIndex: int, file_path: str) -> list:
    """Splits one MCQ question paper into question images and returns its question objects.
    Each PDF works in its own work_dir, so several can run at the same time."""
    current_file = file_path[-18:]
    paperCode = current_file.split("_")[0]  # like 0620

    currentDefintionsData = definitionsData[paperCode]
    subject = currentDefintionsData["subjectName"]
    num_of_questions = currentDefintionsData["mcqNumberOfQuestions"]
    mcqPapers = currentDefintionsData["mcqPapers"]

    if current_file[0] == "0":
        paperType = "IGCSE"
    else:
        paperType = "A-level"

    # Extract paper number from filename
    paper_number = extract_paper_number(current_file)

    if paper_number not in mcqPapers:
        print(f"Paper number {paper_number} not in mcqPapers list, skipping file.")
        return []

    work_dir = make_work_dir(current_file.replace(".pdf", ""))
    questionObjects = []

    makeImages(file_path, work_dir)

    strip_images(mode="qp", work_dir=work_dir)
    answers = extract_answers_from_pdf(paperCode, current_file)
    # Where each question starts on its page, read from the PDF's text layer: {page image number: [(question number, y)]}
    coordinates = get_mcq_text_coordinates(file_path)
    # Each question's text, read from the same region of the PDF's text layer its image is cropped from
    question_texts = get_mcq_question_texts(file_path)
    page_ends = get_mcq_page_ends(file_path)
    if len(answers) != num_of_questions:
        print(f"[WARN] {current_file}: {len(answers)} rows in the mark scheme, expected {num_of_questions}")
    for page_number, page_questions in sorted(coordinates.items()):
        for j, (question_number, y1) in enumerate(page_questions):
            # A question runs to the next one on its page, the page's last question to the page's end (above its
            # footer and copyright notice, see get_mcq_page_ends)
            y2 = page_questions[j + 1][1] if j + 1 < len(page_questions) else page_ends.get(page_number, MCQ_PAGE_END)
            answer = answers[question_number - 1] if question_number <= len(answers) else None
            # Discounted or removed in the mark scheme, so it has no correct answer
            if answer is None:
                print(f"[WARN] {current_file}: question {question_number} has no answer in the mark scheme, left out")
                continue
            image_file_name = f"{subject}_p{paper_number}_{question_number + (currentFileIndex * num_of_questions)}"
            taken = take_screenshot(
                y1, y2, image_file_name, "mcq", f"{page_number}.jpg", mode="qp", work_dir=work_dir
            )
            if not taken:
                continue

            question_text = question_texts.get(question_number, "").lower().strip()
            formatted_text = formatText(question_text)

            level, chapter_num = get_level_and_chapter(
                formatted_text, paper_number, paperType, currentDefintionsData
            )

            # classified/api.py and the website read MCQ images from p<paper number>
            paper_folder = f"p{paper_number}"
            os.makedirs(
                f"{BASE_PATH}/resources/images/{paperType}/{subject}/{paper_folder}",
                exist_ok=True,
            )

            shutil.copy(
                f"{work_dir}/questions/{image_file_name}.jpg",
                f"{BASE_PATH}/resources/images/{paperType}/{subject}/{paper_folder}/{image_file_name}.jpg",
            )

            clean_image(paperType, subject, paper_folder, f"{image_file_name}.jpg", mode="qp")

            answer_object = {
                "questionName": f"{image_file_name}.jpg",
                "Answer": answer,
                "pdfName": current_file,
                "questionText": question_text,
                "Chapter": chapter_num,
                "Level": level,
                "paperNumber": paper_number,
                "Subject": subject,
                "year": "20" + current_file.split("_")[1][1:3],
            }
            questionObjects.append(answer_object)

    print(f"Finished processing {file_path}...")
    shutil.rmtree(work_dir, ignore_errors=True)
    return questionObjects


parser = argparse.ArgumentParser(description="Split MCQ question papers into one image per question.")
parser.add_argument("--folder", help="Folder of PDFs to process instead of selecting them in the file dialog")
parser.add_argument(
    "--from-year",
    type=int,
    default=DEFAULT_FROM_YEAR,
    help=f"Only process a folder's papers from this year onwards (default: {DEFAULT_FROM_YEAR})",
)
args = parser.parse_args()

# The answers are read from each paper's mark scheme, so mark schemes (and inserts) in a folder aren't processed
files = [
    file
    for file in select_files(args.folder, from_year=args.from_year, paper_types=("qp",))
    if "_qp_" in os.path.basename(file)
]
codes = {os.path.basename(file).split("_")[0] for file in files}
db_paths = {code: f"{BASE_PATH}/resources/json/{definitionsData[code]['mcq_db_path']}" for code in codes}
first_file_index = next_file_index(codes, db_paths)

# PDFs are processed in parallel, results are saved in the order the files were selected, after every paper so a
# crash loses at most one paper
with ThreadPoolExecutor(max_workers=PDF_WORKERS) as pool:
    file_indexes = range(first_file_index, first_file_index + len(files))
    for file_path, file_objects in zip(files, pool.map(process_pdf, file_indexes, files)):
        if file_objects:
            db_path = db_paths[os.path.basename(file_path).split("_")[0]]
            db_records = load_json_db(db_path)
            db_records.extend(file_objects)
            with open(db_path, "w") as f:
                json.dump(db_records, f, indent=1)
cleanup()
