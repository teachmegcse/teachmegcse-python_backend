import PIL
import os
import json
import shutil
import sys
# Need to add clean_images to remove whitespace at the bottom

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import (
    process_image, select_files, makeImages, get_level_and_chapter,
    formatText, strip_images, take_screenshot, merge_all_images,
    extract_paper_number, get_dimensions_from_api, cleanup
)

outputPath = f"{BASE_PATH}/resources/images/test_images"
definitionsPath = f"{BASE_PATH}/main/definitions.json"

def get_all_page_coordinates():
    print("Getting coordinates for all pages...")
    pages = os.listdir(f"{outputPath}/currentPdfImages")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    all_coordinates = []
    current_height = 0

    for page_file in pages:
        page_path = f"{outputPath}/currentPdfImages/{page_file}"

        # Get coordinates for this page
        try:
            bounding_boxes = get_dimensions_from_api(page_path)

            if not bounding_boxes:  # Skip if no questions found
                # Still need to account for page height!
                with PIL.Image.open(page_path) as im:
                    current_height += im.height
                continue

            # Take first box
            bounding_boxes.sort(key=lambda box: box[0])
            first_box = bounding_boxes[0]
            x1, y1 = first_box[0], first_box[1]

            # Skip based on x threshold
            if x1 > 150:
                with PIL.Image.open(page_path) as im:
                    current_height += im.height
                continue

            # Adjust coordinate
            adjusted_y = int(y1 + current_height)
            all_coordinates.append(adjusted_y)

            # Update current height based on page height
            with PIL.Image.open(page_path) as im:
                current_height += im.height

        except Exception as e:
            print(f"Error processing page {page_file}: {str(e)}")
            continue

    # Remove duplicates + sort
    all_coordinates = sorted(set(all_coordinates))

    # Add ending coordinate
    all_coordinates.append(current_height)

    return all_coordinates


if __name__ == "__main__":
    print("Starting script...")
    unique_num = 1

    with open(definitionsPath, "r") as db:
        definitionsData = json.load(db)

    print("Creating directories...")
    for dir_path in [outputPath, f"{outputPath}/final", f"{outputPath}/questions"]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Select files and process them
    print("Selecting files...")
    files = select_files()
    if not files:
        print("No files selected")
        exit()

    print(f"Selected files: {files}")

    # Process each question paper
    for file_path in files:
        print(f"\nProcessing file : {file_path}")
        if file_path.find("ms") == -1:
            current_file = file_path[-18:]
            print(f"Starting to process question paper: {current_file}")
            paperCode = current_file.split("_")[0]

            currentDefintionsData = definitionsData[paperCode]
            subject = currentDefintionsData["subjectName"]
            long_db_path = currentDefintionsData["long_db_path"]
            db_path = f"{BASE_PATH}/resources/json/{long_db_path}"

            # Extract paper number from filename
            paper_num = extract_paper_number(current_file)

            # Process the paper
            print("Converting PDF to images...")
            makeImages(file_path)
            print("Stripping images...")
            strip_images(mode='qp')

            # Get coordinates from individual pages first
            coordinates = get_all_page_coordinates()
            print(f"Got all coordinates: {coordinates}")

            # Merge images after getting coordinates
            print("Merging images...")
            merge_all_images()

            # Open the database file in append mode
            with open(db_path, "a") as db:
                # Process each question based on the adjusted coordinates
                for i in range(len(coordinates) - 1):
                    y1 = coordinates[i]
                    y2 = coordinates[i + 1]
                    current_question_num = i + 1

                    unique_filename = (
                        f"{subject}_p{paper_num}_qp_{unique_num}_{current_question_num}"
                    )
                    take_screenshot(
                        y1,
                        y2,
                        unique_filename,
                        'long',
                        ''
                    )

                    # Clean the cropped image
                    image_path = f"{outputPath}/questions/{unique_filename}.jpg"
                    question_text = process_image(image_path)
                    formatted_text = formatText(question_text)

                    if current_file[0] == '0':
                        paperType = 'IGCSE'
                    else:
                        paperType = 'A-level'
                    
                    if os.path.exists(image_path):
                        current_file = current_file.replace(".pdf", "")
                        
                        level, chapter_num = get_level_and_chapter(formatted_text, paper_num, paperType, currentDefintionsData)

                        if not os.path.exists(f"{BASE_PATH}/resources/images/{paperType}/{subject}/long"):
                            os.makedirs(f"{BASE_PATH}/resources/images/{paperType}/{subject}/long")

                        shutil.copy(
                            f"{outputPath}/questions/{unique_filename}.jpg",
                            f"{BASE_PATH}/resources/images/{paperType}/{subject}/long/{
                                unique_filename
                            }.jpg",
                        )

                        # Extract year from filename (e.g., m15 -> 2015)
                        year = "20" + current_file.split("_")[1][1:3]

                        answerObject = {
                            "questionName": f"{unique_filename}.jpg",
                            "questionNum": current_question_num,
                            "Subject": subject,
                            "Level": level,
                            "Chapter": chapter_num,
                            "pdfName": current_file,
                            "year": year,
                            "paperNumber": paper_num,
                            "questionText": formatted_text,
                        }
                        answerObjectFormatted = json.dumps(answerObject)
                        db.write(answerObjectFormatted + ",\n")

                        unique_num += 1

            cleanup()

            print(f"Finished processing file: {file_path}")
        else:
            pass