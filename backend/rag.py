from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from utils import SECRET_KEY, ALGORITHM
from models import User
from database import get_db
from sqlalchemy.orm import Session

rag_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@rag_router.post("/rag/upload")
def upload_pdf(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    content = file.file.read()
    # Here you can process your PDF with RAG pipeline
    return {"filename": file.filename, "size": len(content)}
