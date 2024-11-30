import json
from os.path import exists
import os
from typing import List, Tuple
import cv2
import numpy as np
from PIL import Image, ImageEnhance

# Third-party imports
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def search_in_x(
    img: Image.Image,
    search_color: Tuple[int, int, int],
    constant_y: int,
    start_of_img: bool = True,
    double_check: bool = False
) -> int:
    current_pixel = img.load()
    start = 0 if start_of_img else img.width - 1
    end = img.width - 1 if start_of_img else 0
    step = 1 if start_of_img else -1

    for i in range(start, end, step):
        if current_pixel[i, constant_y] == search_color:
            if double_check:
                if current_pixel[i + 1, constant_y] == search_color:
                    return i
            else:
                return i
    return -1

def search_in_y(
    img: Image.Image,
    search_color: Tuple[int, int, int],
    constant_x: int,
    start_of_img: bool = True,
    double_check: bool = False,
    not_color: bool = False
) -> int:
    current_pixel = img.load()
    start = 0 if start_of_img else img.height - 1
    end = img.height - 1 if start_of_img else 0
    step = 1 if start_of_img else -1

    for i in range(start, end, step):
        pixel_matches = (
            current_pixel[constant_x, i] != search_color
            if not_color
            else current_pixel[constant_x, i] == search_color
        )
        
        if pixel_matches:
            if double_check:
                next_pixel_matches = (
                    current_pixel[constant_x, i + 1] != search_color
                    if not_color
                    else current_pixel[constant_x, i + 1] == search_color
                )
                if next_pixel_matches:
                    return i
            else:
                return i
    return -1

def combine_array_images(image_array: List[Image.Image], save_path: str) -> None:
    if len(image_array) == 1:
        image_array[0].save(save_path)
        return

    # Calculate dimensions for the combined image
    width = image_array[0].width
    total_height = sum(img.height for img in image_array)
    
    # Create new image and combine all images vertically
    combined_image = Image.new('RGB', [width, total_height], (255, 255, 255))
    current_y = 0
    
    for image in image_array:
        combined_image.paste(image, (0, current_y))
        current_y += image.height
    
    combined_image.save(save_path)

def find_content_boundaries(page: Image.Image) -> tuple:
    # Try multiple y-coordinates for horizontal search
    y_search_points = [210, 300, 400, 500]
    # Try multiple x-coordinates for vertical search
    x_search_points = [500, 400, 300, 200]
    
    # Find left boundary
    left_x = -1
    for y in y_search_points:
        if y >= page.height:
            continue
        left = search_in_x(page, (0, 0, 0), y)
        if left != -1:
            left_x = left
            break
    
    # Find right boundary
    right_x = -1
    for y in y_search_points:
        if y >= page.height:
            continue
        right = search_in_x(page, (0, 0, 0), y, start_of_img=False)
        if right != -1:
            right_x = right
            break
    
    # Find top boundary
    top_y = -1
    for x in x_search_points:
        if x >= page.width:
            continue
        top = search_in_y(page, (0, 0, 0), x)
        if top != -1:
            top_y = top
            break
    
    # Find bottom boundary
    bottom_y = -1
    for x in x_search_points:
        if x >= page.width:
            continue
        bottom = search_in_y(page, (0, 0, 0), x, start_of_img=False)
        if bottom != -1:
            bottom_y = bottom
            break

    return left_x, top_y, right_x, bottom_y

def preprocess_image_for_ocr(pil_image):
    # Convert PIL to CV2
    cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to get black and white image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Convert back to PIL
    return Image.fromarray(thresh)

def extract_question_number(page_image, expected_number=None):
    # Crop the image to 150x150 from top-left corner
    crop_size = 150
    region = page_image.crop((0, 0, min(crop_size, page_image.width), min(crop_size, page_image.height)))
    
    # Enhance the cropped image
    enhanced_image = preprocess_image_for_ocr(region)
    
    # Configure Tesseract for digits
    custom_config = r'--oem 3 --psm 6'
    
    # Try to get text from enhanced image
    enhanced_text = pytesseract.image_to_string(enhanced_image, config=custom_config)
    
    # Get first non-empty line
    lines = [line.strip() for line in enhanced_text.split('\n') if line.strip()]

    # Extract first token that could be a number
    potential_numbers = []
    for line in lines[:3]:  # Check first 3 lines
        tokens = line.split()
        if tokens:
            potential_numbers.append(tokens[0])
    
    if not potential_numbers:  # If no numbers found
        enhanced_image.save(f"enhanced_empty.jpg")
        return None

    # Handle common OCR mistakes
    ocr_corrections = {
        '|': '1', '@': '1', 'M': '1',
        'l': '1', 'I': '1', '[': '1',
        'O': '0', 'o': '0'
    }
    
    first_char = potential_numbers[0][0] if potential_numbers[0] else ''
    if first_char in ocr_corrections:
        first_char = ocr_corrections[first_char]

    # Save enhanced image for debugging
    enhanced_image.save(f"enhanced_{first_char}.jpg")
    
    # Check for double-digit numbers
    if potential_numbers[0] and len(potential_numbers[0]) >= 2 and potential_numbers[0][:2].isdigit():
        return potential_numbers[0][:2]
    
    return first_char if first_char.isdigit() else None

