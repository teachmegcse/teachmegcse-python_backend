# Overview

These Python scripts automate the classification and generation of PDFs for exam questions and answers.

## Files Description

### 1. `p1_api.py`
- **Purpose**: 
  - Implements a FastAPI web service for generating and serving classified PDFs.
  - Handles requests to generate question and answer PDFs based on input JSON data.
- **Key Features**:
  - Supports cross-origin resource sharing (CORS) to allow external applications to interact.
  - Processes input data (e.g., questions and their attributes) to create structured PDFs.
  - Combines multiple PDFs into a single downloadable ZIP file.
- **Endpoints**:
  - `/`: A root endpoint that returns a simple "Hello World" message.
  - `/generate-pdf/`: Accepts JSON input (`QuestionsList`) and generates a ZIP file containing `questions.pdf` and `answers.pdf`.

### 2. `p1_fixed.py`
- **Purpose**: 
  - script to generate classified and answer PDFs from a predefined JSON file.
- **Key Features**:
  - Reads a JSON database of classified questions.
  - Outputs PDFs with questions and corresponding answers.
  - Includes page numbering and aesthetic layouts.
  - Combines generated PDFs into a single ZIP file for easier sharing.

### 3. `p1_images_to_classified.py`
- **Purpose**: 
  - Generates classified PDFs with chapters, questions, indexes and mark schemes, although those are all optional to facilitate the creation of worksheets through these tools
- **Key Features**:
  - Reads question images from a directory and organizes them into chapters.
  - Adds optional chapter title pages, advertisement banners, and indexes.
  - Merges classified questions with mark schemes into a single PDF, if enabled.
  - Highly configurable through parameters like `hasIndex`, `hasChapterPages`, and `hasMS`.