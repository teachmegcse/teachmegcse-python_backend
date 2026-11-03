# ML Training Utilities

Scripts and artifacts in this folder build the `.joblib` classifiers referenced in `definitions.json`. Each model maps cleaned question text to an IGCSE/AS/A2 chapter number so downstream pipelines can auto-tag cropped images.

## Directory contents

- `trainModels.py` – shared helper that trains a `TfidfVectorizer + ComplementNB` pipeline and writes the result to `resources/sci-kit/<name>.joblib`. Mathematics splits its syllabus text into 12-line pieces first (`chunk_lines`).
- `chapter_gold.json` / `evaluate_chapters.py` – questions from real papers labelled by hand, and a script that scores the models against them. `dev` papers are for trying changes, `test` papers for the final check: `python evaluate_chapters.py --split test --misses`.
- `trainWithSyllabus<Subject><Level>.py` – subject/level-specific scripts that:
  1. Define chapter labels (`allLabels`).
  2. Provide raw syllabus text snippets per chapter (copied from Cambridge PDFs).
  3. Call `formatText` from `main.utils` for consistency with runtime cleaning.
  4. Invoke `trainModels.train()` to produce the classifier.
- `trainWithPdfs.py` – generic trainer that reads actual syllabus PDFs instead of inline text blocks.

## Workflow

1. Ensure the target syllabus text lives under `resources/full_pdfs/` or is embedded in the script.
2. Activate the virtualenv and install requirements (`scikit-learn`, `nltk`, etc.).
3. Run the desired training script, e.g.:

```bash
python src/main/sci-kit/trainWithSyllabusChemAS.py
```

4. The resulting `.joblib` file lands in `resources/sci-kit/`. Update `definitions.json` if you change filenames.

## Notes

- All trainers depend on `main.utils.formatText`. After changing it, run every `trainWithSyllabus*.py` again so training and prediction clean text the same way, then `makep4-ai.py --steps combine --refresh-text` to update the stored chapters.
- Some scripts reference large multiline strings copied from official syllabi; ensure licensing requirements are respected before distributing those files publicly.
