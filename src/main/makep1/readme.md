# makep1 pipeline (MCQ extraction)

Automates everything needed to convert paper-1 PDFs into cleaned MCQ images, OCR text, per-chapter metadata, and JSON rows.

## Primary script: `makep1Final.py`

- Launches a Tk file picker so you can select one or more PDF question papers.
- Calls helpers from `main.utils` to:
  - Convert PDFs to images (`makeImages`), skipping blank/notes pages.
  - Find where each MCQ starts on its page from the PDF's text layer (`get_mcq_text_coordinates`, see below).
  - Crop each question via `take_screenshot` and store it under `resources/images/test_images/questions`.
  - OCR each crop with EasyOCR (`process_image`), normalize text (`formatText`), and classify it into the correct chapter through the syllabus model declared in `definitions.json`.
  - Copy the cleaned image into `resources/images/<level>/<subject>/mcq/` and update the target JSON file (`mcq_db_path`).

## Finding the questions from the text layer

- `find_mcq_question_starts(pdf)` in `main/utils.py` finds each question number (1, 2, 3, ...) in the left margin from
  the PDF's text layer, and `get_mcq_text_coordinates(pdf)` returns where `process_pdf` crops each question
  (`{page image number: [(question number, y), ...]}` in stripped-page pixels). No GPU or server.
- A question removed from the paper ("Due to an issue with Question 22, the question has been removed ...") is skipped,
  and the numbers of the questions after it are kept, so they still line up with the mark scheme's answers.
- `python ../makep4/question_numbers.py paper.pdf ... [--out DIR]` saves the questions of MCQ papers (those in
  `mcqPapers`) as `<pdf name>_q<number>.jpg` with `split_mcq_paper_from_text`.
- Papers printed on A3 (e.g. 0620 s17 11) are found correctly, but `strip_images` and the crops assume A4 pages, so
  questions low on the page are cut off.

## Requirements

- PDFs with a text layer: questions are found from the text, so no YOLO detection server or GPU is needed.
- PDFs are processed in parallel, `PDF_WORKERS` in `main/utils.py` sets how many at once (default 4, override with the `PDF_WORKERS` environment variable).
- `definitions.json` entry for the paper code being processed, including `mcqPapers`, `mcq_db_path`, and the `.joblib` filename.
- Mark-scheme PDF present in `resources/full_pdfs/<code>/` so `extract_answers_from_pdf` can pull the correct answers.

## Output

- Cropped MCQ images per level/subject.
- Updated JSON (e.g., `ig_chem_mcq.json`) containing `questionName`, `Answer`, `Chapter`, `Level`, `paperNumber`, etc.
- Temporary working files live in `resources/images/test_images/`; run `cleanup()` when finished or rely on the script’s automatic cleanup.

## Usage tips

- If cuts look misaligned, check the number position and size limits (`MCQ_*` constants) in `main/utils.py`.
- `take_screenshot` skips captures that are shorter than configured thresholds; adjust logic in `main.utils` if your papers use different spacing.
- The script assumes Cambridge naming (`0620_s24_qp_12.pdf`). Update `extract_paper_number` if you ingest other formats.
