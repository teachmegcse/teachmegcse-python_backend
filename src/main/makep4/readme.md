# Detailed File Descriptions

Below is a detailed breakdown of each Python script in the folder, including its purpose, features, and functions.

---

## **1. makep4-ai.py**
- **Purpose**: Integrates AI to detect and crop long answer questions' regions dynamically.
- **Features**:
  - Communicates with an AI API for question detection.
  - Dynamically crops questions based on AI-detected bounding boxes.
  - Generates question-specific images and metadata.

### Key Functions:
1. **`call_ai_api(image)`**:
   - Sends an image to the AI service.
   - Returns a list of bounding boxes for detected questions.

2. **`crop_image_by_ai(image, bounding_boxes)`**:
   - Crops the image into sections based on the AI-detected bounding boxes.
   - Each bounding box corresponds to a single question.

3. **`save_ai_cropped_images(output_path, cropped_images)`**:
   - Saves the AI-cropped images with filenames indicating the question numbers.

4. **`process_with_ai(pdf_path, output_path, subject, paper_number)`**:
   - Integrates all steps:
     - Converts the PDF to images.
     - Calls the AI API for question detection.
     - Crops and saves question-specific images.

---

## **2. p4_ms_maker_ai.py**
- **Purpose**: AI-assisted mark scheme splitting for increased accuracy.
- **Features**:
  - Integrates with an AI service to detect question boundaries in mark schemes.
  - Handles diverse layouts and formats more effectively than traditional OCR.

### Key Functions:
1. **`call_ai_service(image)`**:
   - Sends the image to an external AI service for question boundary detection.
   - Returns bounding boxes for question regions.

2. **`crop_question_sections(image, bounding_boxes)`**:
   - Crops question-specific sections using AI-detected bounding boxes.

3. **`save_cropped_mark_schemes(output_path, cropped_sections)`**:
   - Saves cropped mark scheme images.

4. **`process_mark_scheme_with_ai(pdf_path, output_path)`**:
   - Executes the full pipeline:
     - Converts PDFs to images.
     - Detects question regions using AI.
     - Crops and saves question-specific sections.

---