from fastapi import FastAPI ,Depends
from database import engine, Base
from models import user
from auth.auth_routes import auth_router  # ✅ import router
from auth.dependencies import get_admin_user, get_current_user
from models.user import User
from routes.landing import router as landing_router
from routes.admin import router as admin_router

app = FastAPI()

app.include_router(landing_router)
app.include_router(admin_router)
# Create tables
Base.metadata.create_all(bind=engine)

# Include auth routes
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "FastAPI and Database connected successfully!"}

@app.get("/admin")
def admin_page(admin_user: User = Depends(get_admin_user)):
    return {
        "message": f"Welcome admin {admin_user.username}"
    }
@app.get("/landing")
def landing_page(current_user: User = Depends(get_current_user)):
    return {
        "message": f"Welcome {current_user.username}",
        "email": current_user.email
    }
