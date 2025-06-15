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

# Argument parser for model selection
parser = argparse.ArgumentParser(description="Start FastAPI app with specific YOLO model")
parser.add_argument("--mode", type=str, default="best1", help="Model name without .pt extension (e.g., 'mcq' for mcq.pt)")
args, unknown = parser.parse_known_args()

model_path = f"{BASE_PATH}/resources/vision-models/{args.mode}.pt"

# Load the trained model
try:
    model = YOLO(model_path)
    print(f"Loaded model: {model_path}")
except Exception as e:
    raise RuntimeError(f"Failed to load YOLO model '{model_path}': {e}")


@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> List[List[float]]:
    global current_question_num
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Invalid image file provided")

        results = model(image, save=False, conf=0.1)

        boxes = []
        for box in results[0].boxes.xyxy:
            coords = [float(coord) for coord in box]
            boxes.append(coords)

            x1, y1, x2, y2 = map(int, coords)
            cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

        filename = f"{current_question_num}.jpg"
        current_question_num += 1
        save_path = os.path.join(BASE_PATH, "resources", "images", "vision_output_images", filename)
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
