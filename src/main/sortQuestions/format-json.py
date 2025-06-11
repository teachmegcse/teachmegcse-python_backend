import json
import re
import os
import csv

# List of file paths to read
files = [
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_phy_p2_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_phy_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_eco_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_chem_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_chem_p2_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_bio_p2_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\IG_bio_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\A_phy_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\A_eco_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\A_eco_p3_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\A_chem_p1_db.json",
    r"C:\Users\ALLLLLLIIIIIII\Downloads\A_bio_p1_db.json"
]

# List to hold combined data
combined_data = []

# Function to remove asterisks from text fields
def remove_asterisks(text):
    return re.sub(r'\*', '', text)

# Read and combine data from each file
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

            # Check if data is a list or dictionary
            if isinstance(data, list):
                # Process each item in the list
                for item in data:
                    if isinstance(item, dict):
                        # Remove asterisks in explanations within each dictionary item
                        for key, value in item.items():
                            if isinstance(value, str) and "Explanation" in key:
                                item[key] = remove_asterisks(value)
                        combined_data.append(item)
            elif isinstance(data, dict):
                # Process the single dictionary directly
                for key, value in data.items():
                    if isinstance(value, str) and "Explanation" in key:
                        data[key] = remove_asterisks(value)
                combined_data.append(data)

    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except json.JSONDecodeError:
        print(f"Warning: Could not decode JSON in {file}.")

# Write the combined data to a new JSON file
output_file_json = "combined_data.json"
with open(output_file_json, "w", encoding="utf-8") as outfile:
    json.dump(combined_data, outfile, indent=4)

# Convert the combined data to CSV format
output_file_csv = "combined_data.csv"
if combined_data:
    # Get the headers from the keys of the first dictionary
    headers = combined_data[0].keys()

    # Write data to CSV with UTF-8 encoding
    with open(output_file_csv, "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(combined_data)

print(f"Data combined successfully into {output_file_json} and {output_file_csv}")
