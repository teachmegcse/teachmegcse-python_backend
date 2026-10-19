# makep4 pipeline (Long-form + mark schemes)

Tools here handle long-answer question extraction (papers 2–6) and AI-assisted mark-scheme splitting.

## `makep4-ai.py`

- Selects one or more PDFs (question papers) through the Tk dialog.
- Converts each page to an image and trims headers/footers via `strip_images`.
- Calls the YOLO detection API (`coordinates.py`) for every page, then merges all pages into a single tall canvas so questions spanning multiple pages stitch cleanly.
- Generates a sorted list of Y coordinates, crops each question using `take_screenshot(..., type="long")`, and copies it into `resources/images/<level>/<subject>/long/`.
- OCRs + normalizes the cropped text, classifies chapter + level using the syllabus models, and appends a record to the configured `long_db_path` JSON.

## `p4_ms_maker_ai.py`

- Mirrors the question workflow but operates on mark-scheme PDFs.
- Uses the same detection API to locate answer boundaries and saves the resulting crops into the MS image folder.
- Each cropped MS entry can be paired later via `combine_json.py`.

## Supporting files

- `generatePages.py`, `testing.py`, etc., store experimental routines for batching or debugging extraction logic.
- Long-answer metadata ultimately feeds into classified PDF generation once merged with MS references.

## Prerequisites

- YOLO server: started automatically in the background (and stopped when the script ends); an already running `python src/main/coordinates.py` is reused instead. Its output goes to `resources/images/test_images/coordinates.log`.
- PDFs are processed in parallel, `PDF_WORKERS` in `main/utils.py` sets how many at once (default 4, override with the `PDF_WORKERS` environment variable).
- `definitions.json` entries with valid `longPapers`, `long_db_path`, and `long_ms_db_path` values.
- Destination directories under `resources/images/<level>/<subject>/long/` and `.../ms/` (auto-created if missing).

## Outputs

- Long-question JPEGs cleaned of whitespace and truncated at content end (`clean_image`).
- JSON append-only logs containing chapter, question number, source PDF, and formatted text.
- Optional mark-scheme crops ready for downstream pairing.
