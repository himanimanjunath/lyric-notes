import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text

if __name__ == "__main__":
    pdf_path = input("Enter the full path of the PDF file: ")  # User inputs PDF path
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        print("\nExtracted Text:\n", extracted_text)
    except Exception as e:
        print("Error:", e)
