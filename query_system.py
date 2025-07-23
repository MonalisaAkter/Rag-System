import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from evaluation import evaluate_model
from gpt_integration import generate_answer_with_gpt3

def generate_answer(relevant_chunks):
    
    answer = generate_answer_with_gpt3(relevant_chunks)
    return answer


def evaluate_relevance(query, relevant_chunks, ground_truth):
    precision, recall, f1 = evaluate_model(relevant_chunks, ground_truth)
    print(f"Precision: {precision}, Recall: {recall}, F1 Score: {f1}")
    return precision, recall, f1

 
ground_truth = ["expected answer or chunk"]   
evaluate_relevance(query, relevant_chunks, ground_truth)


 
pc = Pinecone(api_key="pcsk_5iMHi5_BEF6WSgJCDTPkejoqqRw7rMvBWEUa52Edyq21rSy6KMQUjPvyTsSUDzwcXVzv9x")  
 

 
index = pc.Index("bangla-paper-index")

 
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def query_rag_system(query, top_k=3):
     
    query_embedding = model.encode([query])
    
     
    result = index.query(query_embedding, top_k=top_k, include_metadata=True)
    
     
    relevant_chunks = [item['metadata'] for item in result['matches']]
    
    return relevant_chunks

def generate_answer(relevant_chunks):
    return " ".join(relevant_chunks)

def evaluate_relevance(query, relevant_chunks):
    query_embedding = model.encode([query])
    chunk_embeddings = model.encode(relevant_chunks)
    similarities = cosine_similarity([query_embedding], chunk_embeddings)
    avg_similarity = np.mean(similarities)
    return avg_similarity

 
query = "অনপুেমর ভাষায় সুপুরুষ কােক বলা হেয়েছ?"
relevant_chunks = query_rag_system(query)
answer = generate_answer(relevant_chunks)

 
avg_similarity = evaluate_relevance(query, relevant_chunks)

print(f"Generated Answer: {answer}")
print(f"Average Relevance Score: {avg_similarity}")
