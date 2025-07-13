from fastapi import APIRouter, HTTPException
from app.schemas.casos_entrenamiento import CasoEntrenamientoInput
from app.services import casos_entrenamiento_services
from app.utils.response import success_response, error_response
from typing import List

router = APIRouter()

@router.post("/registrar_casos_entrenamiento")
def agregar_casos(casos: List[CasoEntrenamientoInput]):
    try:
        lista_dicts = [caso.dict() for caso in casos]
        casos_entrenamiento_services.insertar_casos(lista_dicts)
        return success_response(message="Casos de entrenamiento guardados correctamente")
    except Exception as e:
        return error_response(message="Error al guardar casos", status_code=500, error=str(e))

