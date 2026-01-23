import os

FOLDER_PATH = "/home/mm2/Work/teachmegcse/python/teachmegcse-python_backend/src/resources/Classified_pdfs/9708"
SKIP_STRINGS = ["gt", "ci", "er", "ir"]

def clean_folder():
    if not os.path.isdir(FOLDER_PATH):
        print(f"Not a directory: {FOLDER_PATH}")
        return

    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, filename)

        if not os.path.isfile(file_path):
            continue

        name_lower = filename.lower()

        matched = [s for s in SKIP_STRINGS if s in name_lower]

        if matched:
            print(f"Deleting: {filename} (matched: {', '.join(matched)})")
            os.remove(file_path)

if __name__ == "__main__":
    clean_folder()
