# Data Generation Scripts

This bundle includes two Python scripts designed for generating structured datasets from predefined parameters for various academic subjects. These scripts are tailored for use with TeachMeGCSE/Exceed.

## Files Description

### 1. `6.py`
- **Purpose**:
  - Generates JSON entries for a single subject, creating structured metadata for academic papers, including links to mark schemes and question papers.
- **Key Features**:
  - Supports years ranging from 2011 to 2022.
  - Differentiates between March, Summer, and Winter sessions.
  - Provides URLs for both question papers (`qp`) and mark schemes (`ms`).
  - Handles different paper variants (e.g., `11`, `12`, `13`).
- **Output**:
  - A `data.json` file containing formatted JSON objects with the following fields:
    - `slug`: A unique identifier for each paper.
    - `src`: URL for the PDF resource.
    - `name`: Paper name and variant.
    - `msSrc`: URL for the corresponding mark scheme.
    - `isMs`: Indicates whether the file is a mark scheme.
    - `year`, `subjectName`, and `synonym`: Metadata for categorization.

### 2. `7.py`
- **Purpose**:
  - Extends the functionality of `6.py` to handle multiple subjects dynamically.
  - Reads subject configurations from a predefined dictionary to automate the creation of JSON entries for a wide range of academic subjects.
- **Key Features**:
  - Supports both A-level and IGCSE levels.
  - Handles multiple subjects, including Physics, Biology, Chemistry, Mathematics, etc.
  - Automatically adjusts for subjects with different paper structures and year ranges.
- **Output**:
  - A comprehensive `data.json` file with structured metadata for all configured subjects.

