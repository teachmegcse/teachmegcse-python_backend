import PIL
import os
import easyocr
import requests
from io import BytesIO
import json
import re
import sys
import shutil

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import (
    select_files, strip_images, take_screenshot, makeImages,
    merge_all_images, extract_paper_number, cleanup, clean_image
)

reader = easyocr.Reader(["en"])
output_path = f"{BASE_PATH}/resources/images/test_images"
definitionsPath = f"{BASE_PATH}/main/definitions.json"

def extract_question_number(im, current_question_num, output_path):
    returnArray = []
    try:
        ocr_corrections = {
            "|": "1",
            "@": "1",
            "M": "1",
            "l": "1",
            "I": "1",
            "[": "1",
            "O": "0",
            "o": "0",
            "s": "5",
            "S": "5",
            "}": ")",
        }

        buffer = BytesIO()
        im.save(buffer, format="JPEG")
        buffer.seek(0)
        files = {"file": buffer}
        response = requests.post("http://127.0.0.1:8000/predict", files=files)

        if response.status_code != 200 or not response.json():
            return []

        bounding_boxes = response.json()
        bounding_boxes.sort(key=lambda x: x[1])

        for box in bounding_boxes:
            current_box = im.crop((box[0], box[1], box[2], box[3]))
            current_box.save(f"{output_path}/questions/temp.jpg")
            text_in_box = reader.readtext(f"{output_path}/questions/temp.jpg")

            if text_in_box:
                text_in_box = text_in_box[0][1]  # Extract text from OCR result
                text_in_box = "".join([ocr_corrections.get(c, c) for c in text_in_box])
                print(f"Raw OCR text: {text_in_box}")

                isPaperCode = re.match(r"\d{4}/\d{2}", text_in_box)
                # Extract leading digits manually (no regex)
                digits_only = ""
                for c in text_in_box:
                    if c.isdigit():
                        digits_only += c
                    else:
                        break  # stop at first non-digit character

                print(f"Extracted digits: {digits_only}")

                if digits_only and (not isPaperCode):
                    number = int(digits_only)
                    if number > current_question_num:
                        returnArray.append(int(box[1]))
                        print(
                            f"Question number {current_question_num} found at y1: {
                                int(box[1])
                            }"
                        )
                        current_question_num += 1

        return returnArray

    except Exception as e:
        print(f"Error extracting question regions: {e}")
        return returnArray


if __name__ == "__main__":
    
    with open(definitionsPath, "r") as db:
        definitionsData = json.load(db)
    
    files = select_files()
    files = [file for file in files if "ms" in file.lower()]

    filename_num = 1
    for i in range(len(files)):
        for filename in os.listdir(f"{output_path}/currentPdfImages"):
            file_path = os.path.join(f"{output_path}/currentPdfImages", filename)
            if os.path.isfile(file_path):  # only delete files
                os.remove(file_path)
        
        filename = files[i].split("/")[-1]
        filename = filename.replace(".pdf", "")
        paperCode = filename.split("_")[0]

        if filename[0] == '0':
            paperType = 'IGCSE'
        else:
            paperType = 'A-level'

        if filename[0] == '0':
            level = 'IGCSE'
        else:
            level = 'A-level'

        currentDefintionsData = definitionsData[paperCode]
        subject = currentDefintionsData["subjectName"]
        db_name = currentDefintionsData["long_ms_db_path"]
        
        JSON_FILE_LOCATION = f"{BASE_PATH}/resources/json/{db_name}"
        if not os.path.exists(JSON_FILE_LOCATION):
            with open(JSON_FILE_LOCATION, "w") as f:
                json.dump([], f)  # Use [] if you expect a list

        # Load the file
        with open(JSON_FILE_LOCATION, "r") as json_file:
            ms_data = json.load(json_file)


        print(f"Processing PDF: {filename}")
        makeImages(files[i])
        strip_images(mode='ms')
        merge_all_images()
        currentQuestionNum = 1
        previous_y = 0

        # Sort pages numerically
        number_of_pages = sorted(
            os.listdir(f"{output_path}/currentPdfImages"), key=lambda x: int(x.split(".")[0])
        )

        paper_number = extract_paper_number(filename)

        for j in range(len(number_of_pages)):
            image_path = f"{output_path}/currentPdfImages/{number_of_pages[j]}"
            with PIL.Image.open(image_path) as im:
                y_coordinates = extract_question_number(
                    im, currentQuestionNum, output_path
                )
                if y_coordinates:
                    # Loop through each detected question Y-coordinate
                    for y1 in y_coordinates:
                        image_file_name = f"{subject}_p{paper_number}_ms_{
                            filename_num
                        }_{currentQuestionNum}"
                        take_screenshot(
                            previous_y,
                            # Include a small buffer below
                            y1 + (j) * 1300 + 10,
                            image_file_name,
                            'long',
                            ''
                        )

                        ms_data.append(
                            {
                                "fileName": image_file_name + ".jpg",
                                "questionNumber": currentQuestionNum,
                                "paperCode": filename,
                            }
                        )
                        previous_y = y1 + (j) * 1300
                        currentQuestionNum += 1
                        filename_num += 1

                        if not os.path.exists(f"{BASE_PATH}/resources/images/{paperType}/{subject}/long"):
                            os.makedirs(f"{BASE_PATH}/resources/images/{paperType}/{subject}/long")

                        shutil.copy(
                            f"{output_path}/questions/{image_file_name}.jpg",
                            f"{BASE_PATH}/resources/images/{paperType}/{subject}/long/{
                                image_file_name
                            }.jpg",
                        )

                        clean_image(paperType, subject, "long", f"{image_file_name}.jpg")

        image_file_name = (
            f"{subject}_p{paper_number}_ms_{filename_num}_{currentQuestionNum}"
        )
        take_screenshot(
            previous_y,
            (len(number_of_pages)) * 1300,
            image_file_name,
            'long',
            ''
        )
        ms_data.append(
            {
                "fileName": image_file_name + ".jpg",
                "questionNumber": currentQuestionNum,
                "paperCode": filename,
            }
        )

        shutil.copy(
                    f"{output_path}/questions/{image_file_name}.jpg",
                    f"{BASE_PATH}/resources/images/{paperType}/{subject}/long/{
                        image_file_name
                    }.jpg",
                )
        
        clean_image(paperType, subject, "long", f"{image_file_name}.jpg")

        filename_num += 1
        try:
            with open(JSON_FILE_LOCATION, "w") as json_file:
                json.dump(ms_data, json_file, indent=1)
                cleanup()
        except Exception as e:
            print(f"Error saving JSON data: {str(e)}")
