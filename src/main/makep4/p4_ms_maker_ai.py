import sys
import os


import PIL.Image
from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import easyocr
import requests
from io import BytesIO
import json
from pathConst import POPPLER_PATH
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
def select_files():
    root = Tk()
    filetypes = [("PDF Files", "*.pdf")]
    files = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    return list(files)

def strip_images(output_path, i):
    pages = os.listdir(f"{output_path}/{i}")
    for page in pages:
        if page.endswith('.jpg'):
            image_path = os.path.join(output_path, f"{i}/{page}")
            with PIL.Image.open(image_path) as im:
                im_crop = im.crop((100, 200, 2300, 1500))
                im_crop.save(image_path)

def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    
    # Create output directory for this PDF
    pdf_output_path = os.path.join(output_path, str(i))
    os.makedirs(pdf_output_path, exist_ok=True)
    
    # Create final directory if it doesn't exist
    final_path = os.path.join(output_path, 'final')
    os.makedirs(final_path, exist_ok=True)
    
    current_index = 1
    for x in range(1, number_of_pages):
        page = reader.pages[x]
        text = page.extract_text()
        text = text.lower()
        if x >= 1:
            # Skip if page contains any of these strings
            skip_strings = ["blank page", "important values", "periodic table", "next page", "guidance", "marking principle", "correct answer only"]
            if not any(s in text for s in skip_strings):
                images[x].save(f"{pdf_output_path}/{current_index}.jpg", 'JPEG')
                current_index += 1

def extract_question_number(im, current_question_num, output_path):
    returnArray = []
    try:
        ocr_corrections = {
            '|': '1', '@': '1', 'M': '1',
            'l': '1', 'I': '1', '[': '1',
            'O': '0', 'o': '0', 's': '5', 'S': '5',
            '}': ')',
        }

        buffer = BytesIO()
        im.save(buffer, format='JPEG')
        buffer.seek(0)
        files = {'file': buffer}
        response = requests.post('http://127.0.0.1:8000/predict', files=files)

        if response.status_code != 200 or not response.json():
            return []

        bounding_boxes = response.json()
        bounding_boxes.sort(key=lambda x: x[1])

        for box in bounding_boxes:
            current_box = im.crop((box[0], box[1], box[2], box[3]))
            current_box.save(f"{output_path}/questions/temp.jpg")
            text_in_box = easyocr.Reader(['en']).readtext(f"{output_path}/questions/temp.jpg")

            if text_in_box:
                text_in_box = text_in_box[0][1]  # Extract text from OCR result
                text_in_box = ''.join([ocr_corrections.get(c, c) for c in text_in_box])
                print(f"Raw OCR text: {text_in_box}")

                # Extract leading digits manually (no regex)
                digits_only = ''
                for c in text_in_box:
                    if c.isdigit():
                        digits_only += c
                    else:
                        break  # stop at first non-digit character

                print(f"Extracted digits: {digits_only}")

                if digits_only:
                    number = int(digits_only)
                    if number > current_question_num:
                        returnArray.append(int(box[1]))
                        print(f"Question number {current_question_num} found at y1: {int(box[1])}")
                        current_question_num += 1

        print(f"returnArray: {returnArray} at iteration {current_question_num}")
        return returnArray

    except Exception as e:
        print(f"Error extracting question regions: {e}")
        return returnArray


def merge_all_images(folder_num, output_path):
    pages = os.listdir(f"{output_path}/{folder_num}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    
    # First pass to get total height
    total_height = 0
    for page_file in pages:
        with PIL.Image.open(f"{output_path}/{folder_num}/{page_file}") as im:
            total_height += im.height
    
    dst = PIL.Image.new('RGB', (2200, total_height), color='white')
    current_height = 0
    
    # Second pass to merge images
    for page_file in pages:
        image_path = f"{output_path}/{folder_num}/{page_file}"
        with PIL.Image.open(image_path) as im:
            dst.paste(im, (0, current_height))
            current_height += im.height
    
    dst.save(f"{output_path}/final/final{folder_num}.jpg")


def take_screenshot(y1, y2, file_name, output_path, unique_filename, current_question_num):
    print(f"\nTaking screenshot for question {current_question_num}")
    print(f"Coordinates: y1={y1}, y2={y2}")

    if (y2 - y1) > 100: # Reduced minimum height
        with PIL.Image.open(f"{output_path}/final/final{file_name}.jpg") as im:
            im_crop = im.crop((0, y1, 2200, y2))
            im_crop.save(f"{output_path}/questions/{unique_filename}.jpg")
    else:
        print(f"Skipping question {current_question_num} - too small ({y2 - y1} pixels)")

if __name__ == "__main__":
    files = select_files()
    files = [file for file in files if 'ms' in file.lower()]
    output_path = f"{BASE_PATH}/resources/images/test_images"
    JSON_FILE_LOCATION = f"{BASE_PATH}/resources/json/phy_db_ms_p4.json"
    with open(JSON_FILE_LOCATION, 'r') as json_file:
        ms_data = json.load(json_file)

    for i in range(len(files)):
        filename = files[i].split('/')[-1]
        filename = filename.replace('.pdf', '')
        print(f"Processing PDF: {filename}")
        makeImages(output_path, files[i], i)
        strip_images(output_path, i)
        merge_all_images(i, output_path)
        currentQuestionNum = 1
        previous_y = 0
        
        # Sort pages numerically
        number_of_pages = sorted(
            os.listdir(f"{output_path}/{i}"), 
            key=lambda x: int(x.split('.')[0])
        )
        
        
        for j in range(len(number_of_pages)):
            image_path = f"{output_path}/{i}/{number_of_pages[j]}"
            with PIL.Image.open(image_path) as im:
                y_coordinates = extract_question_number(im, currentQuestionNum, output_path)
                if y_coordinates:
                    # Loop through each detected question Y-coordinate
                    for y1 in y_coordinates:
                        take_screenshot(previous_y, y1 + (j) * 1300 + 10,  # Include a small buffer below
                                         i, output_path, f"{i}_ms_{currentQuestionNum}", currentQuestionNum)

                        ms_data.append({"fileName": f"{i}_ms_{currentQuestionNum}.jpg", 
                                          "questionNumber": currentQuestionNum, 
                                          "paperCode": filename})
                        previous_y = y1 + (j) * 1300
                        currentQuestionNum += 1
        
        take_screenshot(previous_y, (len(number_of_pages)) * 1300, i, output_path, f"{i}_ms_{currentQuestionNum}", currentQuestionNum)
        ms_data.append({"fileName": f"{i}_ms_{currentQuestionNum}.jpg", 
                                          "questionNumber": currentQuestionNum, 
                                          "paperCode": filename})
        try:
            with open(JSON_FILE_LOCATION, 'w') as json_file:
                json.dump(ms_data, json_file, indent=1)
        except Exception as e:
            print(f"Error saving JSON data: {str(e)}")
