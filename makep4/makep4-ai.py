import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import json
import requests
import multiprocessing
from pathConst import BASE_PATH, POPPLER_PATH, TESSERACT_PATH
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import cv2
import pytesseract
from joblib import load
import shutil

# Constants for Tesseract and custom configuration
model = 'IGchem'
CUSTOM_CONFIG = r'--oem 3 --psm 6'
MODEL_PATH_TEMPLATE = f"{BASE_PATH}/python_files/sci-kit/{model}.joblib"

ALL_LABELS = ['States of matter', 'Atoms, elements and compounds', 
             'Stoichiometry', 'Electrochemistry', 'Chemical energetics', 'Chemical reactions', 'Acids, bases and salts',
               'The Periodic Table', 'Metals', 'Chemistry of the environment', 'Organic chemistry', 'Experimental techniques and chemical analysis']

def predict(data, model):
    pipeline = load(MODEL_PATH_TEMPLATE.format(model=model))
    data = formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]

def formatText(text):
    stemmer=PorterStemmer()

    # Convert all text to lowercase
    text = text.lower()

    # Remove punctuation, digits, and non-alphabetic characters
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    
    # Remove Cambridge command words
    text = text.replace("analyse",""); text = text.replace("assess",""); text = text.replace("calculate","")
    text = text.replace("comment",""); text = text.replace("compare",""); text = text.replace("consider","")
    text = text.replace("contrast",""); text = text.replace("define",""); text = text.replace("describe","")
    text = text.replace("develop",""); text = text.replace("discuss",""); text = text.replace("evaluate","")
    text = text.replace("explain",""); text = text.replace("give",""); text = text.replace("identify","")
    text = text.replace("justify",""); text = text.replace("outline",""); text = text.replace("predict","")
    text = text.replace("sketch",""); text = text.replace("state",""); text = text.replace("suggest","")
    text = text.replace("summarise",""); text = text.replace("benefit",""); text = text.replace("drawback","")
    text = text.replace("advantage",""); text = text.replace("disadvantage",""); text = text.replace("understand","")
    text = text.replace("use",""); text = text.replace("notes and guidance",""); text = text.replace("candidates should be able to","")
    text = text.replace("show",""); text = text.replace("understanding","")

    # Tokenize text into words
    words = word_tokenize(text)
    # Stem words
    words = [stemmer.stem(w) for w in words]

    # Join the processed words back into a single string
    return ' '.join(words)

def process_image(image_path, custom_config=CUSTOM_CONFIG):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img, config=custom_config)

def select_files():
    root = Tk()
    filetypes = [("PDF Files", "*.pdf")]
    files = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    return list(files)

