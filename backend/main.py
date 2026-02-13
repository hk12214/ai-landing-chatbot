from fastapi import FastAPI
from database import engine, Base
from models import user
from auth.auth_routes import auth_router  # ✅ import router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include auth routes
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "FastAPI and Database connected successfully!"}