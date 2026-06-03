from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
import cv2
import numpy as np
from typing import List
import uvicorn
import os
import argparse

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))

app = FastAPI()
current_question_num = 0

# Argument parser for model selection - now loading both
parser = argparse.ArgumentParser(description="Start FastAPI app with YOLO models")
args, unknown = parser.parse_known_args()

import glob

# Load all models
models = {}
model_files = glob.glob(f"{BASE_PATH}/resources/vision-models/*.pt")
for model_file in model_files:
    mode = os.path.splitext(os.path.basename(model_file))[0]
    try:
        models[mode] = YOLO(model_file)
        print(f"Loaded model: {model_file}")
    except Exception as e:
        raise RuntimeError(f"Failed to load YOLO model '{model_file}': {e}")

# Confidence levels
conf_levels = {
    "long-double": 0.15,
    "parts": 0.3,
    "mcq": 0.15,
    "ms": 0.15,
}  # Add others if needed, default 0.15


@app.post("/predict")
async def predict(
    mode: str = "long-double", file: UploadFile = File(...)
) -> List[List[float]]:
    global current_question_num
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None or image.size == 0:
            raise ValueError("Invalid image file provided")
        height, width = image.shape[:2]
        if height <= 0 or width <= 0:
            raise ValueError("Invalid image dimensions")

        model = models.get(mode, models["long-double"])
        conf = conf_levels.get(mode, 0.15)
        results = model(image, save=False, conf=conf)

        boxes = []
        for box in results[0].boxes.xyxy:
            coords = [float(coord) for coord in box]
            boxes.append(coords)

            x1, y1, x2, y2 = map(int, coords)
            cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

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
    uvicorn.run("coordinates:app", host="127.0.0.1", port=8000, reload=False)