def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    current_index = 1
    for x in range(1, number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        text = page.extract_text()
        text = text.lower()
        if x >= 1:
            # Skip if page contains any of these strings
            skip_strings = ["blank page", "important values", "lanthanoids", "next page"]
            if not any(s in text for s in skip_strings):
                images[x].save(f"{output_path}/{i}/{current_index}.jpg", 'JPEG')
                current_index += 1

def strip_images(folder_num, output_path):
    pages = os.listdir(f"{output_path}/{folder_num}")
    for i in range(len(pages)):
        with PIL.Image.open(f"{output_path}/{folder_num}/{pages[i]}") as im:
            im_crop = im.crop((0, 150, 1654, 2200))
            im_crop.save(f"{output_path}/{folder_num}/{pages[i]}")

def get_dimensions_from_api(image_path):
    print(f"Opening image file: {image_path}")
    with open(image_path, 'rb') as img:
        files = {'file': img}
        print("Sending request to API...")
        response = requests.post('http://127.0.0.1:8000/predict', files=files)
        print(f"API response status code: {response.status_code}")
        if response.status_code == 200:
            coordinates = response.json()
            return coordinates
        else:
            print(f"API response text: {response.text}")
            raise Exception(f"API request failed with status code {response.status_code}")

def get_all_page_coordinates(folder_num, output_path):
    print("Getting coordinates for all pages...")
    pages = os.listdir(f"{output_path}/{folder_num}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    all_coordinates = []
    page_heights = []
    
    for page_file in pages:
        current_height = (int(page_file.split(".")[0]) - 1) * 2050
        page_path = f"{output_path}/{folder_num}/{page_file}"
        print(f"\nProcessing page: {page_file}")
        
        # Get coordinates for this page
        try:
            bounding_boxes = get_dimensions_from_api(page_path)
            print(f"Got boxes for page {page_file}: {bounding_boxes}")
            
            if not bounding_boxes:  # Skip if no questions found
                continue
                
            # Take only the first box if multiple exist
            if bounding_boxes:
                first_box = bounding_boxes[0]
                y1 = first_box[1]  # Top y coordinate only
                x1 = first_box[0]
                if x1 > 150:
                    continue
                else:
                    print(f"Using y-coordinate {y1} from first box on page {page_file}")
                    
                    # Adjust coordinate based on current height in final image
                    adjusted_y = int(y1 + current_height)
                    print(f"Adjusted y-coordinate for page {page_file}: {adjusted_y} (added {current_height})")
                    all_coordinates.append(adjusted_y)
            
            # Update current height
            with PIL.Image.open(page_path) as im:
                page_height = im.height
                page_heights.append(page_height)
                print(f"Page {page_file} height: {page_height}")
                current_height += page_height
                print(f"New cumulative height: {current_height}")
                
        except Exception as e:
            print(f"Error processing page {page_file}: {str(e)}")
            continue
    
    # Sort all coordinates to ensure they're in order
    all_coordinates = sorted(list(set(all_coordinates)))
    print("\nFinal coordinates after processing all pages:", all_coordinates)
    
    # Add the total height as the last coordinate to capture the last question
    all_coordinates.append(current_height)
    print("Final coordinates with total height:", all_coordinates)
    
    return all_coordinates, current_height

def merge_all_images(folder_num, output_path, heightsArr):
    pages = os.listdir(f"{output_path}/{folder_num}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    
    # First pass to get total height
    total_height = 0
    for page_file in pages:
        with PIL.Image.open(f"{output_path}/{folder_num}/{page_file}") as im:
            total_height += im.height
    
    dst = PIL.Image.new('RGB', (1654, total_height), color='white')
    current_height = 0
    
    # Second pass to merge images
    for page_file in pages:
        image_path = f"{output_path}/{folder_num}/{page_file}"
        with PIL.Image.open(image_path) as im:
            dst.paste(im, (0, current_height))
            current_height += im.height
    
    dst.save(f"{output_path}/final/final{folder_num}.jpg")
    heightsArr[folder_num] = total_height
    return current_height

def take_screenshot(y1, y2, current_question_num, file_name, output_path, unique_filename):
    print(f"\nTaking screenshot for question {current_question_num}")
    print(f"Coordinates: y1={y1}, y2={y2}")
    if (y2 - y1) > 300:
        with PIL.Image.open(f"{output_path}/final/{file_name}") as im:
            print(f"Image size: {im.size}")
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output_path}/questions/{unique_filename}.jpg")
            print(f"Saved question {current_question_num}")
    else:
        print(f"Skipping question {current_question_num} - too small ({y2 - y1} pixels)")

def extract_paper_number(filename):
    try:
        base_name = filename.split('.')[0]
        
        parts = base_name.split('_')
        
        if len(parts) >= 4:
            return int(parts[3][0])
    except Exception as e:
        print(f"Error: {e}")
    return None

def process_question_paper(file_path, m, file_question_counts, output1Path, finalOutputPath, subject2, heightsArr, db_path):
    global unique_num
    ASpapers = [2, 3]
    A2papers = [4, 5]
    print(f"Starting to process question paper: {file_path}")
    current_file = file_path[-18:]
    file_question_counts[current_file] = 0
    
    # Extract paper number from filename
    paper_num = extract_paper_number(current_file)
    
    # Process the paper
    print("Converting PDF to images...")
    makeImages(output1Path, file_path, m)
    print("Stripping images...")
    strip_images(m, output1Path)
    
    # Get coordinates from individual pages first
    coordinates, total_height = get_all_page_coordinates(m, output1Path)
    print(f"Got all coordinates: {coordinates}")
    
    # Merge images after getting coordinates
    print("Merging images...")
    merge_all_images(m, output1Path, heightsArr)
    
    try:
        # Open the database file in append mode
        with open(db_path, 'a') as db:
            # Process each question based on the adjusted coordinates
            for i in range(len(coordinates) - 1):
                y1 = coordinates[i]
                y2 = coordinates[i + 1]
                current_question_num = i + 1
                
                print(f"Processing question {current_question_num} with coordinates y1={y1}, y2={y2}")
                unique_filename = f"{subject2}_p{paper_num}_qp_{unique_num}"
                take_screenshot(y1, y2, current_question_num, f"final{m}.jpg", output1Path, subject, unique_filename)
                
                # Clean the cropped image
                input_path = f"{output1Path}/questions/{unique_filename}.jpg"
                question_text = process_image(input_path)
                formatted_text = formatText(question_text)
                chapter = predict(formatted_text, subject)
                chapter_num = ALL_LABELS.index(chapter) + 1 if chapter in ALL_LABELS else 0
                print(f"Chapter prediction for question {current_question_num}: {chapter}")
                if os.path.exists(input_path):
                    file_question_counts[current_file] += 1
                    
                    # Extract year from filename (e.g., m15 -> 2015)
                    year = "20" + current_file.split("_")[1][1:3]
                    current_file2 = current_file.replace(".pdf", "")
                    if paper_num in ASpapers:
                        level2 = "AS"
                    elif paper_num in A2papers:
                        level2 = "A2"
                    level2 = "IGCSE"

                    if not os.path.exists(f"{BASE_PATH}/images/sorted/{level2}/{subject2}/long/{chapter_num}"):
                        os.makedirs(f"{BASE_PATH}/images/sorted/{level2}/{subject2}/long/{chapter_num}")

                    shutil.copy(f"{output1Path}/questions/{unique_filename}.jpg", f"{BASE_PATH}/images/sorted/{level2}/{subject2}/long/{chapter_num}/{unique_filename}.jpg")

                    answerObject = {
                        "questionName": f"{unique_filename}.jpg",
                        "questionNum": current_question_num,
                        "Subject": subject2,
                        "Level": level2,
                        "Chapter": chapter_num,
                        "pdfName": current_file2,
                        "year": year,
                        "paperNumber": paper_num,
                        "questionText": formatted_text
                    }
                    answerObjectFormatted = json.dumps(answerObject)
                    db.write(answerObjectFormatted + ",\n")

                    unique_num += 1
                
    except Exception as e:
        print(f"Error in processing: {str(e)}")
        raise e

if __name__ == '__main__':
    print("Starting script...")
    # Initialize constants
    subject = 'chem'
    subject2 = 'chemistry'
    unique_num = 1
    
    # Create necessary directories
    output1Path = f"{BASE_PATH}/python_files/makep1/testImages"
    finalOutputPath = "final_output"
    db_path = f"{BASE_PATH}/json_files/ig_chem_theory.json"
    
    # Initialize database file
    with open(db_path, 'w') as db:
        db.write("[")
    
    print("Creating directories...")
    for dir_path in [output1Path, f"{output1Path}/final", f"{output1Path}/questions"]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
    # Select files and process them
    print("Selecting files...")
    files = select_files()
    if not files:
        print("No files selected")
        exit()
    
    print(f"Selected files: {files}")
    
    # Initialize processing variables
    manager = multiprocessing.Manager()
    heightsArr = manager.dict()
    file_question_counts = manager.dict()
    
    # Process each question paper
    for m, file_path in enumerate(files):
        print(f"\nProcessing file {m + 1}: {file_path}")
        if file_path.find("ms") == -1:
            try:
                process_question_paper(file_path, m, file_question_counts, output1Path, finalOutputPath, 
                                     subject2, heightsArr, db_path)
                print(f"Finished processing file {m + 1}")
            except Exception as e:
                print(f"Error processing file {file_path}: {str(e)}")
        else:
            pass