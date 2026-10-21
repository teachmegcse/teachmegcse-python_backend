import sys
import os
import json

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main.utils import load_json_db

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Directories (hardcoded for ig_chem; generalize later if needed)
jsondirectory = os.path.join(BASE_PATH, "resources", "json", "ig_chem_final_long.json")
MSjsonDirectory = os.path.join(BASE_PATH, "resources", "json", "ig_chem_ms.json")
QuestionJsonDirectory = os.path.join(BASE_PATH, "resources", "json", "ig_chem_theory.json")


def normalize_paper_code(code):
    """Normalize paper code by removing ms/qp and converting to lowercase."""
    return code.lower().replace("_ms_", "_").replace("_qp_", "_")


def process_entry(args):
    """Process a single entry."""
    qp_entry, ms_lookup = args

    required_qp_fields = [
        "pdfName",
        "questionNum",
        "questionName",
        "year",
        "Subject",
        "Level",
        "Chapter",
        "paperNumber",
        "questionText",
    ]

    # Skip if any required QP field is missing or None
    if any(qp_entry.get(field) is None for field in required_qp_fields):
        return None

    qp_code = normalize_paper_code(qp_entry["pdfName"])
    key = (qp_entry["questionNum"], qp_code)

    if key not in ms_lookup:
        return None

    ms_entry = ms_lookup[key]

    required_ms_fields = ["fileName", "questionNumber"]

    # Skip if any required MS field is missing or None
    if any(ms_entry.get(field) is None for field in required_ms_fields):
        return None

    return {
        "questionName": qp_entry["questionName"],
        "MSName": ms_entry["fileName"],
        "questionNumber": ms_entry["questionNumber"],
        "pdfName": qp_entry["pdfName"],
        "year": qp_entry["year"],
        "Subject": qp_entry["Subject"],
        "Level": qp_entry["Level"],
        "Chapter": qp_entry["Chapter"],
        "paperNumber": qp_entry["paperNumber"],
        "questionText": qp_entry["questionText"],
        "questionParts": qp_entry.get("questionParts", []),
        # Read from the question paper along with questionText (see check_json_validity in main/utils.py)
        **({"marks": qp_entry["marks"]} if qp_entry.get("marks") is not None else {}),
    }


def combine_and_validate_json(MSjson, QPjson, jsonDirectory):
    print("Starting JSON combination process...")

    # Load the JSON files
    print("Loading JSON files...")
    MSData = load_json_db(MSjson)
    QPData = load_json_db(QPjson)

    print(f"Found {len(MSData)} mark scheme entries")
    print(f"Found {len(QPData)} question paper entries")

    # Create a lookup dictionary for mark scheme data
    ms_lookup = {}
    for ms_entry in MSData:
        key = (ms_entry["questionNumber"], normalize_paper_code(ms_entry["paperCode"]))
        ms_lookup[key] = ms_entry

    # Each entry is only a dictionary lookup, so a process pool would cost more than it saves (and forking
    # makep4-ai.py, which has the scikit-learn models loaded, can hang)
    results = [process_entry((qp_entry, ms_lookup)) for qp_entry in QPData]

    # Filter out None results and save the combined data
    totalData = list(filter(None, results))
    print(f"Processed {len(totalData)} valid entries")

    # questionText and marks come from the question DB, where makep4-ai.py read them from the question papers, so the
    # PDFs aren't read again here
    print("Saving combined data...")
    with open(jsonDirectory, "w") as totalJson:
        json.dump(totalData, totalJson, indent=1)

    print("Combination and validation complete!")


if __name__ == "__main__":
    combine_and_validate_json(MSjsonDirectory, QuestionJsonDirectory, jsondirectory)