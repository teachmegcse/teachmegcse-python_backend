# Exam Processing Automation

This repository contains a collection of Python scripts that automate the classification, processing, and generation of exam materials, including questions, answers, and structured PDFs. It supports AI-assisted workflows, OCR-based text extraction, and machine learning-driven classification for efficient academic content management.

## Features

- **PDF Processing**: Convert exam paper PDFs into structured images and extract relevant content.
- **Classification & Sorting**: Categorize questions and answers into topics, chapters, and subjects.
- **AI & OCR Integration**: Enhance question detection and text extraction for improved accuracy.
- **Metadata & JSON Handling**: Automate structured data creation for easy reference and integration.
- **Machine Learning**: Train and use ML models for syllabus classification and content prediction.

## Key Scripts

### 1. **Web API for PDF Generation**

- **`p1_api.py`**: Implements a FastAPI service to generate and serve classified PDFs.
- **`p1_fixed.py`**: Generates classified PDFs from a predefined JSON database.
- **`p1_images_to_classified.py`**: Creates structured question PDFs with optional chapters, indexes, and mark schemes.

### 2. **Exam Paper Metadata Generation**

- **`6.py`**: Generates structured JSON metadata for individual subjects, linking questions to mark schemes.
- **`7.py`**: Extends `6.py` to handle multiple subjects dynamically, creating a unified `data.json` file.

### 3. **Image Processing & Question Extraction**

- **`makep1-new2.py`**: Extracts question images from PDFs, cleans and crops them, and saves them in a structured format.
- **`makep4.py`**: Extracts images from exam PDFs, removes irrelevant sections, and saves structured question images.
- **`makep4-ai.py`**: Enhances `makep4.py` using AI to detect and crop question regions dynamically.
- **`p4_ms_maker.py`**: Processes mark schemes to extract question-specific sections using OCR.
- **`p4_ms_maker_ai.py`**: Uses AI to improve mark scheme question detection and extraction.
- **`p4ms-images-maker.py`**: Cleans and preprocesses mark scheme images.

### 4. **Machine Learning & NLP Processing**

- **`.joblib`**\*\* Files\*\*: Pre-trained machine learning models for syllabus classification.
- **`predictData.py`**: Uses trained models to classify syllabus content into topics.
- **`trainModels.py`**: Trains machine learning models for syllabus classification using NLP techniques.
- **`trainWithPdfs.py`**: Extracts text from PDFs and trains models based on syllabus content.
- **`getFormattedTextfromPdf.py`**: Extracts and preprocesses text from syllabus PDFs.

### 5. **Data Organization & Formatting**

- **`combine_json.py`**: Merges question and mark scheme data into structured chapter-based directories.
- **`format-json.py`**: Cleans and merges JSON data for consistent formatting.
- **`makeMSforAutomateSort2.py`**: Extracts answers from mark schemes and organizes them using OCR and ML.
- **`MS2.py`**: Extracts answers from mark scheme PDFs using text pattern analysis.

## Output Structure

- **PDFs**: Processed question and answer booklets.
- **Images**: Cropped and structured question images.
- **JSON**: Metadata containing structured exam content.

## Libraries Used

- `FastAPI`, `pdf2image`, `PIL`, `PyPDF2`, `pytesseract`, `scikit-learn`, `tkinter`

## Usage

1. Run `p1_api.py` to serve the PDF generation API.
2. Use `makep1-new2.py` or `makep4.py` to extract question images from PDFs.
3. Use `6.py` and `7.py` to generate JSON metadata.
4. Train or use ML models with `trainModels.py` and `predictData.py`.
5. Organize and format JSON data with `combine_json.py` and `format-json.py`.

## Conclusion

This repository provides a comprehensive solution for automating the processing and organization of exam papers, leveraging AI, OCR, and machine learning for accuracy and efficiency.
