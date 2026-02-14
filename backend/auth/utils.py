from database import get_db
from models.user import User

def get_user_by_username(db, username: str):
    return db.query(User).filter(User.username == username).first()
