import sys
import json
import os
from PyPDF2 import PdfReader

if len(sys.argv) < 2:
    print("Usage: python check_json_validity.py <json_file>")
    sys.exit(1)
json_file = sys.argv[1]
with open(json_file, 'r') as f:
    json_object = json.load(f)

def check_json_validity(json_object):
    flag = True
    past_id = 0
    for record in json_object:
        paper = record["pdfName"]
        last_part = record["questionName"].split('_')[3]
        id = int(last_part.split('.')[0])
        if id != past_id + 1:
            flag = False
            missing_count = id - past_id - 1
            for missing in range(1, missing_count + 1):
                missing_id = past_id + missing
                print(f"missing ID: {missing_id}, question number: {(missing_id) % 40}, paper: {past_paper}")
        past_id = id
        past_paper = paper
        
    prev_file_name = None
    for record in json_object:
        file_name = record["pdfName"]
        if prev_file_name is None:
            prev_file_name = file_name
            count = 1
        else:
            if file_name == prev_file_name:
                count += 1
            else:
                if count != 40:
                    flag = False
                    print(f"Invalid question count for paper {prev_file_name}: {count}")
                prev_file_name = file_name
                count = 1
    
    # Compare answers in JSON with those in the corresponding MS PDFs
    current_pdf_name = None
    ms_text = None
    ms_answers = dict()
    pdf_dir = "pdfs"
    for record in json_object:
        qp_pdf_name = record["pdfName"]
        ms_pdf_name = qp_pdf_name.replace("qp", "ms")
        if ms_pdf_name != current_pdf_name:
            # Open and parse the new MS PDF
            ms_path = os.path.join(pdf_dir, ms_pdf_name)
            if not os.path.exists(ms_path):
                print(f"MS PDF not found: {ms_pdf_name}")
                current_pdf_name = ms_pdf_name
                ms_answers = dict()
                continue
            try:
                reader = PdfReader(ms_path)
                ms_text = " ".join(page.extract_text() or '' for page in reader.pages)
                # Extract answers: lines like '1 D 1', '2 C 1', etc.
                ms_answers = dict()
                import re
                for match in re.finditer(r"(\d{1,2})\s+([A-D])\s+1", ms_text):
                    qnum = int(match.group(1))
                    ans = match.group(2)
                    ms_answers[qnum] = ans
            except Exception as e:
                print(f"Error reading {ms_pdf_name}: {e}")
                ms_answers = dict()
            current_pdf_name = ms_pdf_name
        # Now compare the answer
        if len(ms_answers) != 40:
            print(f"MS PDF {ms_pdf_name} does not have 40 answers, found {len(ms_answers)}")
        qid = int(record["questionName"].split('_')[3].split('.')[0])
        qnum = qid % 40 if qid % 40 != 0 else 40
        json_answer = record["Answer"]
        ms_answer = ms_answers.get(qnum)
        if ms_answer and json_answer and ms_answer != json_answer:
            print(f"Contradiction in {ms_pdf_name}, {record["questionName"]}, Q{qnum}: JSON='{json_answer}' vs MS='{ms_answer}'")

check_json_validity(json_object)