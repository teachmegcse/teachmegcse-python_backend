# This script deletes files in the full_pdfs directory that do not contain "ms" or "qp" in their names.

from pathConst import PDF_PATH
import os

folders = os.listdir(PDF_PATH)
files_to_be_removed = []

for folder in folders:
    files = os.listdir(os.path.join(PDF_PATH, folder))
    for file in files:
        if ("ms" not in file) and ("qp" not in file):
            files_to_be_removed.append(os.path.join(PDF_PATH, folder, file))

for file in files_to_be_removed:
    print(f"Removing file: {file}")
    os.remove(file)
print("Files without 'ms' or 'qp' in their names have been removed.")