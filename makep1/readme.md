# Script: makep1Final.py

This Python script automates the process of extracting images from PDF files, cropping the images, and generating question images. It is designed for use with Exceed.

## Purpose
- Convert PDF pages into images.
- Crop and clean the images to extract question sections.
- Save individual question images with specific dimensions and file naming conventions.

## Key Features

### 1. **PDF to Image Conversion**
- Utilizes the `pdf2image` library to convert PDF pages into JPEG images.
- Extracts all pages, excluding those marked "BLANK PAGE."

### 2. **Image Cropping**
- Crops images to remove headers and footers based on the `startPixel` variable.
- Additional cropping ensures images are focused on relevant question content.

### 3. **Image Cleaning**
- Detects and removes excess whitespace from the bottom of images.
- Ensures all images are cropped cleanly to display only question content.

### 4. **Dynamic Dimensions**
- Automatically calculates the dimensions of each question section within an image.
- Splits images into separate files for each question based on content detection.

### 5. **GUI File Selection**
- Uses `tkinter` for user interaction to select PDF files for processing.

## Script Details

### Parameters
- `subject`: Subject code for file naming.
- `paper_number`: Paper number for file naming.
- `startPage`: First page to start processing (default is 1).
- `startPixel`: Pixel height to begin cropping (default is 150).

### Output Structure
- Saves processed images into a folder structure:
  - Original PDF images.
  - Cropped and cleaned question images.
- File naming convention: `{subject}_{paper_number}_{question_number}.jpg`

### Libraries Used
- `pdf2image`: Converts PDF pages to images.
- `PIL` (Pillow): Image cropping and manipulation.
- `PyPDF2`: PDF text extraction to detect blank pages.
- `tkinter`: GUI for file selection.
- `os`: Directory management.

## How It Works
1. **File Selection**:
   - User selects one or more PDF files using a GUI file dialog.
2. **Image Conversion**:
   - Converts selected PDF pages to images.
   - Filters out blank pages.
3. **Cropping and Cleaning**:
   - Crops images to remove headers, footers, and excess whitespace.
   - Splits pages into question-specific sections.
4. **Question Images**:
   - Saves individual question images with a unique name.
5. **Cleanup**:
   - Ensures all images are properly formatted and stored in the designated directory.