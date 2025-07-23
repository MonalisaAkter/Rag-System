# Retrieval-Augmented Generation (RAG) System

## Project Overview

The **Retrieval-Augmented Generation (RAG) System** is a system that combines document retrieval and natural language generation to answer queries based on a document. This implementation allows you to query a **Bangla** PDF document, retrieve relevant text chunks, and generate answers using **Pinecone** (for vector-based storage and retrieval) and **GPT-3** (for generating detailed answers).

## Features
- **PDF Text Extraction**: Extract text from Bangla PDF documents (e.g., HSC26 Bangla 1st Paper).
- **Text Chunking**: Process the extracted text into smaller, manageable chunks for efficient retrieval.
- **Embedding Generation**: Use **Sentence-BERT** to generate semantic embeddings for the document chunks.
- **Pinecone Integration**: Store the embeddings in **Pinecone** for fast similarity search.
- **Flask API**: A simple web-based API for querying the system.
- **Evaluation Metrics**: Precision, Recall, and F1 Score to evaluate the relevance of retrieved chunks.
- **GPT-3 Integration**: Use **GPT-3** to generate detailed and coherent answers based on retrieved chunks.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MonalisaAkter/Rag-System.git
cd Rag-System
