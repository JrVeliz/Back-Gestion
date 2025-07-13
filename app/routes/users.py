from fastapi import APIRouter, HTTPException
from app.schemas.User import UserRegister, UserLogin
from app.services import user_services
from app.utils.response import success_response, error_response

router = APIRouter()

@router.post("/register-user")
def register(user: UserRegister):
    if user_services.obtener_usuario_por_email(user.email):
        return error_response(message="Email ya registrado", status_code=400)
    
    user_services.crear_usuario(user.nombre, user.email, user.password)
    return success_response(message="Usuario registrado exitosamente")

@router.post("/login")
def login(user: UserLogin):
    usuario = user_services.obtener_usuario_por_email(user.email)
    if not usuario or usuario.password != user.password:
        return error_response(message="Credenciales inválidas", status_code=401)
    
    return success_response(message="Login exitoso")
