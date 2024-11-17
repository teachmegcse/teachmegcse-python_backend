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

def find_content_boundaries(page: Image.Image) -> tuple:
    """
    Find content boundaries using multiple search points.
    Returns (left_x, top_y, right_x, bottom_y) or None if no valid boundaries found.
    """
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
    
    # If we couldn't find boundaries, try using image dimensions
    if -1 in [left_x, right_x, top_y, bottom_y]:
        # Use 10% margin from edges as fallback
        margin_x = page.width // 10
        margin_y = page.height // 10
        left_x = margin_x if left_x == -1 else left_x
        right_x = (page.width - margin_x) if right_x == -1 else right_x
        top_y = margin_y if top_y == -1 else top_y
        bottom_y = (page.height - margin_y) if bottom_y == -1 else bottom_y
    
    return left_x, top_y, right_x, bottom_y

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
        first_page = False
        first_json = True
        ms_data = []

        print(f"Total pages in PDF: {len(total_pages)}")
        print(f"Output folder: {output_folder}")

        # Ensure output directory exists
        os.makedirs(output_folder, exist_ok=True)

        if exists(JSON_FILE_LOCATION):
            with open(JSON_FILE_LOCATION, 'r') as json_file:
                ms_data = json.load(json_file)
                first_json = False

        current_file_number = 1
        while exists(f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"):
            current_file_number += 1

        print(f"Starting with file number: {current_file_number}")

        # Process pages starting from page 3 (skipping cover pages)
        for i in range(3, len(total_pages)):
            try:
                print(f"\nProcessing page {i}")
                # Find content boundaries using original method
                left_x = search_in_x(total_pages[i], (0, 0, 0), 210)
                top_y = search_in_y(total_pages[i], (0, 0, 0), 500) + 68
                right_x = search_in_x(total_pages[i], (0, 0, 0), 210, start_of_img=False)
                bottom_y = search_in_y(total_pages[i], (0, 0, 0), 500, start_of_img=False)
                
                print(f"Found boundaries: ({left_x}, {top_y}) to ({right_x}, {bottom_y})")
                
                this_page = total_pages[i].crop((left_x, top_y, right_x, bottom_y))
                page_text = pytesseract.image_to_string(this_page)
                print(f"Extracted text length: {len(page_text)}")
                print(f"First few characters: {page_text[:50] if page_text else 'No text found'}")
                
                if first_page:
                    ms_pages.append(this_page)
                    temp_file = f"{output_folder}/{subject_name}_page_{i}.jpg"
                    this_page.save(temp_file)
                    temp_files.append(temp_file)
                    print(f"Saved temporary page: {temp_file}")
                    
                if page_text and page_text[0] == "1" and not first_page:
                    print("Found first page with question 1")
                    first_page = True
                    ms_pages.append(this_page)
                    temp_file = f"{output_folder}/{subject_name}_page_{i}.jpg"
                    this_page.save(temp_file)
                    temp_files.append(temp_file)

            except Exception as e:
                print(f"Error processing page {i}: {str(e)}")
                continue

        print("\nProcessing mark scheme pages...")
        for page in ms_pages:
            try:
                page_text = pytesseract.image_to_string(page)
                first_num = page_text[0]
                
                # Handle double-digit question numbers
                if int(first_num) == 1 and question_number > 7:
                    first_num = page_text[:2]
                
                # Convert letter grades to numbers
                if first_num == "A": first_num = "4"
                if first_num == "B": first_num = "6"
                
                print(f"Processing question {first_num}")
                
                if question_number != int(first_num):
                    print(f"Saving question {question_number}")
                    output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
                    combine_array_images(current_question, output_file)
                    print(f"Saved to: {output_file}")
                    
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
                    print(f"Found end of question at y={y}")
                    current_question.append(page.crop((0, 0, page.width, y)))
                    output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
                    combine_array_images(current_question, output_file)
                    print(f"Saved to: {output_file}")
                    
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
                print(f"Saving final question {question_number}")
                output_file = f"{output_folder}/{subject_name}_ms_{current_file_number}.jpg"
                combine_array_images(current_question, output_file)
                print(f"Saved to: {output_file}")
                ms_data.append({"fileName": f"{subject_name}_ms_{current_file_number}.jpg", 
                              "questionNumber": question_number, 
                              "paperCode": ms_pdf})
            except Exception as e:
                print(f"Error saving final question: {str(e)}")

        print("\nSaving JSON data...")
        # Save JSON data
        try:
            with open(JSON_FILE_LOCATION, 'w') as json_file:
                json.dump(ms_data, json_file, indent=1)
            print("JSON data saved successfully")
        except Exception as e:
            print(f"Error saving JSON data: {str(e)}")

        print("\nCleaning up temporary files...")
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

# make_question_ms("9702_m21_ms_42.pdf", 'physics', 9702)