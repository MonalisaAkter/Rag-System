import fitz   

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
 
pdf_path = "HSC26-Bangla1st-Paper.pdf"   
document_text = extract_pdf_text(pdf_path)
print("PDF text extracted successfully.")
