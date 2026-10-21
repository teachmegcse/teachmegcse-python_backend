"""Finds where each question starts from a question paper's text layer instead of the YOLO detection server, and
splits the paper into question images with the same page handling as makep4-ai.py (makeImages -> strip_images ->
merge_all_images -> take_screenshot -> clean_image_file).

Question numbers are printed in the left margin at a fixed size, so they're found by looking for the numbers
1, 2, 3, ... in order at that position. The number of "[Total: N]" markers in the paper is used as a cross-check.

Mark schemes have their own functions (find_ms_question_starts, get_ms_text_coordinates, split_mark_scheme_from_text),
matching split_mark_scheme in p4_ms_maker_ai.py: each question starts at the first row of the table's Question
column numbered with it ("2", "2(a)", "2(a)(i)", ...).

Usage:
    python question_numbers.py                                    # pick the PDFs in a file dialog
    python question_numbers.py paper1.pdf paper2.pdf ... [--out DIR]   # files with "ms" in their name are mark schemes

Test papers are in test_pdfs/ (git-ignored): 9701_s21_qp_43 (last question has no [Total] marker),
9701_w20_qp_41 (question 10 that YOLO misses) and 9701_m24_qp_33 (paper 3 "Qualitative analysis" heading), plus the
mark schemes 9701_s21_ms_43 and 9701_w20_ms_41.
"""
import argparse
import json
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
# Question numbers line up with the "© UCLES" footer (0.1-0.9pt to its right, the footer is usually 49.6pt from the
# left edge but some papers have a wider margin) and are 7-9.5pt tall (graph axis labels etc. are smaller)
DEFAULT_FOOTER_X = 49.6
NUMBER_X_FROM_FOOTER = (-1.5, 2.5)
NUMBER_HEIGHT_RANGE = (7, 9.5)
# How far left of the footer to look for text before a question number on its line. Papers from 2024 have a vertical
# "DO NOT WRITE IN THIS MARGIN" strip about 40pt left of the footer, which isn't part of the line
NUMBER_LINE_LOOKBACK = 25
# A question number at the top of a page is accepted further right, as a few pages are typeset indented
# (e.g. 0610 w20 42 Q3)
TOP_OF_PAGE_Y = (58, 70)
TOP_OF_PAGE_MAX_X = 120
# 9701 paper 3: the "Qualitative analysis" instructions above a question's number belong to that question
SECTION_HEADINGS = ["Qualitative analysis"]

# Must match how makeImages (pdf2image's default 200 DPI) and strip_images ("qp": y 150 to 2200) make the pages
SCALE = 200 / 72
STRIP_TOP, STRIP_BOTTOM = 150, 2200
# Space left above the question number, about the margin YOLO's boxes have above it
PADDING_PX = 14
# take_screenshot crops question images from x = 100
CROP_LEFT = 100

# Part labels: letters start 63-76pt from the left edge (usually 71-73), roman numerals (right-aligned) 80-100pt, so "(i)" in the
# letter column is the letter after (h). Inline references like "... in (b)(i)." in the instructions start further right
PART_LABEL = re.compile(r"\(([a-z]{1,4})\)")
PART_LETTERS = set("abcdefghijk")
ROMAN_NUMERALS = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}
LETTER_X_RANGE = (63, 76)
ROMAN_X_RANGE = (80, 100)
# Margin around a part label's box
PART_PADDING_PX = 6
# Wider than any page, to read the whole line a label is on
KEY_LINE_WIDTH = 2000

# Mark schemes: question numbers like "1", "1(a)" or "10(b)(ii)" start the rows of the table's Question column.
# Must match how strip_images ("ms": y 200 to 1500) and split_mark_scheme in p4_ms_maker_ai.py stack the pages
MS_STRIP_TOP, MS_PAGE_HEIGHT = 200, 1300
# Question numbers start 0-20pt right of the "Question" header's left edge, the Answer
# column's text (including numbered marking points like "1 globular protein ;") starts 55pt or more right of it
MS_COLUMN_FROM_HEADER = (-10, 35)
# Used when a mark scheme has no "Question" header at all (in points from the left of the displayed page)
MS_DEFAULT_COLUMN = (50, 100)
# Some mark schemes start a new table (with its own header row) for each question. A question whose first row is
# directly under a header starts at the header instead, so the header isn't left at the bottom of the previous
# question's image (in points between the header's text and the row's text)
MS_HEADER_GAP = 40
# How close (in points) characters must be to count as one number ("10"), and how far left of the Question column
# to look for text that would mean a number isn't the first thing on its line
MS_DIGIT_GAP = 4
MS_LINE_LOOKBACK = 30


