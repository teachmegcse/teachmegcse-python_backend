import json
from os.path import exists

subjectcode = 9702
subjectname = "physics"
jsondirectory = r"D:\python_projects\teachmegcse\python_files\makep4\phy_db_final_p4.json"
MSjsonDirectory = r"D:\python_projects\teachmegcse\json_files\phy_db_ms_p4.json"
QuestionJsonDirectory = r"D:\python_projects\teachmegcse\json_files\phy_db_p4.json"

def normalize_paper_code(code):
    """Normalize paper code by removing ms/qp and converting to lowercase."""
    return code.lower().replace("_ms_", "_").replace("_qp_", "_")

def combineJSON(MSjson, QPjson, jsonDirectory):
    print("Starting JSON combination process...")
    totalData = []
    
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
    
    # Match questions with mark schemes
    matches_found = 0
    for qp_entry in QPData:
        qp_code = normalize_paper_code(qp_entry["pdfName"])
        key = (qp_entry["questionNum"], qp_code)
        
        if key in ms_lookup:
            matches_found += 1
            ms_entry = ms_lookup[key]
            totalData.append({
                "questionName": qp_entry["questionName"],
                "MSName": ms_entry["fileName"],
                "questionNumber": ms_entry["questionNumber"],
                "pdfName": qp_entry["pdfName"]
            })
    
    print(f"Found {matches_found} matching pairs")
    
    # Save the combined data
    print("Saving combined data...")
    with open(jsonDirectory, 'w') as totalJson:
        json.dump(totalData, totalJson, indent=1)
    
    print("Combination complete!")

combineJSON(MSjsonDirectory, QuestionJsonDirectory, jsondirectory)