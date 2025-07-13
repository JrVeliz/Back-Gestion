from fastapi import APIRouter
from app.schemas.maquinaria_input import RegistroMaquinaria
from app.services import historial_predicciones_services
from app.utils.response import success_response, error_response

router = APIRouter()

@router.get("/obtener-predicciones")
def obtener_predicciones():
    maquinarias = historial_predicciones_services.obtener_predicciones()
    return success_response(message="Lista de predicciones", data=maquinarias)