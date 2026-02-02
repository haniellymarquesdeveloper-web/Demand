from pydantic import BaseModel
from app.users.profiles import ProfileEnum

class User(BaseModel):
    name: str
    email: str
    profile:ProfileEnum


