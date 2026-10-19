import json
from pathlib import Path
import os
import sys
from PIL import Image
import easyocr

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import get_dimensions_from_api

INPUT_JSON = f"{BASE_PATH}/resources/json/a_chem_theory.json"
OUTPUT_JSON = "questions_updated.json"
IMAGES_DIR = f"{BASE_PATH}/resources/images/a-level/chemistry/long"

reader = easyocr.Reader(["en"])


# Have to run coordinates.py at 0.5 confidence for some reason
# Mostly working but need to figure out how to remove the temps and make the OCR more accurate
def process_questions():
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)

    updated_questions = []

    for i, q in enumerate(questions):
        try:
            image_filename = q.get("questionName")

            if not image_filename:
                print(f"[WARN] Skipping index {i}: no questionName")
                updated_questions.append(q)
                continue

            image_path = Path(IMAGES_DIR) / image_filename

            if not image_path.exists():
                print(f"[WARN] Image not found: {image_path}")
                updated_questions.append(q)
                continue

            print(f"Processing {image_filename}...")

            parts = get_dimensions_from_api(str(image_path), mode="parts")

            parts = [[int(v) for v in box] for box in parts]

            parts_sorted = sorted(parts, key=lambda x: x[1])

            image = Image.open(image_path)

            question_parts = []
            for idx, box in enumerate(parts_sorted):
                x1, y1, x2, y2 = box

                if x1 > 250:
                    continue

                cropped = image.crop((x1, y1, x2, y2))

                save_path = Path(IMAGES_DIR) / f"temp_{i}_{idx}.jpg"
                cropped.save(save_path)
                part_text = reader.readtext(str(save_path))

                full_text = " ".join([t[1] for t in part_text]) if part_text else "(i)"

                question_parts.append(
                    {"coordinates": [x1, y1, x2, y2], "text": full_text}
                )

            q["questionParts"] = question_parts

            updated_questions.append(q)

        except Exception as e:
            print(f"[ERROR] Error processing {q.get('questionName')}: {e}")
            updated_questions.append(q)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(updated_questions, f, indent=2, ensure_ascii=False)

    print("[DONE] Done! Saved to", OUTPUT_JSON)


if __name__ == "__main__":
    process_questions()
