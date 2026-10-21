"""Splits question papers and mark schemes into question images using the PDF text layer instead of the YOLO
detection server. The functions (find_question_starts, get_text_coordinates, find_question_parts,
find_ms_question_starts, get_ms_text_coordinates, find_mcq_question_starts, get_mcq_text_coordinates,
split_question_paper_from_text, split_mark_scheme_from_text, split_mcq_paper_from_text, ...) are in main/utils.py.

Usage:
    python question_numbers.py                                    # pick the PDFs in a file dialog
    python question_numbers.py paper1.pdf paper2.pdf ... [--out DIR]

Files with "ms" in their name are mark schemes, and papers listed in mcqPapers in definitions.json are MCQ papers
(their mark schemes are skipped, makep1Final.py reads the answers from their text with extract_answers_from_pdf).

Test papers are in test_pdfs/ (git-ignored): 9701_s21_qp_43 (last question has no [Total] marker),
9701_w20_qp_41 (question 10 that YOLO misses) and 9701_m24_qp_33 (paper 3 "Qualitative analysis" heading), plus the
mark schemes 9701_s21_ms_43 and 9701_w20_ms_41.
"""
import argparse
import json
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import (
    extract_paper_number,
    select_files,
    split_mark_scheme_from_text,
    split_mcq_paper_from_text,
    split_question_paper_from_text,
)

with open(f"{BASE_PATH}/main/definitions.json", "r") as f:
    definitionsData = json.load(f)


def is_mcq_paper(pdf: str) -> bool:
    name = os.path.basename(pdf)
    return extract_paper_number(name) in definitionsData.get(name.split("_")[0], {}).get("mcqPapers", [])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split question papers and mark schemes into question images using the PDF text layer."
    )
    parser.add_argument(
        "pdfs", nargs="*",
        help="Question paper and mark scheme PDFs, mark schemes have 'ms' in their name (opens a file dialog when left out)",
    )
    parser.add_argument(
        "--out",
        default=f"{BASE_PATH}/resources/images/test_images/text_questions",
        help="Folder to save the question images to",
    )
    args = parser.parse_args()
    # Temporary: pick the PDFs in a dialog when none are given on the command line
    pdfs = args.pdfs or select_files()
    if not pdfs:
        print("No files selected")
        sys.exit()
    for pdf in pdfs:
        # Same rule as makep4-ai.py for telling mark schemes from question papers
        is_mark_scheme = "ms" in os.path.basename(pdf).lower()
        if is_mcq_paper(pdf):
            if is_mark_scheme:
                print(f"{os.path.basename(pdf)}: MCQ mark scheme, skipped")
            else:
                split_mcq_paper_from_text(pdf, args.out)
        elif is_mark_scheme:
            split_mark_scheme_from_text(pdf, args.out)
        else:
            split_question_paper_from_text(pdf, args.out)
