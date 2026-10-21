import os
import json
import shutil
import sys
import re
import argparse
from concurrent.futures import ThreadPoolExecutor

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
    cleanup,
    clean_image_file,
    make_work_dir,
    get_text_coordinates,
    find_question_parts,
    check_json_validity,
    PDF_WORKERS,
)
from main.combine_and_validate_json import combine_and_validate_json
from p4_ms_maker_ai import process_mark_schemes

outputPath = f"{BASE_PATH}/resources/images/test_images"
definitionsPath = f"{BASE_PATH}/main/definitions.json"

with open(definitionsPath, "r") as db:
    definitionsData = json.load(db)

STEPS = ["qp", "ms", "combine"]


def load_question_db(db_path: str) -> list:
    """Reads a long-question DB. It's a JSON array, but older runs appended one record per line ("{...},\n")
    and only rewrote the file as an array at the end, so a file can also be an array followed by
    appended lines, or appended lines only. All of these are read into a single list."""
    if not os.path.exists(db_path):
        return []
    with open(db_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    records = []
    if content.startswith("["):
        array, end = json.JSONDecoder().raw_decode(content)
        records.extend(array)
        content = content[end:]
    for line in content.split(",\n"):
        line = line.strip().rstrip(",")
        if line:
            records.append(json.loads(line))
    return records


def save_question_db(db_path: str, records: list) -> None:
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


def next_unique_num(db_paths: set) -> int:
    """Returns the number to continue question filenames from ({subject}_p{paper}_qp_{unique_num}_{question}.jpg),
    so a new run never reuses (and overwrites) the image of a question already in one of the DBs."""
    highest = 0
    for db_path in db_paths:
        for record in load_question_db(db_path):
            match = re.search(r"_qp_(\d+)_\d+\.jpg$", record.get("questionName", ""))
            if match:
                highest = max(highest, int(match.group(1)))
    return highest + 1


def split_question_paper(file_path: str) -> dict:
    """Splits one question paper into cleaned question images inside its own work_dir, so several papers can be
    split at the same time. Final filenames depend on how many questions earlier papers had, so they're given
    in the main thread; this returns the local image paths and the metadata needed to name them."""
    current_file = file_path[-18:]
    print(f"Starting to process question paper: {current_file}")
    paperCode = current_file.split("_")[0]

    currentDefinitionsData = definitionsData[paperCode]
    subject = currentDefinitionsData["subjectName"]
    long_db_path = currentDefinitionsData["long_db_path"]
    db_path = f"{BASE_PATH}/resources/json/{long_db_path}"
    result = {"db_path": db_path, "questions": None}

    # Extract paper number from filename
    paper_num = extract_paper_number(current_file)
    if paper_num is None:
        print(
            f"Could not extract paper number from {current_file}, skipping file."
        )
        return result

    longPapers = currentDefinitionsData["longPapers"]
    if paper_num not in longPapers:
        print(
            f"Paper number {paper_num} not in longPapers list, skipping file."
        )
        return result

    # Extract year from filename (e.g., m15 -> 2015)
    year = "20" + current_file.split("_")[1][1:3]

    if current_file[0] == "0":
        paperType = "IGCSE"
    else:
        paperType = "A-level"

    work_dir = make_work_dir(current_file.replace(".pdf", ""))

    # Process the paper
    print(f"Converting PDF to images ({current_file})...")
    # The periodic table and other reference pages are left out by makeImages
    makeImages(file_path, work_dir)
    print(f"Stripping images ({current_file})...")
    strip_images(mode="qp", work_dir=work_dir)

    # Where each question starts, read from the PDF's text layer (a 9701 paper 3 "Qualitative analysis" heading
    # starts the question below it), and each question's parts ((a), (i), ...)
    coordinates, totals = get_text_coordinates(file_path)
    question_parts = find_question_parts(file_path)
    print(f"Got all coordinates for {current_file}: {coordinates}")
    if len(coordinates) - 1 != totals:
        print(f"[WARN] {current_file}: {len(coordinates) - 1} question numbers found, but {totals} [Total] markers")

    # Merge images after getting coordinates, kept in memory since final.jpg would be shared between papers
    print(f"Merging images ({current_file})...")
    merged = merge_all_images(mode="qp", work_dir=work_dir, save=False)

    questions = []
    # Process each question based on the adjusted coordinates
    for i in range(len(coordinates) - 1):
        y1 = coordinates[i]
        y2 = coordinates[i + 1]
        current_question_num = i + 1

        local_filename = f"q{current_question_num}"
        take_screenshot(
            y1, y2, local_filename, "long", 0, mode="qp", work_dir=work_dir, merged=merged
        )

        # Clean the cropped image
        image_path = f"{work_dir}/questions/{local_filename}.jpg"

        if os.path.exists(image_path):
            clean_image_file(image_path, mode="qp")
            questions.append({
                "image_path": image_path,
                "questionNum": current_question_num,
                "questionParts": question_parts[i],
            })

    print(f"Finished processing file: {file_path}")
    result.update(
        questions=questions,
        subject=subject,
        paperType=paperType,
        pdfName=current_file.replace(".pdf", ""),
        year=year,
        paperNumber=paper_num,
    )
    return result


def process_question_papers(files: list) -> None:
    """Splits the selected question papers into question images (with their parts) using the PDFs' text layer, adds
    them to each subject's long_db_path DB, then fills in their text, marks, level and chapter (see fill_question_text).
    Only the papers split now are read; the questions already in the DBs keep theirs."""
    for dir_path in [outputPath, f"{outputPath}/final", f"{outputPath}/questions"]:
        os.makedirs(dir_path, exist_ok=True)

    # Split the question papers in parallel, then name and save their questions in the order the files were selected
    processed_db_paths = set()
    # The papers split in this run, whose questions need their text, marks, level and chapter
    new_pdf_names = set()
    qp_files = [file_path for file_path in files if "ms" not in os.path.basename(file_path).lower()]
    if not qp_files:
        print("No question papers selected")
        return
    target_db_paths = {
        f"{BASE_PATH}/resources/json/{definitionsData[code]['long_db_path']}"
        for code in {file_path[-18:].split("_")[0] for file_path in qp_files}
        if code in definitionsData
    }
    unique_num = next_unique_num(target_db_paths)
    with ThreadPoolExecutor(max_workers=PDF_WORKERS) as pool:
        for result in pool.map(split_question_paper, qp_files):
            db_path = result["db_path"]
            processed_db_paths.add(db_path)
            if result["questions"] is None:
                continue

            subject = result["subject"]
            paper_num = result["paperNumber"]
            new_pdf_names.add(result["pdfName"])
            images_dir = f"{BASE_PATH}/resources/images/{result['paperType']}/{subject}/long"
            os.makedirs(images_dir, exist_ok=True)

            # Add this paper's questions to the database, saved after every paper so a crash loses at most one paper
            db_records = load_question_db(db_path)
            for question in result["questions"]:
                current_question_num = question["questionNum"]
                unique_filename = (
                    f"{subject}_p{paper_num}_qp_{unique_num}_{current_question_num}"
                )
                shutil.copy(question["image_path"], f"{images_dir}/{unique_filename}.jpg")

                answerObject = {
                    "questionName": f"{unique_filename}.jpg",
                    "questionNum": current_question_num,
                    "Subject": subject,
                    "Level": None,
                    "Chapter": None,
                    "pdfName": result["pdfName"],
                    "year": result["year"],
                    "paperNumber": paper_num,
                    "questionParts": question["questionParts"],
                }
                db_records.append(answerObject)

                unique_num += 1
            save_question_db(db_path, db_records)

    for db_path in processed_db_paths:
        fill_question_text(db_path, new_pdf_names)


def fill_question_text(db_path: str, pdf_names: set | None = None) -> None:
    """Fills in the text and marks of a long-question DB's questions from their question papers, then their level and
    chapter from the text. Only the questions of pdf_names are read, or all of them when it's None (e.g. after a
    change to how question text is read)."""
    all_questions = load_question_db(db_path)
    updated_questions = [q for q in all_questions if pdf_names is None or q.get("pdfName") in pdf_names]
    print(f"Reading question text for {len(updated_questions)} questions in {os.path.basename(db_path)}...")
    if updated_questions:
        paper_code = updated_questions[0]["pdfName"].split("_")[0]
        # check_json_validity updates the records in place, so all_questions gets the new values too
        check_json_validity(updated_questions, f"{BASE_PATH}/resources/full_pdfs/{paper_code}")

        for q in updated_questions:
            question_text = q.get("questionText", "")
            if not question_text:
                continue

            formatted_text = formatText(question_text)
            paper_num = q.get("paperNumber")
            paper_code = q.get("pdfName", "").split("_")[0]
            if not paper_code or paper_code not in definitionsData:
                print(f"[WARN] Missing definitions for {q.get('pdfName')}")
                continue
            if paper_num is None:
                print(f"[WARN] Missing paper number for {q.get('questionName')}")
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
                    f"[WARN] Chapter extraction failed for {q.get('questionName')}: {exc}"
                )
                continue
            q["Level"] = level
            q["Chapter"] = chapter_num

        save_question_db(db_path, all_questions)
        print(f"[DONE] Question text and chapters updated for {os.path.basename(db_path)}")