def _numbers(textpage) -> list:
    """Groups consecutive digits on the same line into numbers, returning (text, [left, bottom, right, top], next)
    in PDF points (origin at the bottom left of the page), where next is the character after the number."""
    numbers, current, box = [], "", None
    for i in range(textpage.count_chars()):
        char = textpage.get_text_range(i, 1)
        left, bottom, right, top = textpage.get_charbox(i)
        if char.isdigit() and current and 0 <= left - box[2] < 3 and abs(bottom - box[1]) < 2:
            current += char
            box = [box[0], bottom, right, top]
        else:
            if current:
                numbers.append((current, box, char))
            current, box = (char, [left, bottom, right, top]) if char.isdigit() else ("", None)
    if current:
        numbers.append((current, box, ""))
    return numbers


def _footer_x(textpage) -> float:
    """Returns how far the "© UCLES" footer is from the left edge of the page (DEFAULT_FOOTER_X when there's none)."""
    footer = textpage.search("UCLES").get_next()
    # The © is two characters before the match
    if footer and footer[0] >= 2:
        return textpage.get_charbox(footer[0] - 2)[0]
    return DEFAULT_FOOTER_X


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

            footer_x = _footer_x(textpage)

            previous_y = 0
            for number, (left, bottom, right, top), next_char in sorted(_numbers(textpage), key=lambda n: -n[1][3]):
                in_column = NUMBER_X_FROM_FOOTER[0] <= left - footer_x <= NUMBER_X_FROM_FOOTER[1]
                at_top_of_page = TOP_OF_PAGE_Y[0] <= page_height - top <= TOP_OF_PAGE_Y[1] and left <= TOP_OF_PAGE_MAX_X
                if not (in_column or at_top_of_page):
                    continue
                # Nothing before it on its line, so the "2" of "Step 2" or "Fig. 1.2" isn't taken for a question
                if textpage.get_text_bounded(max(0, footer_x - NUMBER_LINE_LOOKBACK), bottom + 1, left - 0.5, top - 1).strip():
                    continue
                # Numbered method steps in practical papers ("2. Label 3 test-tubes ...") are in the same column
                if next_char == ".":
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


def _page_offsets(document) -> tuple[dict, int]:
    """Returns where each page kept by makeImages starts in the merged image of the stripped pages
    ({page_index: y}), and the merged image's height."""
    page_offsets, current_height = {}, 0
    for page_index in range(1, len(document)):
        page = document[page_index]
        if page_skip_reason(page.get_textpage().get_text_range()):
            continue
        page_offsets[page_index] = current_height
        rendered_height = round(page.get_size()[1] * SCALE)
        current_height += min(STRIP_BOTTOM, rendered_height) - STRIP_TOP
    return page_offsets, current_height


def get_text_coordinates(pdf_path: str) -> tuple[list, int]:
    """Same output as get_all_page_coordinates in makep4-ai.py, but from the text layer: the y coordinate of each
    question's start in the merged image of the stripped pages, followed by the merged image's height.

    Returns:
        tuple[list, int]: The coordinates, and the number of "[Total: N]" markers to check the question count against.
    """
    starts, totals = find_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        page_offsets, merged_height = _page_offsets(document)
    finally:
        document.close()

    coordinates = [
        page_offsets[page_index] + max(0, int(y * SCALE) - STRIP_TOP - PADDING_PX) for page_index, y in starts
    ]
    coordinates.append(merged_height)
    return coordinates, totals


