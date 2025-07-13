from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    nombre: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
