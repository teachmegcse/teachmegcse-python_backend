"""
Script to process and extract mark scheme data from PDF files.
Handles image processing and text extraction for educational mark schemes.
"""

# Standard library imports
import json
from os.path import exists
import os
from typing import List, Tuple

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
    """
    Search horizontally in an image for a specific color at a given y-coordinate.
    
    Args:
        img: PIL Image object to search in
        search_color: RGB color tuple to search for
        constant_y: Y-coordinate to search along
        start_of_img: If True, search from left to right; if False, right to left
        double_check: If True, verify color appears in two consecutive pixels
    
    Returns:
        x-coordinate where color is found, or -1 if not found
    """
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
    """
    Search vertically in an image for a specific color at a given x-coordinate.
    
    Args:
        img: PIL Image object to search in
        search_color: RGB color tuple to search for
        constant_x: X-coordinate to search along
        start_of_img: If True, search from top to bottom; if False, bottom to top
        double_check: If True, verify color appears in two consecutive pixels
        not_color: If True, search for pixels that are NOT the specified color
    
    Returns:
        y-coordinate where condition is met, or -1 if not found
    """
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
    """
    Combine multiple images vertically into a single image.
    
    Args:
        image_array: List of PIL Image objects to combine
        save_path: Path where the combined image will be saved
    """
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

# Configuration constants
OUTPUT_DIRECTORY = r"D:\python_projects\teachmegcse\images\unsorted"
JSON_FILE_LOCATION = r"D:\python_projects\teachmegcse\json_files\phy_db_ms_p4.json"
pytesseract.pytesseract.tesseract_cmd = r"D:\python_projects\Tesseract-OCR\tesseract.exe"

def make_question_ms(ms_pdf: str, subject_name: str, subject_code: int) -> None:
    """
    Process a mark scheme PDF and extract relevant data.
    
    Args:
        ms_pdf: Path to the mark scheme PDF file
        subject_name: Name of the subject (e.g. "Physics")
        subject_code: Code for the subject (e.g. 9702)
    """
    pdf_directory = f"D:/python_projects/teachmegcse/full_pdfs/{subject_code}"
    output_folder = f"{OUTPUT_DIRECTORY}/A-level/{subject_name}/p4"
    temp_files = []  # Keep track of temporary files for cleanup
    
    question_number = 1
    end_of_question = False
    total_pages = convert_from_path(f"{pdf_directory}/{ms_pdf}", poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin")
    current_question = []
    ms_pages = []
    first_page = False
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

    for i in range(3, len(total_pages)):
        this_page = total_pages[i].crop((
            search_in_x(total_pages[i], (0, 0, 0), 210),
            search_in_y(total_pages[i], (0, 0, 0), 500) + 68,
            search_in_x(total_pages[i], (0, 0, 0), 210, start_of_img=False),
            search_in_y(total_pages[i], (0, 0, 0), 500, start_of_img=False)
        ))
        
        if first_page:
            ms_pages.append(this_page)
            temp_file = f"{output_folder}/{subject_name}_page_{i}.jpg"
            this_page.save(temp_file)
            temp_files.append(temp_file)
            
        if pytesseract.image_to_string(this_page)[0] == "1" and not first_page:
            first_page = True
            ms_pages.append(this_page)
            temp_file = f"{output_folder}/{subject_name}_page_{i}.jpg"
            this_page.save(temp_file)
            temp_files.append(temp_file)

    for page in ms_pages:
        first_num = pytesseract.image_to_string(page)[0]
        if int(first_num) == 1 and question_number > 7:
            first_num = pytesseract.image_to_string(page)[:2]
        
        # Convert letter grades to numbers
        if first_num == "A": first_num = 4
        if first_num == "B": first_num = 6
        
        if question_number != int(first_num):
            output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
            combine_array_images(current_question, output_file)
            
            if first_json:
                ms_data = [{"fileName": f"{subject_name}_ms_{current_file_number}.jpg", "questionNumber": question_number, "paperCode": ms_pdf}]
                first_json = False
            else:
                ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", "questionNumber": question_number, "paperCode": ms_pdf})
            
            current_file_number += 1
            question_number += 1
            end_of_question = False
            current_question = []

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
                ms_data = [{"fileName": f"{subject_name}_ms_{current_file_number}.jpg", "questionNumber": question_number, "paperCode": ms_pdf}]
                first_json = False
            else:
                ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", "questionNumber": question_number, "paperCode": ms_pdf})
            
            question_number += 1
            current_file_number += 1
            
            if y < page.height:
                current_question = [page.crop((0, y + 114, page.width, page.height))]
                end_of_question = False
        else:
            current_question.append(page)

    if current_question:
        output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
        combine_array_images(current_question, output_file)
        ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", "questionNumber": question_number, "paperCode": ms_pdf})

    # Save JSON data
    with open(JSON_FILE_LOCATION, 'w') as json_file:
        json.dump(ms_data, json_file, indent=1)
        
    # Cleanup temporary files
    for temp_file in temp_files:
        try:
            os.remove(temp_file)
        except OSError as e:
            print(f"Error deleting temporary file {temp_file}: {e}")

# make_question_ms("9702_m21_ms_42.pdf", 'physics', 9702)