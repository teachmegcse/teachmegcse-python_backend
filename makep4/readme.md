# Detailed File Descriptions

Below is a detailed breakdown of each Python script in the folder, including its purpose, features, and functions.

---

## **1. makep4.py**
- **Purpose**: Extracts and organizes images of questions from exam paper PDFs.
- **Features**:
  - Converts PDF pages into high-resolution images using `pdf2image`.
  - Detects and removes irrelevant pages (e.g., "BLANK PAGE").
  - Crops images to focus on relevant content such as questions.
  - Saves images with structured filenames and generates JSON metadata.

### Key Functions:
1. **`convert_from_path(pdf_path)`**:
   - Converts PDF pages into images.
   - Returns a list of images corresponding to each PDF page.

2. **`strip_images(output_path, i)`**:
   - Crops unnecessary content (headers, footers) from images.
   - Saves the cleaned images in the specified output folder.

3. **`process_pdf(pdf_path, output_path, subject, paper_number)`**:
   - Manages the full workflow:
     - Converts the PDF to images.
     - Strips unnecessary content from images.
     - Saves images with a naming convention like `{subject}_{paper_number}_{question_number}.jpg`.

4. **`save_metadata(output_path, metadata)`**:
   - Creates a JSON file containing metadata for the processed questions, including filenames, question numbers, and source PDFs.

---

## **2. makep4-ai.py**
- **Purpose**: Enhances `makep4.py` by integrating AI to detect and crop question regions dynamically.
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

## **3. p4_ms_maker.py**
- **Purpose**: Processes mark scheme PDFs to extract question-specific sections.
- **Features**:
  - Uses OCR to detect question numbers within the mark schemes.
  - Dynamically splits pages into question-specific sections.
  - Generates images and metadata for each question.

### Key Functions:
1. **`preprocess_image_for_ocr(image)`**:
   - Enhances the image (grayscale conversion, resizing) to improve OCR accuracy.

2. **`extract_question_numbers(image)`**:
   - Uses OCR to detect text regions likely to contain question numbers.
   - Returns a list of coordinates for detected regions.

3. **`split_mark_scheme(image, question_regions)`**:
   - Splits the mark scheme image into question-specific sections based on OCR-detected regions.

4. **`generate_metadata(output_path, question_sections)`**:
   - Creates a JSON file with metadata, including:
     - Question numbers.
     - Corresponding filenames.
     - Source PDF information.

---

## **4. p4_ms_maker_ai.py**
- **Purpose**: Extends `p4_ms_maker.py` with AI-assisted question detection for increased accuracy.
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

## **5. p4ms-images-maker.py**
- **Purpose**: Processes mark scheme images by applying basic cropping and cleaning.
- **Features**:
  - Strips unnecessary content (headers, footers).
  - Prepares images for further processing or direct use.

### Key Functions:
1. **`strip_images(output_path)`**:
   - Crops predefined regions from images (e.g., removes headers).
   - Saves the cleaned images.

2. **`process_pdf_mark_scheme(pdf_path, output_path)`**:
   - Converts a PDF into images.
   - Applies basic cleaning to each image.
   - Saves the processed images in a structured format.

---

## **6. phy_db_final_p4.json**
- **Purpose**: A JSON file containing metadata for processed exam papers and mark schemes.
- **Structure**:
  - `questionName`: Name of the question image file.
  - `MSName`: Name of the corresponding mark scheme image file.
  - `questionNumber`: The question number.
  - `pdfName`: Source PDF file name.
  - `year`: Year of the exam paper.
  - `Subject`: Subject (e.g., Physics, Chemistry).
  - `Level`: Academic level (e.g., AS, A2).
  - `Chapter`: Chapter or topic number.
  - `paperNumber`: The specific paper number.
