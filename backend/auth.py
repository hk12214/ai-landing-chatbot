from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User
from utils import hash_password, verify_password, create_access_token
from fastapi import UploadFile, File
auth_router = APIRouter()

# Example: a placeholder function for getting the current user
def get_current_user():
    # here you should check token/session
    # for now we return a dummy user
    class User:
        username = "Helen"
    return User()

# Protected route goes here
@auth_router.get("/protected")
async def protected_route(current_user=Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}"}


@auth_router.post("/auth/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User created"}

@auth_router.post("/auth/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}


@auth_router.post("/rag/upload")
async def upload_rag(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    contents = await file.read()
    # process contents
    return {"filename": file.filename, "size": len(contents)}
