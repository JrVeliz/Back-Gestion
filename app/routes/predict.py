from fastapi import APIRouter
from app.schemas.maquinaria_input import MaquinariaInput
from app.model.predictor import predecir

router = APIRouter()

@router.post("/predecir_falla")
def prediccion(datos: MaquinariaInput):
    return predecir(datos.dict())
