import os
from pinecone import Pinecone, ServerlessSpec
from vectorization import embeddings   

# Initialize Pinecone instance
pc = Pinecone(api_key="pcsk_5iMHi5_BEF6WSgJCDTPkejoqqRw7rMvBWEUa52Edyq21rSy6KMQUjPvyTsSUDzwcXVzv9x")   
index_name = "bangla-paper-index"
if index_name not in pc.list_indexes().names():   
    print(f"Creating index: {index_name}")
    pc.create_index(
        name=index_name,
        dimension=embeddings.shape[1],   
        metric="cosine",   
        spec=ServerlessSpec(
            cloud="aws",   
            region="us-west-2"   
        )
    )
else:
    print(f"Index {index_name} already exists.")
 
index = pc.Index(index_name)

 
index.upsert([(str(i), embedding) for i, embedding in enumerate(embeddings)])
print("Embeddings stored in Pinecone.")

 
print(pc.list_indexes().names())