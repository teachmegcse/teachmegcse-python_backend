# CIE A-level and IGCSE Exam Processing Automation

Automation toolkit for turning Cambridge IGCSE and A-level PDFs into structured datasets, images, ML-ready text, and printable study packs. The repo houses extraction scripts, YOLO-powered detectors, FastAPI services, and syllabus-specific ML pipelines that label every question with its level, paper number, and chapter before generating worksheets and answer booklets.

## Repository Layout

| Path | Description |
| --- | --- |
| `src/main/makep1` | MCQ extraction pipeline (paper 1) plus helpers shared with other flows. |
| `src/main/makep4` | Long-form extraction (papers 3–6) and AI-based mark-scheme splitting. |
| `src/main/classified` | FastAPI services that assemble classified PDFs / ZIPs. |
| `src/main/sci-kit` | Training code that produces the `.joblib` syllabus classifiers. |
| `src/main/sortQuestions` | Utilities that merge QP/MS JSON, clean text, and build consolidated datasets. |
| `src/resources` | Working assets: PDFs, cropped images, YOLO weights, JSON databases, trained models. |

## Prerequisites

- Python 3.10+ and `pip`
- System deps for `pdf2image` (Poppler) and OpenCV; GPU drivers if you plan to retrain YOLO
- Tesseract is not required because OCR is handled through EasyOCR
- Optional: Google Generative AI access for explanation generation (`GOOGLE_API_KEY2`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Place raw PDFs under `src/resources/full_pdfs/<paper_code>/` and trained YOLO checkpoints under `src/resources/vision-models/` (e.g. `best1.pt`). The ML classifiers referenced in `src/main/definitions.json` must exist inside `src/resources/sci-kit/`.

## Core Workflows

### 1. MCQ ingestion (`makep1`)
- Start the bounding-box API: `python src/main/coordinates.py --mode best1`
- Run `python src/main/makep1/makep1Final.py` (requires a GUI session for the Tk file picker)
- The script calls EasyOCR, classifies each cropped MCQ via the syllabus model, and copies cleaned images to `resources/images/<level>/<subject>/mcq`
- Outputs JSON rows to `resources/json/<mcq_db_path>` as configured in `definitions.json`

### 2. Long question ingestion (`makep4`)
- Same YOLO service as above, but `makep4-ai.py` merges every page, stitches bounding boxes, and saves long-form questions under `.../long/`
- Mark schemes can be split by `p4_ms_maker_ai.py`, which reuses the detector for MS PDFs
- Each record is appended to the relevant `long_db_path` JSON declared in `definitions.json`

### 3. Classification & packaging (`sortQuestions`, `classified`)
- `combine_json.py` pairs question-paper JSON with mark-scheme JSON to produce chapter-aware datasets (e.g. `ig_chem_final_long.json`)
- `format-json.py` and `final_combine.py` clean, merge, and export CSV/JSON for downstream consumption
- `uvicorn src.main.classified.p1_api:app` exposes `/generate-pdf/`, which accepts a `QuestionsList` payload and returns a ZIP containing `questions.pdf` and `answers.pdf`

### 4. Explanations via Gemini (`explanation_generator.py`)
- Requires `GOOGLE_API_KEY2` in `.env`
- Usage: `python src/main/explanation_generator.py ig_chem_mcq.json`
- For each `questionName` image, the script stores the AI-generated rationale alongside the answer in the source JSON

### 5. Supporting utilities
- `download_pdfs.py`: batch fetch raw papers given metadata
- `clean_folder.py`: remove unwanted PDFs (e.g. GT/CI) from staging folders
- `check_json_validity.py`: validates `questionText` and marks by re-reading the full PDFs with `pdfplumber`
- `final_combine.py`: aggregates subject-level JSON files into a single CSV/JSON pair for analytics

## Data & Model Locations

- `resources/full_pdfs/` – source question papers and mark schemes
- `resources/images/` – per-level, per-subject image banks (`mcq/`, `long/`, `questions/`)
- `resources/json/` – intermediate and final JSON exports referenced by web/API flows
- `resources/sci-kit/` – `.joblib` classifiers for each subject/level combo
- `resources/vision-models/` – YOLO checkpoints consumed by `coordinates.py`

## Running the FastAPI services

- Detection API: `python src/main/coordinates.py --mode best1`
- Packager API: `uvicorn src.main.classified.p1_api:app --host 0.0.0.0 --port 8010`
- Legacy variants (`p1_api_2.py`, `p1_api_server.py`) exist for experimentation but the primary entrypoint is `p1_api.py`

## Tips

- Keep `definitions.json` in sync with available PDFs, classifiers, and JSON destinations
- The Tk-based scripts need a desktop session or X forwarding
- For reproducible OCR output, delete `resources/images/test_images` between runs using `main.utils.cleanup()`
