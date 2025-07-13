from fastapi import FastAPI
from app.routes import predict
from app.routes import predict, users, casos_entrenamiento, training, maquinarias, historial_predicciones
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/api", tags=["Predicción"])
app.include_router(users.router, prefix="/api", tags=["Usuarios"])
app.include_router(casos_entrenamiento.router, prefix="/api", tags=["Datos Entrenamiento"])
app.include_router(training.router, prefix="/api", tags=["Entrenar Modelo"])
app.include_router(maquinarias.router, prefix="/api", tags=["Maquinarias"])
app.include_router(historial_predicciones.router, prefix="/api", tags=["Historial Predicciones"])