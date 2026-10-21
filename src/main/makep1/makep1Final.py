# Need to figure out how to skip pages with formula sheets and add clean_images()

import os
import shutil
import json
import sys
from concurrent.futures import ThreadPoolExecutor

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)
definitionsPath = f"{BASE_PATH}/main/definitions.json"
outputPath = f"{BASE_PATH}/resources/images/test_images"

from main.utils import (
    process_image,
    select_files,
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
    MCQ_PAGE_END,
    PDF_WORKERS,
)

with open(definitionsPath, "r") as db:
    definitionsData = json.load(db)


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
    question_count = sum(len(questions) for questions in coordinates.values())
    # Questions removed from the paper are left out of both, so the answers line up with the questions in order
    if question_count != len(answers):
        print(f"[WARN] {current_file}: {question_count} questions found, but {len(answers)} answers in the mark scheme")
    answer_index = 0
    for page_number, page_questions in sorted(coordinates.items()):
        for j, (question_number, y1) in enumerate(page_questions):
            # A question runs to the next one on its page, the page's last question to MCQ_PAGE_END
            y2 = page_questions[j + 1][1] if j + 1 < len(page_questions) else MCQ_PAGE_END
            answer = answers[answer_index] if answer_index < len(answers) else None
            answer_index += 1
            image_file_name = f"{subject}_p{paper_number}_{question_number + (currentFileIndex * num_of_questions)}"
            taken = take_screenshot(
                y1, y2, image_file_name, "mcq", f"{page_number}.jpg", mode="qp", work_dir=work_dir
            )
            if not taken:
                continue

            question_text = (
                process_image(f"{work_dir}/questions/{image_file_name}.jpg")
                .lower()
                .strip()
            )
            formatted_text = formatText(question_text)

            level, chapter_num = get_level_and_chapter(
                formatted_text, paper_number, paperType, currentDefintionsData
            )

            os.makedirs(
                f"{BASE_PATH}/resources/images/{paperType}/{subject}/mcq",
                exist_ok=True,
            )

            shutil.copy(
                f"{work_dir}/questions/{image_file_name}.jpg",
                f"{BASE_PATH}/resources/images/{paperType}/{subject}/mcq/{image_file_name}.jpg",
            )

            clean_image(paperType, subject, "mcq", f"{image_file_name}.jpg", mode="qp")

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


files = select_files()
questionObjects = []

# PDFs are processed in parallel, results are collected in the order the files were selected
with ThreadPoolExecutor(max_workers=PDF_WORKERS) as pool:
    for file_objects in pool.map(process_pdf, range(len(files)), files):
        questionObjects.extend(file_objects)
cleanup()


with open(f"{BASE_PATH}/resources/json/test_images.json", "w") as f:
    f.write("[\n")
    for obj in questionObjects:
        f.write(json.dumps(obj) + ",\n")
    f.write("]")
