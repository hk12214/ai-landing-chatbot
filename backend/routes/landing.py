# main.py or routes/landing.py
from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user

router = APIRouter()

@router.get("/landing")
async def landing_page(current_user = Depends(get_current_user)):
    return {"message": f"Welcome to the landing page, {current_user.username}!"}