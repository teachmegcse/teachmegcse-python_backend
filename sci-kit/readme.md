# README: Training, Prediction, and Syllabus Processing Scripts

This folder contains Python scripts and pre-trained models (`.joblib` files) for processing syllabus data, training machine learning models, and making predictions. These tools classify academic content into topics or chapters, leveraging NLP and supervised machine learning techniques.

---

## General Overview of `.joblib` Files
The `.joblib` files are pre-trained machine learning models for various subjects and academic levels (e.g., IGCSE, AS, A2). Each `.joblib` file represents a trained model specific to a subject or syllabus, enabling prediction tasks such as topic classification and chapter identification.

These files are used in conjunction with the `predictData.py` script for making predictions.

---

## Detailed File Descriptions

### **1. predictData.py**
- **Purpose**: Makes predictions on syllabus content using pre-trained `.joblib` models.
- **Features**:
  - Processes input text (e.g., syllabus or question text) using NLP techniques.
  - Loads the appropriate `.joblib` model and predicts the corresponding topic or chapter.

#### Key Functions:
1. **`predict(data, model)`**:
   - Preprocesses input text by cleaning and removing irrelevant characters.
   - Loads the specified `.joblib` model and predicts the label for the input data.
2. **`printLabel(data, model)`**:
   - A wrapper for the `predict` function, displaying predictions in a readable format.

---

### **2. trainModels.py**
- **Purpose**: Trains machine learning models for syllabus classification tasks.
- **Features**:
  - Implements an NLP pipeline using `CountVectorizer` and a Naive Bayes classifier.
  - Saves trained models as `.joblib` files for later use.

#### Key Functions:
1. **`train(data, label)`**:
   - Accepts labeled training data.
   - Trains a Naive Bayes model using a pipeline that includes text vectorization.
   - Outputs a `.joblib` file containing the trained model.

---

### **3. trainWithPdfs.py**
- **Purpose**: Trains models using text extracted from PDFs of syllabus documents.
- **Features**:
  - Reads PDF files containing syllabus content, extracts text, and preprocesses it.
  - Labels the text based on chapters or topics and trains a classification model.

#### Key Components:
1. **PDF Text Extraction**:
   - Uses `getFormattedTextfromPdf.py` to extract and clean text from PDFs.
2. **Model Training**:
   - Calls `trainModels.py` to train a model on the extracted text and its labels.

---

### **4. getFormattedTextfromPdf.py**
- **Purpose**: Extracts and preprocesses text from PDF files for training or prediction.
- **Features**:
  - Removes unnecessary content like punctuation, stopwords, and digits.
  - Applies NLP techniques such as stemming and tokenization.
  - Focuses on educational keywords by removing command words like "analyze" or "describe."

#### Key Functions:
1. **`getPdfText(pdfPath)`**:
   - Extracts raw text from all pages of a PDF.
2. **`makeText(pdfPath)`**:
   - Cleans and preprocesses the extracted text for training or prediction.
3. **`formatText(text)`**:
   - Applies similar preprocessing to a given string of text.

---

### **5. Syllabus-Based Training Scripts**
- **Purpose**: Train machine learning models for specific subjects and academic levels.
- **Features**:
  - Prepares labeled training data directly from syllabus content for individual subjects.
  - Calls `trainModels.py` to train models for each syllabus.

These scripts are specialized for different subjects (e.g., Biology, Chemistry, Economics) and levels (e.g., IGCSE, AS, A2). They produce subject-specific `.joblib` files.

---

