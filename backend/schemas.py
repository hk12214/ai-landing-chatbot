from pydantic import BaseModel

# ----------------------------
# Request models
# ----------------------------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

# ----------------------------
# Response models
# ----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str
