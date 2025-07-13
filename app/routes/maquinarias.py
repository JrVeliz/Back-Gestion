from fastapi import APIRouter
from app.schemas.maquinaria_input import RegistroMaquinaria
from app.services import maquinaria_services
from app.utils.response import success_response, error_response

router = APIRouter()

@router.post("/registrar-maquinaria")
def register(maquinaria: RegistroMaquinaria):
    if maquinaria_services.obtener_maquinaria(maquinaria.nombre, maquinaria.modelo):
        return error_response(message="Maquinaria ya registrado", status_code=400)
    
    maquinaria_services.crear_maquinarias(maquinaria.nombre, maquinaria.modelo, maquinaria.descripcion)
    return success_response(message="Maquinaria registrado exitosamente")

@router.get("/obtener-maquinarias")
def obtener_maquinarias():
    maquinarias = maquinaria_services.obtener_maquinarias()
    return success_response(message="Lista de maquinarias", data=maquinarias)