# Need to figure out how to skip pages with formula sheets and add clean_images()

import os
import shutil
import json
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)
definitionsPath = f"{BASE_PATH}/main/definitions.json"
outputPath = f"{BASE_PATH}/resources/images/test_images"

from main.utils import (
    process_image, select_files, makeImages, get_level_and_chapter, clean_images,
    formatText, strip_images, take_screenshot, get_dimensions_from_api, cleanup,
    extract_answers_from_pdf, extract_paper_number
)

with open(definitionsPath, "r") as db:
    definitionsData = json.load(db)

files = select_files()
questionObjects = []

for currentFileIndex in range(len(files)):
    current_file = files[currentFileIndex][-18:]
    paperCode = current_file.split("_")[0] # like 0620
    currentDefintionsData = definitionsData[paperCode]

    currentDefintionsData = definitionsData[paperCode]
    subject = currentDefintionsData["subjectName"]
    mcq_db_path = currentDefintionsData["mcq_db_path"]
    db_path = f"{BASE_PATH}/resources/json/{mcq_db_path}"
    num_of_questions = currentDefintionsData["mcqNumberOfQuestions"]

    if current_file[0] == '0':
        paperType = 'IGCSE'
    else:
        paperType = 'A-level'

    # Extract paper number from filename
    paper_number = extract_paper_number(current_file)

    makeImages(files[currentFileIndex])

    strip_images(mode='qp')
    pages = os.listdir(f"{outputPath}/currentPdfImages")
    answers = extract_answers_from_pdf(paperCode, current_file)
    current_question_num = 1
    for k in range(len(pages)):
        y_coordinates = get_dimensions_from_api(f"{outputPath}/currentPdfImages/{k + 1}.jpg")
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
                    take_screenshot(y2_list[j], 2050, image_file_name, 'mcq', f"{k + 1}.jpg")
                else:
                    take_screenshot(y2_list[j], y2_list[j + 1], image_file_name, 'mcq', f"{k + 1}.jpg")
                
                if os.path.exists(f"{outputPath}/questions/{image_file_name}.jpg"):
                    question_text = (
                        process_image(f"{outputPath}/questions/{image_file_name}.jpg").lower().strip()
                    )
                    formatted_text = formatText(question_text)

                    level, chapter_num = get_level_and_chapter(formatted_text, paper_number, paperType, currentDefintionsData)

                    if not os.path.exists(f"{BASE_PATH}/resources/images/{paperType}/{subject}/mcq"):
                        os.makedirs(f"{BASE_PATH}/resources/images/{paperType}/{subject}/mcq")

                    shutil.copy(
                        f"{outputPath}/questions/{image_file_name}.jpg",
                        f"{BASE_PATH}/resources/images/{paperType}/{subject}/mcq/{image_file_name}.jpg",
                    )

                    answer_object = {
                        "questionName": f"{image_file_name}.jpg",
                        "Answer": answers[current_question_num - 1],
                        "pdfName": current_file,
                        "questionText": question_text,
                        "Chapter": chapter_num,
                        "Level": level,
                        "paperNumber": paper_number,
                        "Subject": subject,
                    }
                    questionObjects.append(answer_object)
                current_question_num += 1
    
    print(f"Finished processing {files[currentFileIndex]}...")


with open(f"{BASE_PATH}/resources/json/test_images.json", "w") as f:
    f.write("[\n")
    for obj in questionObjects:
        f.write(json.dumps(obj) + ",\n")
    f.write("]")
