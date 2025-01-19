import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
import fitz  

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(filepath):
    """Extracts text from a PDF, handling both text-based and scanned PDFs."""
    extracted_text = ""
    pdf_document = fitz.open(filepath)

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        page_text = page.get_text()

        if page_text.strip():  
            extracted_text += page_text + "\n"
        else:  
            images = page.get_images(full=True)
            for img_index, image in enumerate(images):
                xref = image[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]

                temp_image_path = f"temp_image_{page_number}_{img_index}.png"
                with open(temp_image_path, "wb") as img_file:
                    img_file.write(image_bytes)

                img = Image.open(temp_image_path)
                ocr_text = pytesseract.image_to_string(img)
                extracted_text += ocr_text + "\n"

                os.remove(temp_image_path)

    pdf_document.close()
    return extracted_text

# Flask routes
@app.route('/')
def index():
    """Render the upload page."""
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads and text extraction."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            if filename.lower().endswith('.pdf'):
                extracted_text = extract_text_from_pdf(filepath)
            else:
                image = Image.open(filepath)
                extracted_text = pytesseract.image_to_string(image)

            # Format the text for HTML rendering
            extracted_text = extracted_text.replace('\n', '<br>')
            return jsonify({"text": extracted_text})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Unsupported file type."}), 400

if __name__ == '__main__':
    app.run(debug=True)

    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
