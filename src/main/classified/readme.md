# Classified PDF Services

APIs and helpers that bundle curated question datasets into printable PDFs + ZIP archives.

## p1_api.py

- **What it does**: FastAPI app exposing `/generate-pdf/`. Accepts a `QuestionsList` payload (MCQ + long question metadata) and returns a ZIP containing `questions.pdf` and `answers.pdf`.
- **Key behaviors**:
  - Applies CORS defaults for external callers.
  - Splits MCQ vs long-answer data so layouts stay consistent (MCQ images inline; long answers paginated and rotated when necessary).
  - Uses `resources/images/<level>/<subject>` to fetch question/answer JPEGs saved by `makep1` / `makep4` pipelines.
  - Stores the generated PDFs in `resources/pdfs/classified/` before zipping.
- **Running locally**:
  ```bash
  uvicorn src.main.classified.p1_api:app --host 0.0.0.0 --port 8010
  ```

## p1_api_2.py / p1_api_server.py

- Legacy/alternate FastAPI entry points kept for experimentation (different payload formats, legacy UI integration). Prefer `p1_api.py` unless you need backwards compatibility.

## p1_fixed.py

- CLI-oriented script that reads a predefined JSON dataset, renders `questions.pdf` + `answers.pdf`, and zips them without hosting an API. Handy for batch generation or debugging layout changes offline.

## p1_images_to_classified.py

- Builds chaptered PDFs directly from an image directory (e.g., `resources/images/IGCSE/chemistry/mcq`).
- Optional flags control chapter title pages, index generation, advertising banners, and mark-scheme inclusion.
- Useful for ad-hoc worksheet creation when you already have curated folders rather than JSON payloads.