def _part_labels(textpage, page_height: float) -> list:
    """Finds the part labels on a page: letters like "(a)" and roman numerals like "(ii)" at the left margin.
    "(b)(i)" gives two labels. Returns (top, bottom, left, right, text) for each, with y from the top of the page
    in points."""
    labels = []
    # Papers with a wider margin have their part columns shifted by the same amount as the footer
    shift = _footer_x(textpage) - DEFAULT_FOOTER_X
    # Index of the last character of the previous label kept, so the "(i)" of "(b)(i)" is kept too
    previous_label_end = None
    for i in range(textpage.count_chars()):
        if textpage.get_text_range(i, 1) != "(":
            continue
        match = PART_LABEL.match(textpage.get_text_range(i, 7))
        if not match:
            continue
        # A label starts its line, or follows another label. This leaves out references like "3(b)(i)" or "in (b)(i)."
        before = textpage.get_text_range(i - 1, 1) if i > 0 else ""
        if before.strip() and previous_label_end != i - 1:
            continue
        # Leaves out references that wrapped onto a new line, like "(g) and (h)."
        following = textpage.get_text_range(i + len(match.group(0)), 12).strip(" \x07")
        if re.match(r"(and|or)\b|[,.;:]", following):
            continue
        label = match.group(1)
        left, bottom, _, top = textpage.get_charbox(i)
        # Leaves out the rows of dichotomous keys, like "(a) beak is longer than the head ... go to 2"
        if "go to" in textpage.get_text_bounded(0, bottom + 1, KEY_LINE_WIDTH, top - 1):
            continue
        in_letter_column = LETTER_X_RANGE[0] <= left - shift <= LETTER_X_RANGE[1]
        in_roman_column = ROMAN_X_RANGE[0] <= left - shift <= ROMAN_X_RANGE[1]
        # Roman numerals are occasionally printed in the letter column too (e.g. 9701 w20 34 Q2 (c)(v))
        if (label in PART_LETTERS and in_letter_column) or (
            label in ROMAN_NUMERALS and (in_roman_column or in_letter_column)
        ):
            end = i + len(match.group(0)) - 1
            right = textpage.get_charbox(end)[2]
            labels.append((page_height - top, page_height - bottom, left, right, match.group(0)))
            previous_label_end = end
    return labels


