# backend/utils/doc_processor.py
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter # type: ignore
from langchain.embeddings import OpenAIEmbeddings # type: ignore
import numpy as np
from .embeddings import SimpleEmbeddingModel  # import your embedding class
import openai

DOCUMENTS = []

embedding_model = SimpleEmbeddingModel()  # create the embedding instance

# 1️⃣ Add document chunks with embeddings
def add_document_chunks(chunks):
    for chunk in chunks:
        emb = embedding_model.embed_text(chunk)
        DOCUMENTS.append({"text": chunk, "embedding": emb})

# 2️⃣ Retrieve relevant chunks for a query
def retrieve_from_vector_db(query):
    query_embedding = embedding_model.embed_text(query)
    similarities = [np.dot(query_embedding, doc['embedding']) for doc in DOCUMENTS]
    top_indices = np.argsort(similarities)[-3:]  # get top 3 relevant chunks
    return [DOCUMENTS[i]['text'] for i in top_indices]

# 3️⃣ Generate RAG response using GPT
def generate_rag_response(query, chunks):
    context = "\n".join(chunks)
    prompt = f"Use the following context to answer the question:\n{context}\n\nQuestion: {query}\nAnswer:"
    
    response = openai.Completion.create(
        model="text-davinci-003",  # or "gpt-3.5-turbo"
        prompt=prompt,
        max_tokens=200
    )
    return response['choices'][0]['text'].strip()


def process_text(text: str, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

def create_embeddings(chunks: List[str]):
    embeddings_model = OpenAIEmbeddings()  # Make sure OPENAI_API_KEY is set
    embeddings = embeddings_model.embed_documents(chunks)
    return embeddings
