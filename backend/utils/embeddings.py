# utils/embeddings.py
from dotenv import load_dotenv # type: ignore
import os
from openai import OpenAI

load_dotenv()  # loads variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SimpleEmbeddingModel:
    def embed_text(self, text):
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return response['data'][0]['embedding']
