import json

# Path to the input JSON file and output JSON file
input_json = r"C:\Users\ALLLLLLIIIIIII\Documents\teachmegcse\teachmegcse-js\public\all.json"
output_json = "output_file.json"

# Function to extract the year from pdfName
def extract_year(pdf_name):
    try:
        # Extract the year from `_mYY`, `_wYY`, or `_sYY`
        for prefix in ['_m', '_w', '_s']:
            if prefix in pdf_name:
                year_part = pdf_name.split(prefix)[1][:2]  # Extract the two-digit year after the prefix
                # Convert year to four digits (e.g., '19' to '2019')
                return f"20{year_part}" if len(year_part) == 2 else year_part
    except Exception as e:
        print(f"Error processing pdfName: {pdf_name}, Error: {e}")
    return None

# Read the input JSON file
with open(input_json, "r") as infile:
    data = json.load(infile)  # Assumes the input file is a list of JSON objects

# Add the 'year' field to each JSON object
for question in data:
    question['year'] = extract_year(question.get('pdfName', ''))

# Save the updated data to the output JSON file
with open(output_json, "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Processed JSON file saved as {output_json}")
