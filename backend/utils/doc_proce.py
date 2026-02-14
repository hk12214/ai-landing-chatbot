# backend/utils/doc_processor.py
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter # type: ignore
from langchain.embeddings import OpenAIEmbeddings # type: ignore
import numpy as np

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
