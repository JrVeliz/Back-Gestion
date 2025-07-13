from fastapi import APIRouter
from app.schemas.maquinaria_input import MaquinariaInput
from app.model.predictor import predecir
from app.utils.response import success_response, error_response
from app.services import predicciones_services
router = APIRouter()

@router.post("/predecir_falla")
def prediccion(datos: MaquinariaInput):
    try:
        print("hola 1")
        resultado = predecir(datos)
        print("hola 2")
        maquinaria_id = datos.id  # si no tienes, puedes pasar aparte
        if maquinaria_id:
            predicciones_services.guardar_prediccion(maquinaria_id, resultado_prediccion=resultado["falla_predicha"], confianza=resultado["top_3_probabilidades"][0]["probabilidad"])

        return success_response(message="Predicción realizaday guardada correctamente", data=resultado)
    except Exception as e:
        return error_response(message="Error al realizar la predicción", status_code=500, error=str(e))
