# Social Media Content Analyzer

## Overview

The Social Media Content Analyzer is a web-based application designed to analyze uploaded documents (PDFs and images) by extracting text content and suggesting improvements to increase engagement on social media. It leverages OCR (Optical Character Recognition) for image files and PDF parsing for text extraction. The project is built using Python, Flask, and various libraries for processing documents.

---

## Features

### 1. Document Upload
- Supports uploading of PDFs and image files (PNG, JPG, JPEG).
- Provides a drag-and-drop or file picker interface for ease of use.

### 2. Text Extraction
- Extracts text content from PDFs while preserving formatting using `pdfplumber`.
- Utilizes Tesseract OCR for extracting text from scanned images or photos.

### 3. User Experience Enhancements
- Displays extracted text directly on the webpage.
- Provides error messages for unsupported file types or processing errors.
- Loading indicators for file processing to enhance user experience.

### 4. Modular Design
- Built with modularity and scalability in mind for future enhancements, such as AI-based text analysis and engagement suggestions.

---

## Technical Details

### Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **OCR:** Tesseract
- **PDF Parsing:** pdfplumber

### Folder Structure
```plaintext
project-root/
|-- app/
|   |-- static/               # Static files (CSS, JS, images)
|   |-- templates/            # HTML templates
|   |-- uploads/              # Temporary storage for uploaded files
|   |-- app.py                # Main Flask application file
|-- README.md                 # Documentation
|-- requirements.txt          # Python dependencies
```

---

## Prerequisites

1. Python 3.7 or later.
2. Pip (Python package manager).
3. Tesseract OCR installed on your system:
   - **Linux (Ubuntu):**
     ```bash
     sudo apt install tesseract-ocr
     ```
   - **Windows:**
     Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python app/app.py
   ```

4. **Access the App:**
   - Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

1. Navigate to the application in your web browser.
2. Upload a PDF or image file using the provided interface.
3. View the extracted text displayed directly on the page.

---

## Future Enhancements

- Implement AI/ML-based suggestions for text improvement (e.g., readability, engagement).
- Add multi-language OCR support.
- Extend file support to include DOCX and other document types.
- Enable saving extracted text to downloadable files.

---

## Dependencies

- **Flask:** Web framework for building the application.
- **pytesseract:** OCR library for extracting text from images.
- **pdfplumber:** Library for parsing and extracting text from PDFs.
- **Pillow:** Image processing library.
- **Werkzeug:** For secure file handling.

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

---

## Contributing

Feel free to fork this repository, open issues, or submit pull requests to contribute to the project.
