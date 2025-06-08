import sys
import json
import os
import requests
import re

# Usage: python download_pdfs.py <json_file>
if len(sys.argv) < 2:
    print("Usage: python download_pdfs.py <json_file>")
    sys.exit(1)
json_file = sys.argv[1]

with open(json_file, 'r') as f:
    json_object = json.load(f)

# Set up the base URL and output directory
BASE_URL = "https://dynamicpapers.com/wp-content/uploads/2015/09/"
PDF_DIR = "pdfs"
os.makedirs(PDF_DIR, exist_ok=True)
def qp_to_ms(pdf_name):
    # Replace 'qp' with 'ms' only if 'qp' is surrounded by non-word boundaries (e.g., in the middle)
    return re.sub(r'(?<=\w)qp(?=\w)', 'ms', pdf_name)
def download_pdf(pdf_name):
    pdf_name = qp_to_ms(pdf_name)
    url = BASE_URL + pdf_name
    output_path = os.path.join(PDF_DIR, pdf_name)
    if os.path.exists(output_path):
        print(f"Already exists: {pdf_name}")
        return
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {pdf_name}")
        else:
            print(f"Failed to download {pdf_name}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error downloading {pdf_name}: {e}")

def main():
    pdf_names = set(record["pdfName"] for record in json_object)
    print(f"Found {len(pdf_names)} unique PDF names in the JSON file.")
    print(pdf_names)
    for pdf_name in pdf_names:
        if not pdf_name.lower().endswith('.pdf'):
            continue
        download_pdf(pdf_name)

if __name__ == "__main__":
    main()
