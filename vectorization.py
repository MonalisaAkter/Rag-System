from sentence_transformers import SentenceTransformer
from chunking import document_chunks   
 
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
 
embeddings = model.encode(document_chunks)

print("Embeddings generated for document chunks.")
