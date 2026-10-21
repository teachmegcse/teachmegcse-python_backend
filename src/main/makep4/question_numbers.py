"""Finds where each question starts from a question paper's text layer instead of the YOLO detection server, and
splits the paper into question images with the same page handling as makep4-ai.py (makeImages -> strip_images ->
merge_all_images -> take_screenshot -> clean_image_file).

Question numbers are printed in the left margin at a fixed size, so they're found by looking for the numbers
1, 2, 3, ... in order at that position. The number of "[Total: N]" markers in the paper is used as a cross-check.

Usage:
    python question_numbers.py                                    # pick the PDFs in a file dialog
    python question_numbers.py paper1.pdf paper2.pdf ... [--out DIR]

Test papers are in test_pdfs/ (git-ignored): 9701_s21_qp_43 (last question has no [Total] marker),
9701_w20_qp_41 (question 10 that YOLO misses) and 9701_m24_qp_33 (paper 3 "Qualitative analysis" heading).
"""
import argparse
import os
import re
import shutil
import sys

import pypdfium2 as pdfium

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import (
    page_skip_reason,
    makeImages,
    strip_images,
    merge_all_images,
    take_screenshot,
    clean_image_file,
    make_work_dir,
    select_files,
)

TOTAL = re.compile(r"\[\s*Total\s*:?\s*\d+\+?\s*\]", re.I)
# Question numbers start 45-56pt from the left edge and are 7-9.5pt tall (graph axis labels etc. are smaller)
NUMBER_X_RANGE = (45, 56)
NUMBER_HEIGHT_RANGE = (7, 9.5)
# 9701 paper 3: the "Qualitative analysis" instructions above a question's number belong to that question
SECTION_HEADINGS = ["Qualitative analysis"]

# Must match how makeImages (pdf2image's default 200 DPI) and strip_images ("qp": y 150 to 2200) make the pages
SCALE = 200 / 72
STRIP_TOP, STRIP_BOTTOM = 150, 2200
# Space left above the question number, about the margin YOLO's boxes have above it
PADDING_PX = 14


def _numbers(textpage) -> list:
    """Groups consecutive digits on the same line into numbers, returning (text, [left, bottom, right, top])
    in PDF points (origin at the bottom left of the page)."""
    numbers, current, box = [], "", None
    for i in range(textpage.count_chars()):
        char = textpage.get_text_range(i, 1)
        left, bottom, right, top = textpage.get_charbox(i)
        if char.isdigit() and current and 0 <= left - box[2] < 3 and abs(bottom - box[1]) < 2:
            current += char
            box = [box[0], bottom, right, top]
        else:
            if current:
                numbers.append((current, box))
            current, box = (char, [left, bottom, right, top]) if char.isdigit() else ("", None)
    if current:
        numbers.append((current, box))
    return numbers


def find_question_starts(pdf_path: str) -> tuple[list, int]:
    """Finds the question numbers 1, 2, 3, ... in a question paper.

    Args:
    pdf_path (str): The path to the question paper.

    Returns:
        tuple[list, int]: [(page_index, y), ...] where y is how far the question starts from the top of the page
          in points, one per question in order, and the number of "[Total: N]" markers in the paper.
          The first page and pages left out by makeImages (see page_skip_reason) are never used.
    """
    document = pdfium.PdfDocument(pdf_path)
    starts, expected, totals = [], 1, 0
    try:
        for page_index in range(1, len(document)):
            page = document[page_index]
            textpage = page.get_textpage()
            text = textpage.get_text_range()
            totals += len(TOTAL.findall(text))
            if page_skip_reason(text):
                continue
            page_height = page.get_size()[1]

            headings = []
            for heading in SECTION_HEADINGS:
                searcher = textpage.search(heading, match_case=True)
                while (match := searcher.get_next()) is not None:
                    headings.append(page_height - textpage.get_charbox(match[0])[3])

            previous_y = 0
            for number, (left, bottom, right, top) in sorted(_numbers(textpage), key=lambda n: -n[1][3]):
                if not (NUMBER_X_RANGE[0] <= left <= NUMBER_X_RANGE[1]):
                    continue
                if not (NUMBER_HEIGHT_RANGE[0] <= top - bottom <= NUMBER_HEIGHT_RANGE[1]):
                    continue
                if int(number) != expected:
                    continue
                y = page_height - top
                # Start at a section heading between the previous question on this page and this number
                above = [h for h in headings if previous_y <= h < y]
                starts.append((page_index, min(above) if above else y))
                previous_y = y
                expected += 1
    finally:
        document.close()
    return starts, totals


def get_text_coordinates(pdf_path: str) -> tuple[list, int]:
    """Same output as get_all_page_coordinates in makep4-ai.py, but from the text layer: the y coordinate of each
    question's start in the merged image of the stripped pages, followed by the merged image's height.

    Returns:
        tuple[list, int]: The coordinates, and the number of "[Total: N]" markers to check the question count against.
    """
    starts, totals = find_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        # Where each page kept by makeImages starts in the merged image
        page_offsets, current_height = {}, 0
        for page_index in range(1, len(document)):
            page = document[page_index]
            if page_skip_reason(page.get_textpage().get_text_range()):
                continue
            page_offsets[page_index] = current_height
            rendered_height = round(page.get_size()[1] * SCALE)
            current_height += min(STRIP_BOTTOM, rendered_height) - STRIP_TOP
    finally:
        document.close()

    coordinates = [
        page_offsets[page_index] + max(0, int(y * SCALE) - STRIP_TOP - PADDING_PX) for page_index, y in starts
    ]
    coordinates.append(current_height)
    return coordinates, totals


def split_question_paper_from_text(pdf_path: str, out_dir: str) -> list:
    """Splits a question paper into one cleaned image per question, saved as <pdf name>_q<number>.jpg in out_dir.

    Returns:
        list: The paths of the saved question images, in question order.
    """
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    coordinates, totals = get_text_coordinates(pdf_path)
    question_count = len(coordinates) - 1
    if question_count == 0:
        print(f"[WARN] {pdf_name}: no question numbers found in the text layer")
        return []
    if question_count != totals:
        print(f"[WARN] {pdf_name}: {question_count} question numbers found, but {totals} [Total] markers")

    work_dir = make_work_dir(f"text-{pdf_name}")
    makeImages(pdf_path, work_dir)
    strip_images(mode="qp", work_dir=work_dir)
    merged = merge_all_images(mode="qp", work_dir=work_dir, save=False)

    os.makedirs(out_dir, exist_ok=True)
    saved = []
    for i in range(question_count):
        local_filename = f"q{i + 1}"
        if not take_screenshot(
            coordinates[i], coordinates[i + 1], local_filename, "long", 0, mode="qp", work_dir=work_dir, merged=merged
        ):
            continue
        image_path = f"{work_dir}/questions/{local_filename}.jpg"
        clean_image_file(image_path, mode="qp")
        destination = f"{out_dir}/{pdf_name}_q{i + 1}.jpg"
        shutil.copy(image_path, destination)
        saved.append(destination)
    shutil.rmtree(work_dir, ignore_errors=True)
    print(f"{pdf_name}: saved {len(saved)} questions to {out_dir}")
    return saved


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split question papers into question images using the PDF text layer.")
    parser.add_argument("pdfs", nargs="*", help="Question paper PDFs (opens a file dialog when left out)")
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
        split_question_paper_from_text(pdf, args.out)