def combine_paper_codes(paper_codes: set) -> None:
    """Pairs each subject's questions with their mark schemes, writing the subject's long_final_db_path DB."""
    for code in sorted(paper_codes):
        definitions = definitionsData.get(code, {})
        if not all(key in definitions for key in ["long_db_path", "long_ms_db_path", "long_final_db_path"]):
            print(f"[WARN] {code} has no long_db_path/long_ms_db_path/long_final_db_path in definitions.json, skipping combine.")
            continue
        json_dir = f"{BASE_PATH}/resources/json"
        print(f"Combining {definitions['long_db_path']} + {definitions['long_ms_db_path']} -> {definitions['long_final_db_path']}")
        combine_and_validate_json(
            f"{json_dir}/{definitions['long_ms_db_path']}",
            f"{json_dir}/{definitions['long_db_path']}",
            f"{json_dir}/{definitions['long_final_db_path']}",
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Long-answer pipeline: split question papers (qp), split mark schemes (ms), then pair them into "
        "the final DB (combine). Select the question papers and their mark schemes together."
    )
    parser.add_argument(
        "--steps",
        default=",".join(STEPS),
        help="Comma-separated steps to run, e.g. --steps qp to only split question papers (default: qp,ms,combine)",
    )
    parser.add_argument(
        "--refresh-text",
        action="store_true",
        help="Read the text, marks, level and chapter of every question already in the long-question DBs of the "
        "selected files' subjects again (e.g. after a change to how question text is read), before the combine step. "
        "Can be used with --steps combine to refresh without splitting anything",
    )
    args = parser.parse_args()
    steps = [step.strip() for step in args.steps.split(",") if step.strip()]
    unknown = [step for step in steps if step not in STEPS]
    if unknown:
        parser.error(f"Unknown steps {unknown}, choose from {STEPS}")
    print(f"Running steps: {', '.join(steps)}")

    print("Selecting files...")
    files = select_files()
    if not files:
        print("No files selected")
        exit()
    print(f"Selected files: {files}")

    if "qp" in steps:
        process_question_papers(files)
    if "ms" in steps:
        process_mark_schemes(files)
    if args.refresh_text:
        for code in sorted({os.path.basename(file).split("_")[0] for file in files}):
            if "long_db_path" in definitionsData.get(code, {}):
                fill_question_text(f"{BASE_PATH}/resources/json/{definitionsData[code]['long_db_path']}")
    if "combine" in steps:
        combine_paper_codes({os.path.basename(file).split("_")[0] for file in files})