def find_question_parts(pdf_path: str) -> list:
    """Finds the part labels of every question, in the same format add_question_parts in makep4-ai.py stores in
    questionParts: [{"coordinates": [x1, y1, x2, y2], "text": "(a)"}, ...] in pixels of the question image
    (as saved by split_question_paper_from_text, before clean_image_file trims its bottom).

    Returns:
        list: One list of parts per question, in question order.
    """
    coordinates, _ = get_text_coordinates(pdf_path)
    question_parts = [[] for _ in range(len(coordinates) - 1)]
    document = pdfium.PdfDocument(pdf_path)
    try:
        page_offsets, _ = _page_offsets(document)
        for page_index, offset in page_offsets.items():
            page = document[page_index]
            for top, bottom, left, right, text in _part_labels(page.get_textpage(), page.get_size()[1]):
                y1 = offset + int(top * SCALE) - STRIP_TOP - PART_PADDING_PX
                y2 = offset + int(bottom * SCALE) - STRIP_TOP + PART_PADDING_PX
                # The question whose region the label starts in
                question = next((i for i in range(len(question_parts)) if coordinates[i] <= y1 < coordinates[i + 1]), None)
                if question is None:
                    continue
                start = coordinates[question]
                question_parts[question].append({
                    "coordinates": [
                        int(left * SCALE) - CROP_LEFT - PART_PADDING_PX,
                        y1 - start,
                        int(right * SCALE) - CROP_LEFT + PART_PADDING_PX,
                        y2 - start,
                    ],
                    "text": text,
                })
    finally:
        document.close()
    for parts in question_parts:
        parts.sort(key=lambda part: (part["coordinates"][1] // 10, part["coordinates"][0]))
    return question_parts


def split_question_paper_from_text(pdf_path: str, out_dir: str) -> list:
    """Splits a question paper into one cleaned image per question, saved as <pdf name>_q<number>.jpg in out_dir,
    with each question's parts (see find_question_parts) saved to <pdf name>_parts.json, keyed by image name.

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

    question_parts = find_question_parts(pdf_path)

    os.makedirs(out_dir, exist_ok=True)
    saved = []
    parts_by_image = {}
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
        parts_by_image[os.path.basename(destination)] = question_parts[i]
    shutil.rmtree(work_dir, ignore_errors=True)
    with open(f"{out_dir}/{pdf_name}_parts.json", "w", encoding="utf-8") as f:
        json.dump(parts_by_image, f, indent=2)
    print(f"{pdf_name}: saved {len(saved)} questions to {out_dir}")
    return saved


def _displayed_box(page, box: tuple) -> tuple:
    """Converts a character box from get_charbox (PDF points, before the page's rotation) to (left, top, right, bottom)
    in points from the top left of the page as displayed, which is how pdf2image renders it. Mark scheme pages
    are often landscape pages stored rotated by 90 degrees."""
    left, bottom, right, top = box
    media_left, media_bottom, media_right, media_top = page.get_mediabox()
    rotation = page.get_rotation()
    if rotation == 90:
        return bottom - media_bottom, left - media_left, top - media_bottom, right - media_left
    if rotation == 180:
        return media_right - right, bottom - media_bottom, media_right - left, top - media_bottom
    if rotation == 270:
        return media_top - top, media_right - right, media_top - bottom, media_right - left
    return left - media_left, media_top - top, right - media_left, media_top - bottom


def _ms_question_column(page, textpage) -> tuple | None:
    """Returns the (left, right) range of the table's Question column on a mark scheme page from its "Question"
    header, or None when the page has no header."""
    match = textpage.search("Question", match_case=True, match_whole_word=True).get_next()
    if not match:
        return None
    header_left = _displayed_box(page, textpage.get_charbox(match[0]))[0]
    return header_left + MS_COLUMN_FROM_HEADER[0], header_left + MS_COLUMN_FROM_HEADER[1]


def _ms_column_numbers(page, textpage, column: tuple) -> list:
    """Finds the numbers that start a line of a mark scheme page's Question column: "2", "2(a)", "2(a)(i)", ...
    Lines are found from the characters' positions rather than the text's line breaks, as some pages store their
    characters out of reading order (e.g. 0625 s17 42 page 9).

    Returns:
        list: (top, number, bare) for each, where top is in points from the top of the displayed page and bare is
          True when the number isn't followed by a part label like "(a)".
    """
    characters = []
    for i in range(textpage.count_chars()):
        char = textpage.get_text_range(i, 1)
        if char.strip():
            characters.append((char, _displayed_box(page, textpage.get_charbox(i))))

    def same_line(a: tuple, b: tuple) -> bool:
        # Overlapping vertically by at least half the shorter character, so subscripts like the "2" of "H2" count
        overlap = min(a[3], b[3]) - max(a[1], b[1])
        return overlap >= 0.5 * min(a[3] - a[1], b[3] - b[1])

    numbers = []
    for char, box in characters:
        left, top, _, _ = box
        if not char.isdigit() or not column[0] <= left < column[1]:
            continue
        line = sorted(
            (other for other in characters if other[1] is not box and same_line(other[1], box)), key=lambda c: c[1][0]
        )
        # Nothing before it on its line in or just left of the column, so it starts the line (and isn't the "0" of "10")
        if any(column[0] - MS_LINE_LOOKBACK <= other[1][2] <= left + 0.5 for other in line):
            continue
        number, right = char, box[2]
        after = [other for other in line if other[1][0] >= right - 0.5]
        while after and after[0][0].isdigit() and after[0][1][0] - right < MS_DIGIT_GAP:
            number, right = number + after[0][0], after[0][1][2]
            after = after[1:]
        if len(number) > 2:
            continue
        numbers.append((top, int(number), not after or after[0][0] != "("))
    return numbers


def _ms_header_tops(page, textpage) -> list:
    """Returns how far each "Question" table header on a mark scheme page is from the top of the displayed page."""
    tops = []
    searcher = textpage.search("Question", match_case=True, match_whole_word=True)
    while (match := searcher.get_next()) is not None:
        tops.append(_displayed_box(page, textpage.get_charbox(match[0]))[1])
    return tops


def find_ms_question_starts(pdf_path: str) -> list:
    """Finds where each question's rows start in a mark scheme: the first row of the Question column whose number
    is the next question (1, 2, 3, ...), whether it's written "2", "2(a)" or "2(a)(i)".

    Args:
    pdf_path (str): The path to the mark scheme.

    Returns:
        list: [(page_index, y), ...] where y is how far the question's first row starts from the top of the displayed
          page in points (or where the page's table header starts, when the row is right under it), one per question
          in order. The first page and pages left out by makeImages
          (see page_skip_reason) are never used.
    """
    document = pdfium.PdfDocument(pdf_path)
    # Bare numbers (see _ms_column_numbers) seen since the last question's first row
    starts, expected, bare_since_start = [], 1, set()
    try:
        pages = [
            (page_index, document[page_index], document[page_index].get_textpage())
            for page_index in range(1, len(document))
        ]
        pages = [(page_index, page, textpage) for page_index, page, textpage in pages
                 if not page_skip_reason(textpage.get_text_range())]
        columns = [_ms_question_column(page, textpage) for _, page, textpage in pages]
        # Pages without a header (a table continuing from the previous page) use the last header's column, or the
        # first one in the mark scheme when no header came before them
        column = next((c for c in columns if c), MS_DEFAULT_COLUMN)
        for (page_index, page, textpage), page_column in zip(pages, columns):
            column = page_column or column

            header_tops = _ms_header_tops(page, textpage)
            for top, number, bare in sorted(_ms_column_numbers(page, textpage, column)):
                # Numbered rows of a table inside an answer ("1 KMnO4 ...", "2 AgNO3 ...", ...) look like questions
                # without parts, so a bare number is part of such a list when every bare number from 1 up to it
                # already came after the current question's first row. A lone repeated heading row ("3 Tests on
                # solid O") isn't a list
                in_list = bare and expected > 1 and set(range(1, expected)) <= bare_since_start
                if number == expected and not in_list:
                    header_above = [header for header in header_tops if 0 < top - header < MS_HEADER_GAP]
                    starts.append((page_index, header_above[0] if header_above else top))
                    expected += 1
                    bare_since_start = set()
                elif bare:
                    bare_since_start.add(number)
    finally:
        document.close()
    return starts


def get_ms_text_coordinates(pdf_path: str) -> list:
    """The y coordinate of each question's start in the stacked image of the stripped mark scheme pages that
    split_mark_scheme in p4_ms_maker_ai.py crops from (page j starts at j * 1300), followed by its height.

    Returns:
        list: The coordinates, one per question in order, then the stacked image's height.
    """
    starts = find_ms_question_starts(pdf_path)
    document = pdfium.PdfDocument(pdf_path)
    try:
        kept_pages = [
            page_index
            for page_index in range(1, len(document))
            if not page_skip_reason(document[page_index].get_textpage().get_text_range())
        ]
    finally:
        document.close()
    page_position = {page_index: j for j, page_index in enumerate(kept_pages)}

    coordinates = [
        page_position[page_index] * MS_PAGE_HEIGHT + max(0, int(y * SCALE) - MS_STRIP_TOP - PADDING_PX)
        for page_index, y in starts
    ]
    coordinates.append(len(kept_pages) * MS_PAGE_HEIGHT)
    return coordinates


def split_mark_scheme_from_text(pdf_path: str, out_dir: str) -> list:
    """Splits a mark scheme into one cleaned image per question, saved as <pdf name>_q<number>.jpg in out_dir, with the
    same page handling as split_mark_scheme in p4_ms_maker_ai.py.

    Returns:
        list: The paths of the saved mark scheme images, in question order.
    """
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    coordinates = get_ms_text_coordinates(pdf_path)
    question_count = len(coordinates) - 1
    if question_count == 0:
        print(f"[WARN] {pdf_name}: no question numbers found in the text layer")
        return []

    work_dir = make_work_dir(f"text-{pdf_name}")
    makeImages(pdf_path, work_dir)
    strip_images(mode="ms", work_dir=work_dir)
    merged = merge_all_images(mode="ms", work_dir=work_dir, save=False)

    os.makedirs(out_dir, exist_ok=True)
    saved = []
    for i in range(question_count):
        local_filename = f"q{i + 1}"
        if not take_screenshot(
            coordinates[i], coordinates[i + 1], local_filename, "long", "", mode="ms", work_dir=work_dir, merged=merged
        ):
            continue
        image_path = f"{work_dir}/questions/{local_filename}.jpg"
        clean_image_file(image_path, mode="ms")
        destination = f"{out_dir}/{pdf_name}_q{i + 1}.jpg"
        shutil.copy(image_path, destination)
        saved.append(destination)
    shutil.rmtree(work_dir, ignore_errors=True)
    print(f"{pdf_name}: saved {len(saved)} mark schemes to {out_dir}")
    return saved


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
        if "ms" in os.path.basename(pdf).lower():
            split_mark_scheme_from_text(pdf, args.out)
        else:
            split_question_paper_from_text(pdf, args.out)