# Configuration constants
OUTPUT_DIRECTORY = r"D:\python_projects\teachmegcse\images\unsorted"
JSON_FILE_LOCATION = r"D:\python_projects\teachmegcse\json_files\phy_db_ms_p4.json"
pytesseract.pytesseract.tesseract_cmd = r"D:\python_projects\Tesseract-OCR\tesseract.exe"

def make_question_ms(ms_pdf: str, subject_name: str, subject_code: int) -> None:
    try:
        print(f"Processing mark scheme: {ms_pdf}")
        pdf_directory = f"D:/python_projects/teachmegcse/full_pdfs/{subject_code}"
        output_folder = f"{OUTPUT_DIRECTORY}/A-level/{subject_name}/p4"
        temp_files = []  # Keep track of temporary files for cleanup
        
        question_number = 1
        end_of_question = False
        total_pages = convert_from_path(f"{pdf_directory}/{ms_pdf}", poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin")
        current_question = []
        ms_pages = []
        first_json = True
        ms_data = []

        # Ensure output directory exists
        os.makedirs(output_folder, exist_ok=True)

        if exists(JSON_FILE_LOCATION):
            with open(JSON_FILE_LOCATION, 'r') as json_file:
                ms_data = json.load(json_file)
                first_json = False

        current_file_number = 1
        while exists(f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"):
            current_file_number += 1

        # Process pages starting from page 4 (skipping cover pages)
        for i in range(4, len(total_pages)):
            try:
                # Find content boundaries using original method
                left_x = search_in_x(total_pages[i], (0, 0, 0), 210)
                top_y = search_in_y(total_pages[i], (0, 0, 0), 500) + 68
                right_x = search_in_x(total_pages[i], (0, 0, 0), 210, start_of_img=False)
                bottom_y = search_in_y(total_pages[i], (0, 0, 0), 500, start_of_img=False)
                
                
                this_page = total_pages[i].crop((left_x, top_y, right_x, bottom_y))
                page_text = pytesseract.image_to_string(this_page)
                    
                if page_text and ("question" in page_text.lower() or "1" in page_text.lower()):
                    ms_pages.append((this_page, i))  # Store the page number along with the image
                    temp_file = f"{output_folder}/{subject_name}_page_{i}.jpg"
                    this_page.save(temp_file)
                    temp_files.append(temp_file)

            except Exception as e:
                print(f"Error processing page {i}: {str(e)}")
                continue

        for page, page_num in ms_pages:
            try:
                first_num = extract_question_number(page)
                
                if first_num is None:
                    print(f"Could not extract question number on page {page_num}, skipping...")
                    continue
                                    
                try:
                    if int(first_num) > 13:
                        first_num = first_num[0]
                except ValueError:
                    # If conversion fails, skip this page
                    print(f"Invalid number format on page {page_num}, skipping...")
                    continue
                
                print(f"Question number: {first_num} on page {page_num}")

                if question_number != int(first_num):
                    output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
                    combine_array_images(current_question, output_file)
                    
                    if first_json:
                        ms_data = [{"fileName": f"{subject_name}_ms_{current_file_number}.jpg", 
                                  "questionNumber": question_number, 
                                  "paperCode": ms_pdf}]
                        first_json = False
                    else:
                        ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", 
                                      "questionNumber": question_number, 
                                      "paperCode": ms_pdf})
                    
                    current_file_number += 1
                    question_number += 1
                    end_of_question = False
                    current_question = []

                # Check for question boundaries using pixel analysis
                pixel = page.load()
                y = 0
                pixel_color = pixel[0, y]
                
                while pixel_color != (255, 255, 255) and y < page.height:
                    pixel_color = pixel[0, y]
                    if pixel_color == (255, 255, 255):
                        pixel_color = pixel[0, y + 1]
                        if pixel_color == (255, 255, 255):
                            end_of_question = True
                            break
                    y += 1

                if end_of_question:
                    current_question.append(page.crop((0, 0, page.width, y)))
                    output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
                    combine_array_images(current_question, output_file)
                    
                    if first_json:
                        ms_data = [{"fileName": f"{subject_name}_ms_{current_file_number}.jpg", 
                                  "questionNumber": question_number, 
                                  "paperCode": ms_pdf}]
                        first_json = False
                    else:
                        ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", 
                                      "questionNumber": question_number, 
                                      "paperCode": ms_pdf})
                    
                    question_number += 1
                    current_file_number += 1
                    
                    if y < page.height:
                        current_question = [page.crop((0, y + 114, page.width, page.height))]
                        end_of_question = False
                else:
                    current_question.append(page)

            except Exception as e:
                print(f"Error processing page content: {str(e)}")
                continue

        # Save the last question if we have one
        if current_question:
            try:
                output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
                combine_array_images(current_question, output_file)
                ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", 
                              "questionNumber": question_number, 
                              "paperCode": ms_pdf})
            except Exception as e:
                print(f"Error saving final question: {str(e)}")

        try:
            with open(JSON_FILE_LOCATION, 'w') as json_file:
                json.dump(ms_data, json_file, indent=1)
        except Exception as e:
            print(f"Error saving JSON data: {str(e)}")

        # Cleanup temporary files
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except Exception as e:
                print(f"Error removing temporary file {temp_file}: {str(e)}")
        
        print("Mark scheme processing completed!")
                
    except Exception as e:
        print(f"Error processing mark scheme {ms_pdf}: {str(e)}")