import os
import csv
import json

# This file takes all json files then outputs a single csv


def csv_value(value):
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return value


def combine_json_to_csv_and_json(base_path, json_files, output_csv, output_json):
    """
    Combines multiple JSON files into one combined JSON and CSV file.

    Parameters:
        base_path (str): Folder containing the JSON files.
        json_files (list): List of JSON filenames (e.g. ["a.json", "b.json"]).
        output_csv (str): Name of the output CSV file (e.g. "combined.csv").
        output_json (str): Name of the output JSON file (e.g. "combined.json").
    """
    combined_data = []

    for filename in json_files:
        file_path = os.path.join(base_path, filename)

        if not os.path.exists(file_path):
            print(f"[WARN] File not found: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Normalize to a list of dicts
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            print(f"[WARN] Unsupported JSON structure in {filename}")
            continue

        combined_data.extend(data)

    if not combined_data:
        print("[ERROR] No valid JSON data found.")
        return

    # Save combined JSON
    combined_json_path = os.path.join(base_path, output_json)
    with open(combined_json_path, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=2)
    print(f"[DONE] Combined JSON saved to: {combined_json_path}")

    # Save combined CSV, with every field in any of the files as a column. Lists and dicts (questionParts) are written
    # as JSON and missing values as empty cells, the rest as they are in the JSON (pandas turned them into Python
    # reprs, and int columns with a missing value into floats like 6.0)
    columns = list(dict.fromkeys(key for row in combined_data for key in row))
    combined_csv_path = os.path.join(base_path, output_csv)
    with open(combined_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in combined_data:
            writer.writerow({key: csv_value(row.get(key)) for key in columns})
    print(f"[DONE] Combined CSV saved to: {combined_csv_path}")


# Example usage:
if __name__ == "__main__":
    base_path = "../resources/json"
    print(os.listdir(base_path))
    json_files = [
        "ig_chem_final_long.json",
    ]
    output_csv = "combined.csv"
    output_json = "all.json"
    combine_json_to_csv_and_json(base_path, json_files, output_csv, output_json)
