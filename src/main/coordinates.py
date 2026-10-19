from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
import cv2
import numpy as np
from typing import List
import uvicorn
import os
import argparse
import threading

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))

app = FastAPI()
current_question_num = 0

# Argument parser for model selection - now loading both
parser = argparse.ArgumentParser(description="Start FastAPI app with YOLO models")
args, unknown = parser.parse_known_args()

import glob

# Models that are redundant and not worth the load time / GPU memory
SKIPPED_MODELS = {"long-double", "best"}

# Load all models
models = {}
model_files = glob.glob(f"{BASE_PATH}/resources/vision-models/*.pt")
for model_file in model_files:
    mode = os.path.splitext(os.path.basename(model_file))[0]
    if mode in SKIPPED_MODELS:
        continue
    try:
        models[mode] = YOLO(model_file)
        print(f"Loaded model: {model_file}")
    except Exception as e:
        raise RuntimeError(f"Failed to load YOLO model '{model_file}': {e}")

# YOLO models aren't safe to call from several threads at once, so each model gets a lock.
# Requests are handled on FastAPI's thread pool, so decoding and saving images still overlap between requests.
model_locks = {mode: threading.Lock() for mode in models}
# Protects current_question_num, which numbers the saved debug images
counter_lock = threading.Lock()

# Confidence levels
conf_levels = {
    "long-double-p3": 0.05,
    "parts": 0.3,
    "mcq": 0.15,
    "ms": 0.15,
}  # Add others if needed, default 0.15


@app.post("/predict")
def predict(
    mode: str = "long-double-p3", file: UploadFile = File(...)
) -> List[List[float]]:
    global current_question_num
    try:
        contents = file.file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None or image.size == 0:
            raise ValueError("Invalid image file provided")
        height, width = image.shape[:2]
        if height <= 0 or width <= 0:
            raise ValueError("Invalid image dimensions")

        conf = conf_levels.get(mode, 0.15)
        if mode not in models:
            mode = "long-double-p3"
        with model_locks[mode]:
            results = models[mode](image, save=False, conf=conf)

        boxes = []
        for box in results[0].boxes.xyxy:
            coords = [float(coord) for coord in box]
            boxes.append(coords)

            x1, y1, x2, y2 = map(int, coords)
            cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

        with counter_lock:
            filename = f"{current_question_num}.jpg"
            current_question_num += 1
        save_path = os.path.join(
            BASE_PATH, "resources", "images", "vision_output_images", filename
        )
        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        cv2.imwrite(save_path, image)

        print(f"Saved image with boxes to {save_path}")

        return boxes

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        raise HTTPException(status_code=500, detail=error_message)


if __name__ == "__main__":
    # Pass the app object rather than "coordinates:app" so uvicorn doesn't re-import this module and load every model twice
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
