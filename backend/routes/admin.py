# routes/admin.py
from fastapi import APIRouter, Depends, UploadFile, File # type: ignore
from auth.dependencies import get_admin_user
from utils.doc_proce import process_text, create_embeddings ,add_document_chunks


router = APIRouter()

@router.post("/admin/upload")
async def upload_document(file: UploadFile = File(...), admin=Depends(get_admin_user)):
    contents = await file.read()
    # TODO: Process file -> extract text, create embeddings, store in vector DB
    return {"filename": file.filename, "message": "File uploaded successfully"}