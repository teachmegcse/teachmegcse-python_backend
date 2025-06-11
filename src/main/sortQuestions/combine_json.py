import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import os
import json
from multiprocessing import Pool, cpu_count

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))

# Directories
jsondirectory = rf"{BASE_PATH}\resources\json\phy_db_final_p4.json"
MSjsonDirectory = rf"{BASE_PATH}\resources\json\phy_db_ms_p4.json"
QuestionJsonDirectory = rf"{BASE_PATH}\resources\json\phy_db_theory.json"

def normalize_paper_code(code):
    """Normalize paper code by removing ms/qp and converting to lowercase."""
    return code.lower().replace("_ms_", "_").replace("_qp_", "_")


def process_entry(args):
    """Process a single entry."""
    qp_entry, ms_lookup = args

    qp_code = normalize_paper_code(qp_entry["pdfName"])
    key = (qp_entry["questionNum"], qp_code)
    if key not in ms_lookup:
        return None  # Skip if no match


    # Paths and processing
    question_name = qp_entry["questionName"]
    ms_entry = ms_lookup[key]
    ms_name = ms_entry["fileName"]

    # Return processed data
    return {
        "questionName": question_name,
        "MSName": ms_name,
        "questionNumber": ms_entry["questionNumber"],
        "pdfName": qp_entry["pdfName"],
        "year": qp_entry["year"],
        "Subject": qp_entry["Subject"],
        "Level": qp_entry["Level"],
        "Chapter": qp_entry["Chapter"],
        "paperNumber": qp_entry["paperNumber"],
        "questionText": qp_entry["questionText"]
    }

def combineJSON(MSjson, QPjson, jsonDirectory):
    print("Starting JSON combination process...")

    # Load the JSON files
    print("Loading JSON files...")
    with open(MSjson, 'r') as f:
        MSData = json.load(f)
    with open(QPjson, 'r') as f:
        QPData = json.load(f)

    print(f"Found {len(MSData)} mark scheme entries")
    print(f"Found {len(QPData)} question paper entries")

    # Create a lookup dictionary for mark scheme data
    ms_lookup = {}
    for ms_entry in MSData:
        key = (ms_entry["questionNumber"], normalize_paper_code(ms_entry["paperCode"]))
        ms_lookup[key] = ms_entry

    # Use multiprocessing to process entries
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_entry, [
            (qp_entry, ms_lookup) 
            for qp_entry in QPData
        ])

    # Filter out None results and save the combined data
    totalData = list(filter(None, results))
    print(f"Processed {len(totalData)} valid entries")

    print("Saving combined data...")
    with open(jsonDirectory, 'w') as totalJson:
        json.dump(totalData, totalJson, indent=1)

    print("Combination complete!")

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()  # Optional for compatibility on some systems

    combineJSON(MSjsonDirectory, QuestionJsonDirectory, jsondirectory)
