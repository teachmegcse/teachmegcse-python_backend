# Sorting & Data Merging

Utilities in this directory clean JSON exports, stitch question + mark-scheme metadata, and publish consolidated CSV/JSON outputs for worksheet builders and analytics consumers.

## combine_json.py

- **Purpose**: Pair question-paper (`*_theory.json`) entries with mark-scheme (`*_ms.json`) entries to produce unified datasets such as `ig_chem_final_long.json`.
- **Highlights**:
  - `normalize_paper_code` hides `_qp_` vs `_ms_` differences before matching.
  - Uses `multiprocessing.Pool` so large datasets merge quickly.
  - Emits rows containing `questionName`, `MSName`, chapter info, and provenance fields (`Level`, `Subject`, `pdfName`, `paperNumber`).
- **Inputs/Outputs**: Update `jsondirectory`, `MSjsonDirectory`, and `QuestionJsonDirectory` near the top of the script to target the subject you are combining.

## final_combine.py

- **Purpose**: Convenience entry point that concatenates multiple subject JSONs into `combined.csv` and `all.json` using pandas.
- **Typical flow**:
  - Edit the `json_files` list to include the datasets you want.
  - Execute `python src/main/sortQuestions/final_combine.py` to refresh the exports in `resources/json/`.

## Tips

- Paths assume execution from `src/main/sortQuestions`; keep `BASE_PATH` definitions intact if you reorganize directories.
- Before running any scripts, confirm the JSON filenames configured here align with `definitions.json` and the extraction pipelines (`makep1`, `makep4`).
