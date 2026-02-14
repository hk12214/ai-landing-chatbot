from fastapi import Depends, HTTPException

from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database import get_db
from .utils import get_user_by_username



SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

def decode_access_token(token: str):
    """
    Decode a JWT token and return its payload.
    Raises JWTError if invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise e

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

from fastapi import Header, HTTPException, status

STATIC_TOKEN = "YOUR_SECRET_BEARER_TOKEN"

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise ValueError()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
        )

    if token != STATIC_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return {"username": "helen"}
