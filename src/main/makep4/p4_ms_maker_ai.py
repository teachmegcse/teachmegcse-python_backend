import os
import json
import re
import sys
import shutil
from concurrent.futures import ThreadPoolExecutor

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import (
    select_files,
    strip_images,
    take_screenshot,
    makeImages,
    merge_all_images,
    extract_paper_number,
    cleanup,
    clean_image_file,
    make_work_dir,
    get_ms_text_coordinates,
    PDF_WORKERS,
)

output_path = f"{BASE_PATH}/resources/images/test_images"
definitionsPath = f"{BASE_PATH}/main/definitions.json"

with open(definitionsPath, "r") as db:
    definitionsData = json.load(db)


def next_ms_num(db_paths: set) -> int:
    """Returns the number to continue mark-scheme filenames from ({subject}_p{paper}_ms_{num}_{question}.jpg),
    so a new run never reuses (and overwrites) the image of a mark scheme already in one of the DBs."""
    highest = 0
    for db_path in db_paths:
        if not os.path.exists(db_path):
            continue
        with open(db_path, "r") as f:
            for record in json.load(f):
                match = re.search(r"_ms_(\d+)_\d+\.jpg$", record.get("fileName", ""))
                if match:
                    highest = max(highest, int(match.group(1)))
    return highest + 1


def split_mark_scheme(file_path: str) -> tuple[str, list] | None:
    """Splits one mark scheme into cleaned question images inside its own work_dir, so several mark schemes can be
    split at the same time. Final filenames depend on how many questions earlier mark schemes had, so they're given
    in the main thread; this returns the work_dir (to delete once the images are copied out) and
    (local image path or None if the crop failed, question number) for each question, or None if the paper isn't a long paper."""
    filename = file_path.split("/")[-1].replace(".pdf", "")
    paperCode = filename.split("_")[0]
    longPapers = definitionsData[paperCode]["longPapers"]

    paper_number = extract_paper_number(filename)
    if paper_number not in longPapers:
        print(f"Paper number {paper_number} not in longPapers list, skipping file.")
        return None

    work_dir = make_work_dir(filename)

    print(f"Processing PDF: {filename}")
    makeImages(file_path, work_dir)
    strip_images(mode="ms", work_dir=work_dir)
    # Kept in memory since final.jpg would be shared between mark schemes
    merged = merge_all_images(mode="ms", work_dir=work_dir, save=False)
    # Where each question starts, read from the PDF's text layer (the first row of the table's Question column
    # numbered with it), followed by the merged image's height
    coordinates = get_ms_text_coordinates(file_path)
    if len(coordinates) == 1:
        print(f"[WARN] {filename}: no question numbers found in the text layer")
    questions = []
    for i in range(len(coordinates) - 1):
        currentQuestionNum = i + 1
        local_filename = f"q{currentQuestionNum}"
        take_screenshot(
            coordinates[i], coordinates[i + 1], local_filename, "long", "", mode="ms", work_dir=work_dir, merged=merged
        )
        image_path = f"{work_dir}/questions/{local_filename}.jpg"
        # sometimes the screenshot fails if the size is too small or for other random reasons, this prevents a breaking error
        if os.path.exists(image_path):
            clean_image_file(image_path, mode="ms")
            questions.append((image_path, currentQuestionNum))
        else:
            questions.append((None, currentQuestionNum))
    return work_dir, questions


def process_mark_schemes(files: list) -> None:
    """Splits the selected mark schemes into question images using the PDFs' text layer and adds them to each
    subject's long_ms_db_path DB."""
    files = [file for file in files if "ms" in os.path.basename(file).lower()]
    if not files:
        print("No mark schemes selected")
        return

    target_db_paths = {
        f"{BASE_PATH}/resources/json/{definitionsData[code]['long_ms_db_path']}"
        for code in {os.path.basename(file).split("_")[0] for file in files}
        if "long_ms_db_path" in definitionsData.get(code, {})
    }
    filename_num = next_ms_num(target_db_paths)
    # Split the mark schemes in parallel, then name and save their questions in the order the files were selected
    with ThreadPoolExecutor(max_workers=PDF_WORKERS) as pool:
        for file_path, split in zip(files, pool.map(split_mark_scheme, files)):
            filename = file_path.split("/")[-1].replace(".pdf", "")
            paperCode = filename.split("_")[0]

            if filename[0] == "0":
                paperType = "IGCSE"
            else:
                paperType = "A-level"

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

            if split is None:
                continue
            work_dir, questions = split

            paper_number = extract_paper_number(filename)
            images_dir = f"{BASE_PATH}/resources/images/{paperType}/{subject}/long"
            os.makedirs(images_dir, exist_ok=True)

            for local_path, currentQuestionNum in questions:
                image_file_name = f"{subject}_p{paper_number}_ms_{filename_num}_{currentQuestionNum}"
                ms_data.append(
                    {
                        "fileName": image_file_name + ".jpg",
                        "questionNumber": currentQuestionNum,
                        "paperCode": filename,
                    }
                )
                if local_path:
                    shutil.copy(local_path, f"{images_dir}/{image_file_name}.jpg")
                filename_num += 1
            shutil.rmtree(work_dir, ignore_errors=True)

            try:
                with open(JSON_FILE_LOCATION, "w") as json_file:
                    json.dump(ms_data, json_file, indent=1)
            except Exception as e:
                print(f"Error saving JSON data: {str(e)}")
    cleanup()


if __name__ == "__main__":
    files = select_files()
    process_mark_schemes(files)
