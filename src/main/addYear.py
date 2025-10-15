import json

# Path to the input JSON file and output JSON file
input_json = r"D:\python_projects\teachmegcse\python_files\src\resources\json\mcq.json"
output_json = "output_file.json"


# Function to extract the year from pdfName
def extract_year(pdf_name):
    try:
        for prefix in ["_m", "_w", "_s"]:
            if prefix in pdf_name:
                year_part = pdf_name.split(prefix)[1][
                    :2
                ]  # Extract the two-digit year after the prefix
                return f"20{year_part}" if len(year_part) == 2 else year_part
    except Exception as e:
        print(f"Error processing pdfName: {pdf_name}, Error: {e}")
    return None


# Read the input JSON file with UTF-8 encoding
with open(input_json, "r", encoding="utf-8") as infile:
    data = json.load(infile)

# Add the 'year' field to each JSON object
for question in data:
    question["year"] = extract_year(question.get("pdfName", ""))

# Save the updated data to the output JSON file with UTF-8 encoding
with open(output_json, "w", encoding="utf-8") as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

print(f"Processed JSON file saved as {output_json}")
