from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import json
from p4_ms_maker import make_question_ms
import multiprocessing

def select_files():
    root = Tk()
    filetypes = [("PDF Files", "*.pdf")]
    files = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    return list(files)

def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin")
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(2, number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        if x >= 2:
            if page.extract_text().find("BLANK PAGE") == -1:
                images[x].save(f"{output_path}/{i}/{x}.jpg", 'JPEG')

def strip_images(folder_num, output_path):
    pages = os.listdir(f"{output_path}/{folder_num}")
    for i in range(len(pages)):
        with PIL.Image.open(f"{output_path}/{folder_num}/{pages[i]}") as im:
            im_crop = im.crop((0, 180, 1654, 2200))
            im_crop.save(f"{output_path}/{folder_num}/{pages[i]}")

def merge_all_images(folder_num, output_path, heightsArr):
    pages = os.listdir(f"{output_path}/{folder_num}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    height = (len(pages) - 1) * (2200 - 180)
    dst = PIL.Image.new('RGB', (1654, height), color='black')
    current_height = 0
    for i in range(1, len(pages)):
        image_path = f"{output_path}/{folder_num}/{pages[i]}"
        image = PIL.Image.open(image_path)
        dst.paste(image, (0, current_height, 1654, current_height + (2200 - 180)), mask=None)
        current_height += (2200 - 180)
    dst.save(f"{output_path}/final/final{folder_num}.jpg")
    heightsArr[folder_num] = current_height

def get_dimensions(current_page, prev_pixel, stop_value, output_path):
    im = PIL.Image.open(f"{output_path}/final/{current_page}")
    pix = im.load()
    found = False
    i = 80
    while not found and (prev_pixel + i <= stop_value):
        value = pix[147, prev_pixel + i]
        if value != (255, 255, 255):
            found = True
        else:
            i += 2
    return (prev_pixel + i) - 30

def take_screenshot(y1, y2, current_question_num, file_name, output_path, subject, unique_filename):
    if (y2 - y1) > 300:
        with PIL.Image.open(f"{output_path}/final/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output_path}/questions/{unique_filename}.jpg")

def clean_single_image(input_path, output_path):
    with PIL.Image.open(input_path) as im:
        pix = im.load()
        y = im.height - 2
        
        # Find the actual content bottom
        for curr_y in range(im.height - 2, 1, -2):
            found_content = False
            for x in range(im.width - 2, 1, -2):
                if pix[x, curr_y] != (255, 255, 255):
                    y = curr_y
                    found_content = True
                    break
            if found_content:
                break
        
        # Crop and save
        cleaned_image = im.crop((0, 0, 1500, y))
        cleaned_image.save(output_path)

def process_question_paper(file_path, m, file_question_counts, output1Path, finalOutputPath, subject, subject2, level2, paperNumber, heightsArr, db_path):
    current_file = file_path[-18:]
    file_question_counts[current_file] = 0
    
    # Extract paper number from filename
    paper_num = extract_paper_number(current_file)
    if paper_num is None:
        paper_num = paperNumber  # fallback to passed parameter
    
    # Clear the questions directory before processing new file
    questions_dir = f"{output1Path}/questions"
    if os.path.exists(questions_dir):
        for f in os.listdir(questions_dir):
            os.remove(os.path.join(questions_dir, f))
    
    makeImages(output1Path, file_path, m)
    strip_images(m, output1Path)
    merge_all_images(m, output1Path, heightsArr)

    current_y = 0
    stop_value = heightsArr[m] - 2
    question_count = 0
    
    # Open the database file in append mode
    with open(db_path, 'a') as db:
        while current_y <= stop_value:
            end_y = get_dimensions(f"final{m}.jpg", current_y, stop_value, output1Path)
            
            # Only process if there's enough height for a question
            if (end_y - current_y) > 300:
                question_count += 1
                unique_filename = f"{subject}_{m+1}_{question_count}"
                
                # Take screenshot and save with unique filename
                take_screenshot(current_y, end_y, question_count, f"final{m}.jpg", output1Path, subject, unique_filename)
                
                # Check if the question file exists and process it
                temp_path = f"{output1Path}/questions/{unique_filename}.jpg"
                final_path = f"{finalOutputPath}/{level2}/{subject2}/p{paperNumber}/{unique_filename}.jpg"
                
                if os.path.isfile(temp_path):
                    # Move the file to final location
                    if os.path.exists(final_path):
                        os.remove(final_path)  # Remove if exists to avoid conflicts
                    
                    # Clean and save the image
                    clean_single_image(temp_path, final_path)
                    
                    # Extract year from filename (e.g., m15 -> 2015)
                    year = "20" + current_file.split("_")[1][1:3]
                    
                    answerObject = {
                        "questionName": f"{unique_filename}.jpg",
                        "questionNum": question_count,
                        "Subject": subject2,
                        "Level": level2,
                        "pdfName": current_file,
                        "year": year,
                        "paperNumber": paper_num
                    }
                    answerObjectFormatted = json.dumps(answerObject)
                    db.write(answerObjectFormatted + ",\n")
            
            current_y = end_y

def process_mark_scheme(ms_filename, subject_name, subject_code):
    make_question_ms(ms_filename, subject_name, subject_code)

def extract_paper_number(filename):
    # Extract paper number from filename (e.g., from '9702_s22_qp_41.pdf' get 4)
    try:
        paper_variant = filename.split('_')[-1].split('.')[0]  # gets '41'
        paper_number = int(paper_variant[0])     # gets 4
        return paper_number
    except:
        return None

if __name__ == '__main__':
    # Initialize constants
    subject = 'phy'
    subject2 = 'physics'
    level = 'A2'
    level2 = 'A-level'
    output1Path = r"D:\python_projects\teachmegcse\python_files\makep1\testImages"
    finalOutputPath = r"D:\python_projects\teachmegcse\images\unsorted"
    heightsArr = [0 for _ in range(100)]
    db_path = f"D:\\python_projects\\teachmegcse\\json_files\\{subject}_db_theory.json"
    
    # Initialize database files
    with open(db_path, 'w') as db:
        db.write("[")
    
    with open(f"D:\\python_projects\\teachmegcse\\json_files\\{subject}_db_ms_theory.json", 'w') as ms_db:
        ms_db.write("[]")
    
    # Get files from user
    files = select_files()
    
    # Dictionary to keep track of question numbers per file
    file_question_counts = multiprocessing.Manager().dict()
    
    for m in range(len(files)):
        current_file = files[m][-18:]
        paper_number = extract_paper_number(current_file)
        if paper_number is None:
            print(f"Warning: Could not extract paper number from {current_file}, skipping...")
            continue
        
        # Create processes for both question paper and mark scheme
        qp_process = multiprocessing.Process(
            target=process_question_paper,
            args=(files[m], m, file_question_counts, output1Path, finalOutputPath, 
                  subject, subject2, level2, paper_number, heightsArr, db_path)
        )
        
        ms_process = multiprocessing.Process(
            target=process_mark_scheme,
            args=(files[m][-18:].replace('qp', 'ms'), subject2, 9702)
        )
        
        # Start both processes
        qp_process.start()
        ms_process.start()
        
        # Wait for both processes to complete before moving to next file
        qp_process.join()
        ms_process.join()
    
    # Finalize the database file
    with open(db_path, 'rb+') as db:
        db.seek(0, 2)  # Go to end of file
        db.write(b']')