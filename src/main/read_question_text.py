import sys
import json
import os
import re
import pdfplumber
import logging
from concurrent.futures import ProcessPoolExecutor


def extract_question_blocks(qp_path: str) -> list:
    """Reads a question paper and splits its text into one block per question (each ending at its [Total: x])."""
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

        # Some PDFs have control characters (mostly \x07) where spaces should be. Replace them before splitting,
        # as they also stop "[Total:\x0715]" from matching, which merged that question with the next one
        question_text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", " ", question_text)

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
        pattern = re.compile(r"\[\s*Total\s*:?\s*\d+\+?\s*\]", re.IGNORECASE)
        start = 0
        for match in pattern.finditer(question_text):
            block = question_text[start : match.end()]
            split_questions.append(block.strip())
            start = match.end()
        return split_questions
    except Exception as e:
        # Surface the underlying error with context so callers can handle it upstream
        raise RuntimeError(f"Error reading {os.path.basename(qp_path)}: {e}") from e


def check_json_validity(json_object, pdf_dir) -> json:
    # Read every question paper up front, in separate processes since pdfplumber is slow pure Python
    # (threads wouldn't run it any faster)
    pdf_names = list(dict.fromkeys(f"{record['pdfName']}.pdf" for record in json_object))
    found = [name for name in pdf_names if os.path.exists(os.path.join(pdf_dir, name))]
    blocks_by_pdf = {}
    if found:
        with ProcessPoolExecutor(max_workers=min(os.cpu_count() or 1, len(found))) as pool:
            paths = [os.path.join(pdf_dir, name) for name in found]
            blocks_by_pdf = dict(zip(found, pool.map(extract_question_blocks, paths)))

    current_pdf_name = None
    split_questions = []
    for record in json_object:
        qp_pdf_name = f"{record['pdfName']}.pdf"
        if qp_pdf_name != current_pdf_name:
            print(f"Reading PDF: {qp_pdf_name}")
            current_pdf_name = qp_pdf_name
            if qp_pdf_name not in blocks_by_pdf:
                logging.warning(f"QP PDF not found: {qp_pdf_name}")
                split_questions = []
                continue
            split_questions = blocks_by_pdf[qp_pdf_name]

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
        # Replace the current record's questionText with our extracted question text
        qnum = record["questionNum"]
        if qnum - 1 < len(split_questions):
            block_text = split_questions[qnum - 1]
            # Clean the text: remove non-ASCII chars and replace newlines
            block_text = re.sub(r"\(cid:\d+\)", "", block_text)
            block_text = re.sub(
                r"AM SIHT NI ETIRW TON OD NIGRAM", "", block_text, flags=re.IGNORECASE
            )
            block_text = re.sub(r"\b[A-Z][A-Z\s]{3,}\b", "", block_text)
            block_text = (
                block_text.encode("ascii", "ignore")
                .decode("ascii")
                .replace("\n", " ")
                .strip()
            )
            block_text = re.sub(r" {2,}", " ", block_text)
            record["questionText"] = block_text
            # Extract the marks from the trailing [Total: X] within this block
            m = re.search(
                r"\[\s*Total\s*:?\s*([0-9]+\+?)\s*\]", block_text, flags=re.IGNORECASE
            )
            if m:
                record["marks"] = int(m.group(1))
        else:
            # The expected question index was not found in the parsed blocks
            # logging.debug(question_text)
            pass
    return json_object


def main():
    # Make JSON path location independent (relative to this script)
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) < 2:
        print("Usage: python check_json_validity.py <json_file>")
        sys.exit(1)
    # Configure logging to file in the current working directory
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(
                os.path.join(os.getcwd(), f"{sys.argv[1]}.log"),
                mode="w",
                encoding="utf-8",
            ),
            logging.StreamHandler(),
        ],
    )
    logging.captureWarnings(True)
    json_name = sys.argv[1]
    json_file = os.path.join(SCRIPT_DIR, "..", "resources", "json", json_name)
    with open(json_file, "r") as f:
        json_object = json.load(f)
    pdf_directory = os.path.join(
        SCRIPT_DIR,
        "..",
        "resources",
        "full_pdfs",
        json_object[0]["pdfName"].split("_")[0],
    )
    new_json = check_json_validity(json_object, pdf_directory)
    with open(json_file, "w") as f:
        json.dump(new_json, f, indent=2)


if __name__ == "__main__":
    main()
