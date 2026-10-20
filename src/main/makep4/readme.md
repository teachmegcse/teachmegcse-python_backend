# makep4 pipeline (Long-form + mark schemes)

Tools here handle long-answer question extraction (papers 2–6) and AI-assisted mark-scheme splitting.

## Running the whole pipeline

```bash
python makep4-ai.py                    # qp -> ms -> combine
python makep4-ai.py --steps qp         # debug: only split the question papers
python makep4-ai.py --steps qp,ms      # skip combine
python makep4-ai.py --steps combine    # only re-pair the DBs of the selected subjects
```

Select the question papers **and** their mark schemes in the same dialog. Files with `ms` in their name go to the
mark-scheme step, the rest to the question step. The combine step pairs `long_db_path` + `long_ms_db_path` into
`long_final_db_path` (from `definitions.json`) for every subject that was selected, then validates the question text
and marks against the PDFs in `resources/full_pdfs/<code>/`.

`p4_ms_maker_ai.py` and `../combine_and_validate_json.py` can still be run on their own.

## `makep4-ai.py`

- Selects one or more PDFs (question papers) through the Tk dialog.
- Converts each page to an image and trims headers/footers via `strip_images`.
- Calls the YOLO detection API (`coordinates.py`) for every page, then merges all pages into a single tall canvas so questions spanning multiple pages stitch cleanly.
- Generates a sorted list of Y coordinates, crops each question using `take_screenshot(..., type="long")`, and copies it into `resources/images/<level>/<subject>/long/`.
- OCRs + normalizes the cropped text, classifies chapter + level using the syllabus models, and appends a record to the configured `long_db_path` JSON.

## `p4_ms_maker_ai.py`

- Mirrors the question workflow but operates on mark-scheme PDFs.
- Uses the same detection API to locate answer boundaries and saves the resulting crops into the MS image folder.
- Filenames continue from the highest number already in the MS DB, so a new run never overwrites earlier MS images.
- Each cropped MS entry is paired with its question by the combine step (`combine_and_validate_json.py`).

## Supporting files

- `generatePages.py`, `testing.py`, etc., store experimental routines for batching or debugging extraction logic.
- Long-answer metadata ultimately feeds into classified PDF generation once merged with MS references.

## Prerequisites

- YOLO server: started automatically in the background (and stopped when the script ends); an already running `python src/main/coordinates.py` is reused instead. Its output goes to `resources/images/test_images/coordinates.log`.
- PDFs are processed in parallel, `PDF_WORKERS` in `main/utils.py` sets how many at once (default 4, override with the `PDF_WORKERS` environment variable).
- `definitions.json` entries with valid `longPapers`, `long_db_path`, `long_ms_db_path` and (for the combine step) `long_final_db_path` values.
- Destination directories under `resources/images/<level>/<subject>/long/` and `.../ms/` (auto-created if missing).

## Outputs

- Long-question JPEGs cleaned of whitespace and truncated at content end (`clean_image`).
- JSON append-only logs containing chapter, question number, source PDF, and formatted text.
- Optional mark-scheme crops ready for downstream pairing.
