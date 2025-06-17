import sys
import json
import os
import requests

def download_pdf(pdf_name, base_url, pdf_directory):
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

def download_from_json(json_name):
    # Usage: python download_pdfs.py <json_file>
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Build the absolute path to the JSON file relative to the script location
    json_file = os.path.join(SCRIPT_DIR, "..", "resources", "json", json_name)

    with open(json_file, 'r') as f:
        json_object = json.load(f)

    # Set up the base URL and output directory (also location independent)
    BASE_URL = "https://dynamicpapers.com/wp-content/uploads/2015/09/"
    PDF_DIR = os.path.join(SCRIPT_DIR, "..", "resources", "pdfs", "cie_papers", json_object[0]["pdfName"].split("_")[0])


    os.makedirs(PDF_DIR, exist_ok=True)

    pdf_names = set(record["pdfName"] for record in json_object)
    print(f"Found {len(pdf_names)} unique PDF names in the JSON file.")
    print(pdf_names)

    for pdf_name in pdf_names:
        if not pdf_name.lower().endswith('.pdf'):
            continue
        pdf_name = pdf_name.replace("qp", "ms")
        download_pdf(pdf_name, BASE_URL, PDF_DIR)


def download_papers_for_years(target_year, code):
    """
    Downloads all 'qp' and 'ms' PDFs for each season (w, s, m) from 2025 down to and including target_year.
    Assumes CIE naming format: <subject>_<code>_<season><year>_<qp/ms>_<variant>.pdf
    """
    BASE_URL = "https://dynamicpapers.com/wp-content/uploads/2015/09/"
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PDF_DIR = os.path.join(SCRIPT_DIR, "..", "resources", "pdfs", "cie_papers", code)
    os.makedirs(PDF_DIR, exist_ok=True)
    variants = ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43", "51", "52", "53", "61", "62", "63"]
    seasons = ["m", "s", "w"]

    for year in range(int(target_year), 2026):
        for season in seasons:
            for paper_type in ["qp", "ms"]:
                for variant in variants:
                    pdf_name = f"{code}_{season}{str(year)[-2:]}_{paper_type}_{variant}.pdf"
                    try:
                        download_pdf(pdf_name, BASE_URL, PDF_DIR)
                    except Exception as e:
                        print(f"Error downloading {pdf_name}: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python download_pdfs.py <target_year> <code>")
    download_papers_for_years(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()