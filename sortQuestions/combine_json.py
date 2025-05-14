import os
import shutil
import json
import cv2
import pytesseract
from joblib import load
from multiprocessing import Pool, Manager, cpu_count
import getFormattedTextfromPdf
from pathConst import BASE_PATH, TESSERACT_PATH

# Labels
asLabels = ['Atomic structure', 'Atoms, molecules and stoichiometry', 
             'Chemical bonding', 'States of matter', 'Chemical energetics', 'Electrochemistry', 'Equilibria',
               'Reaction kinetics', 'The Periodic Table: chemical periodicity', 'Group 2', 'Group 17', 'Nitrogen and sulfur', 'introduction to AS Level organic chemistry', 
               'Hydrocarbons', 'Halogen compounds', 'Hydroxy compounds', 'Carbonyl compounds', 'Carboxylic acids and derivatives', 'Nitrogen compounds', 'Polymerisation',
                 'Organic synthesis', 'Analytical techniques']

a2Labels = ['Chemical energetics', 'Electrochemistry', 
             'Equilibria', 'Reaction kinetics', 'Group 2', 'Chemistry of transition elements', 'An introduction to A Level organic chemistry',
               'Hydrocarbons', 'Halogen compounds', 'Hydroxy compounds', 'Carboxylic acids and derivatives','Nitrogen compounds',
               'Polymerisation','Organic synthesis','Analytical techniques']

IGLabels = ['States of matter', 'Atoms, elements and compounds', 
             'Stoichiometry', 'Electrochemistry', 'Chemical energetics', 'Chemical reactions', 'Acids, bases and salts',
               'The Periodic Table', 'Metals', 'Chemistry of the environment', 'Organic chemistry', 'Experimental techniques and chemical analysis']

# Directories
jsondirectory = rf"{BASE_PATH}\python_files\makep4\phy_db_final_p4.json"
MSjsonDirectory = rf"{BASE_PATH}\json_files\phy_db_ms_p4.json"
QuestionJsonDirectory = rf"{BASE_PATH}\json_files\phy_db_theory.json"
UNSORTED_DIR = rf"{BASE_PATH}\teachmegcse\images\unsorted\IGCSE\chemistry\long"
SORTED_DIR = rf"{BASE_PATH}\images\sorted\IGCSE\chemistry\long"
TESSERACT_CMD = TESSERACT_PATH
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

def copy_files_to_chapter_folders(question_name, ms_name, chapter_num):
    """Copy question and mark scheme files to chapter folders."""
    chapter_dir = os.path.join(SORTED_DIR, str(chapter_num))
    os.makedirs(chapter_dir, exist_ok=True)

    # Source file paths
    question_src = os.path.join(UNSORTED_DIR, question_name)
    ms_src = os.path.join(UNSORTED_DIR, ms_name)

    # Destination file paths
    question_dest = os.path.join(chapter_dir, question_name)
    ms_dest = os.path.join(chapter_dir, ms_name)

    # Copy files
    if os.path.exists(question_src):
        shutil.copy(question_src, question_dest)
    else:
        print(f"Warning: Question file {question_src} does not exist.")

    if os.path.exists(ms_src):
        shutil.copy(ms_src, ms_dest)
    else:
        print(f"Warning: Mark scheme file {ms_src} does not exist.")

def process_entry(args):
    """Process a single entry."""
    qp_entry, ms_lookup, asLabels, a2Labels, IGLabels, UNSORTED_DIR, CUSTOM_CONFIG = args

    qp_code = normalize_paper_code(qp_entry["pdfName"])
    key = (qp_entry["questionNum"], qp_code)
    if key not in ms_lookup:
        return None  # Skip if no match

    #model = "aschem" if qp_entry["Level"] == "AS" else "a2chem"
    model = "IGchem"
    #start_chapter = 0 if model == "aschem" else len(asLabels)
    start_chapter = 0

    # Paths and processing
    question_name = qp_entry["questionName"]
    ms_entry = ms_lookup[key]
    ms_name = ms_entry["fileName"]

    question_text = process_image(os.path.join(UNSORTED_DIR, question_name), CUSTOM_CONFIG).lower().strip()
    chapter = predict(question_text, model)
    #chapter_num = (asLabels.index(chapter) + 1 if model == "aschem" else a2Labels.index(chapter) + 1)
    chapter_num = IGLabels.index(chapter) + 1

    # Copy files to chapter folder
    copy_files_to_chapter_folders(question_name, ms_name, chapter_num + start_chapter)

    # Return processed data
    return {
        "questionName": question_name,
        "MSName": ms_name,
        "questionNumber": ms_entry["questionNumber"],
        "pdfName": qp_entry["pdfName"],
        "year": qp_entry["year"],
        "Subject": qp_entry["Subject"],
        "Level": qp_entry["Level"],
        "Chapter": chapter_num + start_chapter,
        "paperNumber": qp_entry["paperNumber"],
        "questionText": question_text
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
            (qp_entry, ms_lookup, asLabels, a2Labels, IGLabels, UNSORTED_DIR, CUSTOM_CONFIG) 
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
