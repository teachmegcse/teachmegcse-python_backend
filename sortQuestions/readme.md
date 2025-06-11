# Detailed File Descriptions

## **1. combine_json.py**
- **Purpose**: Combines question and mark scheme data from JSON files into a single JSON file, with files sorted into chapter-based directories.
- **Features**:
  - Processes question paper (`QP`) and mark scheme (`MS`) JSON files.
  - Uses OCR (`pytesseract`) to extract text from images and classify content into chapters.
  - Assigns questions and mark schemes to specific chapters based on a machine learning model.

### Key Functions:
1. **`normalize_paper_code(code)`**:
   - Cleans and standardizes the paper codes for consistency.
   - Example: Removes `_ms_` and `_qp_` substrings.

2. **`process_image(image_path, custom_config)`**:
   - Reads an image and extracts its text content using `pytesseract`.

3. **`predict(data, model)`**:
   - Uses a pre-trained machine learning model to predict the chapter of a question based on text.

4. **`copy_files_to_chapter_folders(question_name, ms_name, chapter_num)`**:
   - Copies question and mark scheme files to their respective chapter directories.

5. **`combineJSON(MSjson, QPjson, jsonDirectory)`**:
   - Combines data from `QP` and `MS` JSON files, processes entries, and saves the results in a new JSON file.

---

## **2. format-json.py**
- **Purpose**: Formats and combines multiple JSON files into a single file, optionally removing unnecessary characters like asterisks.
- **Features**:
  - Reads data from multiple JSON files.
  - Cleans up text fields by removing asterisks or unwanted characters.
  - Outputs a combined JSON file and a CSV file for compatibility.

### Key Functions:
1. **`remove_asterisks(text)`**:
   - Removes asterisks (`*`) from text fields to clean explanations or notes.

2. **Main Processing Loop**:
   - Iterates through each file in the `files` list.
   - Processes each entry and cleans up text fields as needed.

3. **Combined Output**:
   - Outputs cleaned and formatted data into:
     - A single JSON file (`combined_data.json`).
     - A CSV file (`combined_data.csv`).

---

## **3. getFormattedTextfromPdf.py**
- **Purpose**: Extracts, cleans, and formats text from PDF files for further processing.
- **Features**:
  - Uses `PyPDF2` to extract text from PDF pages.
  - Applies NLP techniques (tokenization, stemming, stopword removal) to preprocess the text.

### Key Functions:
1. **`getPdfText(pdfPath)`**:
   - Reads all pages of a PDF and extracts text while ignoring irrelevant sections.

2. **`makeText(pdfPath)`**:
   - Converts text to lowercase, removes punctuation, and applies stemming and stopword removal.
   - Specifically removes Cambridge command words like "analyse" and "describe."

3. **`formatText(text)`**:
   - Cleans and preprocesses a given string using the same logic as `makeText`.

---
