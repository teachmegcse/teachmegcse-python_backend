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
    get_dimensions_from_api,
    cleanup,
    extract_answers_from_pdf,
    extract_paper_number,
    make_work_dir,
    start_detection_server,
    wait_for_detection_server,
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
    pages = os.listdir(f"{work_dir}/currentPdfImages")
    answers = extract_answers_from_pdf(paperCode, current_file)
    current_question_num = 1
    for k in range(len(pages)):
        y_coordinates = get_dimensions_from_api(
            f"{work_dir}/currentPdfImages/{k + 1}.jpg",
            mode="mcq"
        )
        # Filter boxes where x1 < 250 and extract their y2 (i.e. box[1])
        raw_y2_list = sorted(box[1] for box in y_coordinates if box[0] < 160)
        threshold = 10  # adjust as needed depending on your use case
        y2_list = []
        for y2 in raw_y2_list:
            if not y2_list or abs(y2 - y2_list[-1]) > threshold:
                y2_list.append(y2)
        if len(y2_list):
            for j in range(len(y2_list)):
                image_file_name = f"{subject}_p{paper_number}_{current_question_num + (currentFileIndex * num_of_questions)}"

                if j == len(y2_list) - 1:
                    taken = take_screenshot(
                        y2_list[j], 2050, image_file_name, "mcq", f"{k + 1}.jpg", mode="qp", work_dir=work_dir
                    )
                else:
                    taken = take_screenshot(
                        y2_list[j],
                        y2_list[j + 1],
                        image_file_name,
                        "mcq",
                        f"{k + 1}.jpg",
                        mode="qp",
                        work_dir=work_dir,
                    )
                if not taken:
                    current_question_num -= 1
                if os.path.exists(f"{work_dir}/questions/{image_file_name}.jpg"):
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
                        "Answer": answers[current_question_num - 1],
                        "pdfName": current_file,
                        "questionText": question_text,
                        "Chapter": chapter_num,
                        "Level": level,
                        "paperNumber": paper_number,
                        "Subject": subject,
                        "year": "20" + current_file.split("_")[1][1:3],
                    }
                    questionObjects.append(answer_object)
                current_question_num += 1

    print(f"Finished processing {file_path}...")
    shutil.rmtree(work_dir, ignore_errors=True)
    return questionObjects


start_detection_server()
files = select_files()
wait_for_detection_server()
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
