from fastapi import APIRouter
from app.model.trainer import entrenar_modelo
from app.utils.response import success_response, error_response

router = APIRouter()

@router.post("/entrenar")
def reentrenar():
    try:
        entrenar_modelo()
        return success_response("Modelo reentrenado correctamente")
    except Exception as e:
        return error_response("Error al reentrenar el modelo", error=str(e))