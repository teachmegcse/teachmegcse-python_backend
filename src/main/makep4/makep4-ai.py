from PIL import Image
import os
import json
import shutil
import sys
from pathlib import Path
import easyocr
import subprocess

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import (
    select_files,
    makeImages,
    get_level_and_chapter,
    formatText,
    strip_images,
    take_screenshot,
    merge_all_images,
    extract_paper_number,
    get_dimensions_from_api,
    cleanup,
    clean_image,
)

outputPath = f"{BASE_PATH}/resources/images/test_images"
definitionsPath = f"{BASE_PATH}/main/definitions.json"

reader = easyocr.Reader(["en"])


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
            bounding_boxes = get_dimensions_from_api(page_path, mode="long-double-p3")

            if not bounding_boxes:  # Skip if no questions found
                # Still need to account for page height!
                with Image.open(page_path) as im:
                    current_height += im.height
                continue

            # Take first box
            bounding_boxes.sort(key=lambda box: box[0])
            first_box = bounding_boxes[0]
            x1, y1 = first_box[0], first_box[1]

            # Skip based on x threshold
            if x1 > 150:
                with Image.open(page_path) as im:
                    current_height += im.height
                continue

            # Adjust coordinate
            adjusted_y = int(y1 + current_height)
            all_coordinates.append(adjusted_y)

            # Update current height based on page height
            with Image.open(page_path) as im:
                current_height += im.height

        except Exception as e:
            print(f"Error processing page {page_file}: {str(e)}")
            continue

    # Remove duplicates + sort
    all_coordinates = sorted(set(all_coordinates))
    if all_coordinates and all_coordinates[0] >= 500:
        all_coordinates.insert(0, 0)

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
    processed_db_paths = set()
    for file_path in files:
        print(f"\nProcessing file : {file_path}")
        if file_path.find("ms") == -1:
            current_file = file_path[-18:]
            print(f"Starting to process question paper: {current_file}")
            paperCode = current_file.split("_")[0]

            currentDefinitionsData = definitionsData[paperCode]
            subject = currentDefinitionsData["subjectName"]
            long_db_path = currentDefinitionsData["long_db_path"]
            db_path = f"{BASE_PATH}/resources/json/{long_db_path}"

            processed_db_paths.add(db_path)

            # Extract paper number from filename
            paper_num = extract_paper_number(current_file)
            if paper_num is None:
                print(
                    f"Could not extract paper number from {current_file}, skipping file."
                )
                continue
            if paper_num is None:
                print(
                    f"Could not extract paper number from {current_file}, skipping file."
                )
                continue

            longPapers = currentDefinitionsData["longPapers"]
            if paper_num not in longPapers:
                print(
                    f"Paper number {paper_num} not in longPapers list, skipping file."
                )
                continue
            
            # Extract year from filename (e.g., m15 -> 2015)
            year = "20" + current_file.split("_")[1][1:3]


            # Process the paper
            print("Converting PDF to images...")
            makeImages(file_path)
            # Removing periodic table page for A-level Chemistry 9701 papers
            if paperCode == "9701" and int(year) >= 2020:
                images_dir = f"{outputPath}/currentPdfImages"
                pages = [p for p in os.listdir(images_dir) if p.endswith(".jpg")]
                if pages:
                    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
                    last_page_name = pages[-1]
                    last_page_path = os.path.join(images_dir, last_page_name)
                    os.remove(last_page_path)
                    print(f"[SKIPPED] Removed last page image: {last_page_name}")
            print("Stripping images...")
            strip_images(mode="qp")

            # Get coordinates from individual pages first
            coordinates = get_all_page_coordinates()
            print(f"Got all coordinates: {coordinates}")

            # Merge images after getting coordinates
            print("Merging images...")
            merge_all_images(mode='qp')

            # Open the database file in append mode
            with open(db_path, "a") as db:
                transferred_tail = None
                # Process each question based on the adjusted coordinates
                for i in range(len(coordinates) - 1):
                    y1 = coordinates[i]
                    y2 = coordinates[i + 1]
                    current_question_num = i + 1

                    unique_filename = (
                        f"{subject}_p{paper_num}_qp_{unique_num}_{current_question_num}"
                    )
                    take_screenshot(y1, y2, unique_filename, "long", 0, mode="qp")

                    # Clean the cropped image
                    image_path = f"{outputPath}/questions/{unique_filename}.jpg"
                    if current_file[0] == "0":
                        paperType = "IGCSE"
                    else:
                        paperType = "A-level"

                    if os.path.exists(image_path):
                        current_file = current_file.replace(".pdf", "")

                        # Removes bottom 700px of Q2 and appends to Q3 for 9701 papers, to account for qualitative notes header
                        if paperCode == "9701" and paper_num == 3:
                            try:
                                image = Image.open(image_path)
                                width, height = image.size
                                if current_question_num == 2 and height > 700:
                                    transferred_tail = image.crop(
                                        (0, height - 700, width, height)
                                    )
                                    image = image.crop((0, 0, width, height - 700))
                                    image.save(image_path)
                                elif current_question_num == 3 and transferred_tail:
                                    new_height = transferred_tail.height + height
                                    combined = Image.new("RGB", (width, new_height))
                                    combined.paste(transferred_tail, (0, 0))
                                    combined.paste(image, (0, transferred_tail.height))
                                    combined.save(image_path)
                                    transferred_tail = None
                            except Exception as exc:
                                print(
                                    f"⚠️ Failed to adjust Q2/Q3 for {image_path}: {exc}"
                                )

                        if not os.path.exists(
                            f"{BASE_PATH}/resources/images/{paperType}/{subject}/long"
                        ):
                            os.makedirs(
                                f"{BASE_PATH}/resources/images/{paperType}/{subject}/long"
                            )

                        shutil.copy(
                            f"{outputPath}/questions/{unique_filename}.jpg",
                            f"{BASE_PATH}/resources/images/{paperType}/{subject}/long/{
                                unique_filename
                            }.jpg",
                        )

                        clean_image(
                            paperType, subject, "long", f"{unique_filename}.jpg", mode="qp"
                        )

                        answerObject = {
                            "questionName": f"{unique_filename}.jpg",
                            "questionNum": current_question_num,
                            "Subject": subject,
                            "Level": None,
                            "Chapter": None,
                            "pdfName": current_file,
                            "year": year,
                            "paperNumber": paper_num,
                        }
                        answerObjectFormatted = json.dumps(answerObject)
                        db.write(answerObjectFormatted + ",\n")

                        unique_num += 1

            cleanup()

            print(f"Finished processing file: {file_path}")
        else:
            pass

    # Now process parts for all questions in processed DBs
    for db_path in processed_db_paths:
        print(f"Processing parts for {db_path}...")

        with open(db_path, "r") as f:
            content = f.read()
        parts = content.split(",\n")
        questions = [json.loads(part) for part in parts if part.strip()]

        updated_questions = []

        for q in questions:
            image_filename = q.get("questionName")
            if not image_filename:
                print(f"⚠️ Skipping: no questionName")
                updated_questions.append(q)
                continue

            paper_code = q.get("pdfName", "").split("_")[0]
            paper_type = "IGCSE" if paper_code.startswith("0") else "A-level"
            subject = q["Subject"]
            IMAGES_DIR = f"{BASE_PATH}/resources/images/{paper_type}/{subject}/long"
            image_path = Path(IMAGES_DIR) / image_filename

            if not image_path.exists():
                print(f"⚠️ Image not found: {image_path}")
                updated_questions.append(q)
                continue

            print(f"Processing parts for {image_filename}...")

            parts = get_dimensions_from_api(str(image_path), mode="parts")
            parts = [[int(v) for v in box] for box in parts]
            parts_sorted = sorted(parts, key=lambda x: x[1])

            image = Image.open(image_path)
            height = image.height

            if height <= 3000:
                parts = get_dimensions_from_api(str(image_path), mode="parts")
            else:
                parts = []
                y_offset = 0
                section_idx = 0
                while y_offset < height:
                    y_end = min(y_offset + 3000, height)
                    section = image.crop((0, y_offset, image.width, y_end))
                    section_path = (
                        Path(IMAGES_DIR)
                        / f"temp_section_{image_filename}_{section_idx}.jpg"
                    )
                    section.save(section_path)
                    section_parts = get_dimensions_from_api(
                        str(section_path), mode="parts"
                    )
                    # Adjust coordinates
                    adjusted_parts = [
                        [x1, y1 + y_offset, x2, y2 + y_offset]
                        for x1, y1, x2, y2 in section_parts
                    ]
                    parts.extend(adjusted_parts)
                    os.remove(section_path)
                    y_offset = y_end
                    section_idx += 1

            parts = [[int(v) for v in box] for box in parts]
            parts_sorted = sorted(parts, key=lambda x: x[1])

            question_parts = []
            for idx, box in enumerate(parts_sorted):
                x1, y1, x2, y2 = box
                if x1 > 250:
                    continue
                cropped = image.crop((x1, y1, x2, y2))
                save_path = Path(IMAGES_DIR) / f"temp_{image_filename}_{idx}.jpg"
                cropped.save(save_path)
                part_text = reader.readtext(str(save_path))
                if part_text:
                    pieces = []
                    for entry in part_text:
                        if isinstance(entry, (list, tuple)) and len(entry) > 1:
                            pieces.append(str(entry[1]))
                        elif isinstance(entry, dict):
                            text_value = entry.get("text")
                            if text_value:
                                pieces.append(str(text_value))
                    full_text = " ".join(pieces) if pieces else "(i)"
                else:
                    full_text = "(i)"
                if "(" not in full_text and ")" not in full_text:
                    os.remove(save_path)  # cleanup temp
                    continue
                question_parts.append(
                    {"coordinates": [x1, y1, x2, y2], "text": full_text}
                )
                os.remove(save_path)  # cleanup temp

            q["questionParts"] = question_parts
            updated_questions.append(q)

        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(updated_questions, f, indent=2, ensure_ascii=False)

        print(f"✅ Parts processing complete for {db_path}")

        # Now call read_question_text to update questionText from PDFs
        print(f"Running read_question_text on {os.path.basename(db_path)}...")
        result = subprocess.run(
            ["python", "../read_question_text.py", os.path.basename(db_path)],
            cwd=os.path.dirname(__file__),  # src/main/makep4/
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ read_question_text completed successfully")
            try:
                with open(db_path, "r", encoding="utf-8") as f:
                    updated_questions = json.load(f)
            except (OSError, json.JSONDecodeError) as exc:
                print(f"❌ Failed to reload {db_path}: {exc}")
                continue

            for q in updated_questions:
                question_text = q.get("questionText", "")
                if not question_text:
                    continue

                formatted_text = formatText(question_text)
                paper_num = q.get("paperNumber")
                paper_code = q.get("pdfName", "").split("_")[0]
                if not paper_code or paper_code not in definitionsData:
                    print(f"⚠️ Missing definitions for {q.get('pdfName')}")
                    continue
                if paper_num is None:
                    print(f"⚠️ Missing paper number for {q.get('questionName')}")
                    continue
                paper_type = "IGCSE" if paper_code.startswith("0") else "A-level"
                try:
                    level, chapter_num = get_level_and_chapter(
                        formatted_text,
                        int(paper_num),
                        paper_type,
                        definitionsData[paper_code],
                    )
                except Exception as exc:
                    print(
                        f"⚠️ Chapter extraction failed for {q.get('questionName')}: {exc}"
                    )
                    continue
                q["Level"] = level
                q["Chapter"] = chapter_num

            with open(db_path, "w", encoding="utf-8") as f:
                json.dump(updated_questions, f, indent=2, ensure_ascii=False)
            print(f"✅ Chapter extraction updated for {os.path.basename(db_path)}")
        else:
            print(f"❌ read_question_text failed: {result.stderr}")
