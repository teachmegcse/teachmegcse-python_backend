import sys
import os
import json
import re
import pdfplumber
import logging
from multiprocessing import Pool, cpu_count

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Directories (hardcoded for ig_chem; generalize later if needed)
jsondirectory = os.path.join(BASE_PATH, "resources", "json", "ig_chem_final_long.json")
MSjsonDirectory = os.path.join(BASE_PATH, "resources", "json", "ig_chem_ms.json")
QuestionJsonDirectory = os.path.join(BASE_PATH, "resources", "json", "ig_chem_theory.json")


def normalize_paper_code(code):
    """Normalize paper code by removing ms/qp and converting to lowercase."""
    return code.lower().replace("_ms_", "_").replace("_qp_", "_")


def process_entry(args):
    """Process a single entry."""
    qp_entry, ms_lookup = args

    required_qp_fields = [
        "pdfName",
        "questionNum",
        "questionName",
        "year",
        "Subject",
        "Level",
        "Chapter",
        "paperNumber",
        "questionText",
    ]

    # Skip if any required QP field is missing or None
    if any(qp_entry.get(field) is None for field in required_qp_fields):
        return None

    qp_code = normalize_paper_code(qp_entry["pdfName"])
    key = (qp_entry["questionNum"], qp_code)

    if key not in ms_lookup:
        return None

    ms_entry = ms_lookup[key]

    required_ms_fields = ["fileName", "questionNumber"]

    # Skip if any required MS field is missing or None
    if any(ms_entry.get(field) is None for field in required_ms_fields):
        return None

    return {
        "questionName": qp_entry["questionName"],
        "MSName": ms_entry["fileName"],
        "questionNumber": ms_entry["questionNumber"],
        "pdfName": qp_entry["pdfName"],
        "year": qp_entry["year"],
        "Subject": qp_entry["Subject"],
        "Level": qp_entry["Level"],
        "Chapter": qp_entry["Chapter"],
        "paperNumber": qp_entry["paperNumber"],
        "questionText": qp_entry["questionText"],
        "questionParts": qp_entry.get("questionParts", []),
    }


