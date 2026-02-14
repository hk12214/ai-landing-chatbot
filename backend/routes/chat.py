from fastapi import APIRouter, Depends # type: ignore
from auth.jwt_handler import get_current_user

router = APIRouter()

@router.post("/chat")
async def chat(query: str, current_user=Depends(get_current_user)):
    # Retrieve relevant document chunks from your vector DB
    relevant_chunks = retrieve_from_vector_db(query) # type: ignore

    # Generate response (RAG)
    answer = generate_rag_response(query, relevant_chunks) # type: ignore
    return {"answer": answer}
