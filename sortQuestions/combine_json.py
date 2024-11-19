import json
from os.path import exists
from joblib import load
import getFormattedTextfromPdf
import cv2
import pytesseract

# This file is for p4 only

allLabels = ['Motion in a circle', 'Gravitational fields', 
             'Temperature', 'Ideal gases', 'Thermodynamics', 'Oscillations', 'Electric fields',
               'Capacitance', 'Magnetic fields', 'Alternating currents', 'Quantum physics', 'Nuclear physics',
               'Medical physics', 'Astronomy and cosmology']

subjectname = "physics"
model = "a2phyp4"
level2 = "A-level"
paperNumber = "p4"
start_chapter = 1 # Default is 1 when AS but not 1 when A2
jsondirectory = r"D:\python_projects\teachmegcse\python_files\makep4\phy_db_final_p4.json"
MSjsonDirectory = r"D:\python_projects\teachmegcse\json_files\phy_db_ms_p4.json"
QuestionJsonDirectory = r"D:\python_projects\teachmegcse\json_files\phy_db_p4.json"
TESSERACT_CMD = r"D:\python_projects\Tesseract-OCR\tesseract.exe"
CUSTOM_CONFIG = r'--oem 3 --psm 6'
MODEL_PATH_TEMPLATE = "D:/python_projects/teachmegcse/python_files/sci-kit/{model}.joblib"

def normalize_paper_code(code):
    """Normalize paper code by removing ms/qp and converting to lowercase."""
    return code.lower().replace("_ms_", "_").replace("_qp_", "_")

def process_image(image_path, custom_config):
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img, config=custom_config)

def predict(data, model):
    pipeline = load(MODEL_PATH_TEMPLATE.format(model=model))
    data = getFormattedTextfromPdf.formatText(data)
    predicted_labels = pipeline.predict([data])
    return predicted_labels[0]

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
            image_path = f"D:/python_projects/teachmegcse/images/unsorted/{level2}/{subjectname}/{paperNumber}/{qp_entry['questionName']}" # This is the path to the image of the question
            question_text = process_image(image_path, CUSTOM_CONFIG).lower().strip()
            chapter = predict(question_text, model)
            chapter_num = start_chapter + allLabels.index(chapter)
            ms_entry = ms_lookup[key]
            totalData.append({
                "questionName": qp_entry["questionName"],
                "MSName": ms_entry["fileName"],
                "questionNumber": ms_entry["questionNumber"],
                "pdfName": qp_entry["pdfName"],
                "year" : qp_entry["year"],
                "Subject" : qp_entry["Subject"],
                "Level" : qp_entry["Level"],
                "Chapter" : chapter_num,
                "paperNumber" : int(paperNumber[1:])
            })
    
    print(f"Found {matches_found} matching pairs")
    
    # Save the combined data
    print("Saving combined data...")
    with open(jsonDirectory, 'w') as totalJson:
        json.dump(totalData, totalJson, indent=1)
    
    print("Combination complete!")

combineJSON(MSjsonDirectory, QuestionJsonDirectory, jsondirectory)