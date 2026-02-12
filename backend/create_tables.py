# create_tables.py (run once)
from database import engine, Base
from models import User

Base.metadata.create_all(bind=engine)
print("Database tables created!")