import re
from extract_pdf import document_text 

def clean_and_chunk(text, chunk_size=500):
    
    text = re.sub(r'\s+', ' ', text.strip())
    
    
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

 
document_chunks = clean_and_chunk(document_text)
print(f"Document chunked into {len(document_chunks)} parts.")
