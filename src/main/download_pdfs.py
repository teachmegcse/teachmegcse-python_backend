import sys
import json
import os
import requests

def download_pdf(pdf_name, base_url, pdf_directory):
    pdf_name = pdf_name.replace("qp", "ms")
    url = base_url + pdf_name
    output_path = os.path.join(pdf_directory, pdf_name)
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
    # Usage: python download_pdfs.py <json_file>
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Usage: python download_pdfs.py <json_file>
    if len(sys.argv) < 2:
        print("Usage: python download_pdfs.py <json_file>")
        sys.exit(1)

    # Build the absolute path to the JSON file relative to the script location
    json_file = os.path.join(SCRIPT_DIR, "..", "resources", "json", sys.argv[1])

    with open(json_file, 'r') as f:
        json_object = json.load(f)

    # Set up the base URL and output directory (also location independent)
    BASE_URL = "https://dynamicpapers.com/wp-content/uploads/2015/09/"
    PDF_DIR = os.path.join(SCRIPT_DIR, "..", "resources", "pdfs", json_object[0]["pdfName"].split("_")[0])


    os.makedirs(PDF_DIR, exist_ok=True)

    pdf_names = set(record["pdfName"] for record in json_object)
    print(f"Found {len(pdf_names)} unique PDF names in the JSON file.")
    print(pdf_names)

    for pdf_name in pdf_names:
        if not pdf_name.lower().endswith('.pdf'):
            continue
        download_pdf(pdf_name, BASE_URL, PDF_DIR)

if __name__ == "__main__":
    main()
