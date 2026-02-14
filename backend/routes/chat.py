from fastapi import APIRouter, Depends # type: ignore
from auth.jwt_handler import get_current_user
from utils.doc_proce import DOCUMENTS, add_document_chunks ,retrieve_from_vector_db, generate_rag_response

router = APIRouter()


@router.post("/chat")
async def chat(query: str):
    # Now current_user is validated
    relevant_chunks = retrieve_from_vector_db(query)  # type: ignore
    answer = generate_rag_response(query, relevant_chunks)  # type: ignore
    return {"answer": answer}