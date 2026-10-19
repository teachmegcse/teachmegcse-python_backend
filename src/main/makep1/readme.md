# makep1 pipeline (MCQ extraction)

Automates everything needed to convert paper-1 PDFs into cleaned MCQ images, OCR text, per-chapter metadata, and JSON rows.

## Primary script: `makep1Final.py`

- Launches a Tk file picker so you can select one or more PDF question papers.
- Calls helpers from `main.utils` to:
  - Convert PDFs to images (`makeImages`), skipping blank/notes pages.
  - Invoke the YOLO detection API (`coordinates.py`) to find horizontal cuts between MCQs.
  - Crop each question via `take_screenshot` and store it under `resources/images/test_images/questions`.
  - OCR each crop with EasyOCR (`process_image`), normalize text (`formatText`), and classify it into the correct chapter through the syllabus model declared in `definitions.json`.
  - Copy the cleaned image into `resources/images/<level>/<subject>/mcq/` and update the target JSON file (`mcq_db_path`).

## Requirements

- Detection server: started automatically in the background (and stopped when the script ends); an already running `python src/main/coordinates.py` is reused instead. Its output goes to `resources/images/test_images/coordinates.log`.
- PDFs are processed in parallel, `PDF_WORKERS` in `main/utils.py` sets how many at once (default 4, override with the `PDF_WORKERS` environment variable).
- `definitions.json` entry for the paper code being processed, including `mcqPapers`, `mcq_db_path`, and the `.joblib` filename.
- Mark-scheme PDF present in `resources/full_pdfs/<code>/` so `extract_answers_from_pdf` can pull the correct answers.

## Output

- Cropped MCQ images per level/subject.
- Updated JSON (e.g., `ig_chem_mcq.json`) containing `questionName`, `Answer`, `Chapter`, `Level`, `paperNumber`, etc.
- Temporary working files live in `resources/images/test_images/`; run `cleanup()` when finished or rely on the script’s automatic cleanup.

## Usage tips

- Inspect the YOLO confidence (`--mode` weights) if cuts look misaligned; the detector lives under `resources/vision-models/`.
- `take_screenshot` skips captures that are shorter than configured thresholds; adjust logic in `main.utils` if your papers use different spacing.
- The script assumes Cambridge naming (`0620_s24_qp_12.pdf`). Update `extract_paper_number` if you ingest other formats.