def check_json_validity(json_object, pdf_dir) -> json:
    # Compare answers in JSON with those in the corresponding MS PDFs
    current_pdf_name = None
    split_questions = dict()
    for record in json_object:
        qp_pdf_name = f"{record['pdfName']}.pdf"
        if qp_pdf_name != current_pdf_name:
            # Open and parse the new MS PDF
            qp_path = os.path.join(pdf_dir, qp_pdf_name)
            print(f"Reading PDF: {qp_pdf_name}")
            if not os.path.exists(qp_path):
                logging.warning(f"QP PDF not found: {qp_pdf_name}")
                current_pdf_name = qp_pdf_name
                continue
            try:
                # Crop top and bottom of each page to remove headers/footers (e.g., 60 points from top, 60 from bottom)
                question_text = ""
                with pdfplumber.open(qp_path) as pdf:
                    for page in pdf.pages:
                        if page.page_number == 1:
                            continue
                        # Crop 50pt from top only
                        width = page.width
                        height = page.height
                        cropped = page.within_bbox((0, 50, width, height))
                        question_text += cropped.extract_text() + "\n"

                # Remove dotted lines (5 or more consecutive dots)
                question_text = re.sub(r"\.{5,}", "", question_text)

                # Remove lines like "Question x starts on page y." or "Question x is on page y."
                question_text = re.sub(
                    r"Question\s+\d+\s+(starts on|is on)\s+page\s+\d+\.",
                    "",
                    question_text,
                    flags=re.IGNORECASE,
                )

                # Remove copyright lines like "© UCLES 2024" (year can vary)
                question_text = re.sub(
                    r"©\s*UCLES\s*\d{2,4}", "", question_text, flags=re.IGNORECASE
                )

                # Remove paper codes like "9700/43/M/J/24" (general format: digits/digits/letters/letters/digits)
                question_text = re.sub(
                    r"\d{4}/\d{2}/\s*[A-Z]/\s*[A-Z]/\d{2,4}",
                    "",
                    question_text,
                    flags=re.IGNORECASE,
                )

                # Remove "Turn over" with starting bracket (case-insensitive, no ending bracket)
                question_text = re.sub(
                    r"\[Turn over", "", question_text, flags=re.IGNORECASE
                )

                # Remove "blank page" (case-insensitive)
                question_text = re.sub(
                    r"blank page", "", question_text, flags=re.IGNORECASE
                )

                # Remove lines that are now empty or contain only whitespace after removing dots
                question_text = "\n".join(
                    line for line in question_text.splitlines() if line.strip()
                )

                # Extract each question block: everything from start to each "[Total: x]" (colon optional), and spaces could be there
                split_questions = []
                # Support marks like 10 or 10+
                pattern = re.compile(r'\[\s*Total\s*:?\s*\d+\+?\s*\]', re.IGNORECASE)
                start = 0
                for match in pattern.finditer(question_text):
                    block = question_text[start : match.end()]
                    split_questions.append(block.strip())
                    start = match.end()

                # Check that the number of questions in the PDF matches the number in the JSON for this paper
                num_questions_in_json = sum(
                    1 for rec in json_object if rec["pdfName"] == record["pdfName"]
                )
                num_questions_in_pdf = len(split_questions)
                if num_questions_in_json != num_questions_in_pdf:
                    if num_questions_in_json > num_questions_in_pdf:
                        logging.warning(
                            f"Mismatch in question count for {qp_pdf_name}: "
                            f"{num_questions_in_pdf} questions found in PDF, "
                            f"but {num_questions_in_json} in JSON."
                        )
                    else:
                        logging.warning(
                            f"More questions in PDF ({num_questions_in_pdf}) than in JSON ({num_questions_in_json}) for {qp_pdf_name}. Continuing..."
                        )
            except Exception as e:
                # Surface the underlying error with context so callers can handle it upstream
                raise RuntimeError(f"Error reading {qp_pdf_name}: {e}") from e
            current_pdf_name = qp_pdf_name
        # Replace the current record's questionText with our extracted question text
        qnum = record["questionNumber"]
        if qnum - 1 < len(split_questions):
            block_text = split_questions[qnum - 1]
            # Clean the text: remove non-ASCII chars and replace newlines
            block_text = block_text.encode('ascii', 'ignore').decode('ascii').replace('\n', ' ').strip()
            record["questionText"] = block_text
            # Extract the marks from the trailing [Total: X] within this block
            m = re.search(r"\[\s*Total\s*:?\s*([0-9]+\+?)\s*\]", block_text, flags=re.IGNORECASE)
            if m:
                record["marks"] = int(m.group(1))
        else:
            # The expected question index was not found in the parsed blocks
            #logging.debug(question_text)
            pass
    return json_object


def combine_and_validate_json(MSjson, QPjson, jsonDirectory):
    print("Starting JSON combination process...")

    # Load the JSON files
    print("Loading JSON files...")
    with open(MSjson, "r") as f:
        MSData = json.load(f)
    with open(QPjson, "r") as f:
        QPData = json.load(f)

    print(f"Found {len(MSData)} mark scheme entries")
    print(f"Found {len(QPData)} question paper entries")

    # Create a lookup dictionary for mark scheme data
    ms_lookup = {}
    for ms_entry in MSData:
        key = (ms_entry["questionNumber"], normalize_paper_code(ms_entry["paperCode"]))
        ms_lookup[key] = ms_entry

    # Use multiprocessing to process entries
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(
            process_entry, [(qp_entry, ms_lookup) for qp_entry in QPData]
        )

    # Filter out None results and save the combined data
    totalData = list(filter(None, results))
    print(f"Processed {len(totalData)} valid entries")

    # Now validate and update questionText from PDFs
    if totalData:
        paper_code = totalData[0]["pdfName"].split("_")[0]  # e.g., "9700"
        pdf_dir = os.path.join(BASE_PATH, "resources", "full_pdfs", paper_code)
        print(f"Validating question text from PDFs in {pdf_dir}...")
        totalData = check_json_validity(totalData, pdf_dir)

    print("Saving combined and validated data...")
    with open(jsonDirectory, "w") as totalJson:
        json.dump(totalData, totalJson, indent=1)

    print("Combination and validation complete!")


if __name__ == "__main__":
    import multiprocessing

    multiprocessing.freeze_support()  # Optional for compatibility on some systems

    combine_and_validate_json(MSjsonDirectory, QuestionJsonDirectory, jsondirectory)