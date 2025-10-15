import os
import json
import pandas as pd

# This file takes all json files then outputs a single csv


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
    data_frames = []

    for filename in json_files:
        file_path = os.path.join(base_path, filename)

        if not os.path.exists(file_path):
            print(f"⚠️ File not found: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Normalize to a list of dicts
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            print(f"⚠️ Unsupported JSON structure in {filename}")
            continue

        combined_data.extend(data)
        data_frames.append(pd.DataFrame(data))

    if not combined_data:
        print("❌ No valid JSON data found.")
        return

    # Save combined JSON
    combined_json_path = os.path.join(base_path, output_json)
    with open(combined_json_path, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Combined JSON saved to: {combined_json_path}")

    # Save combined CSV
    combined_df = pd.concat(data_frames, ignore_index=True)
    combined_csv_path = os.path.join(base_path, output_csv)
    combined_df.to_csv(combined_csv_path, index=False)
    print(f"✅ Combined CSV saved to: {combined_csv_path}")


# Example usage:
if __name__ == "__main__":
    base_path = "../resources/json"
    print(os.listdir(base_path))
    json_files = [
        "a_bio_final_long.json",
        "a_chem_final_long.json",
        "a_phy_final_long.json",
        "ig_bio_final_long.json",
        "ig_chem_final_long.json",
        "ig_phy_final.json",
    ]
    output_csv = "combined.csv"
    output_json = "all.json"
    combine_json_to_csv_and_json(base_path, json_files, output_csv, output_json)
