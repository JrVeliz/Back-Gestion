from pydantic import BaseModel
from typing import Optional

class CasoEntrenamientoInput(BaseModel):
    tipo_maquinaria: str
    tiempo_uso_horas: int
    temperatura_motor: float
    vibracion_general: float
    presion_hidraulica: float
    nivel_aceite_motor: float
    nivel_combustible: float
    rpm_motor: int
    velocidad_avance: float
    carga_trabajo: float
    sensor_fugas: bool
    sensor_ruido: str
    codigo_error: str
    modo_operacion: str
    tiempo_operacion_sesion: int
    ultima_mantencion_dias: int
    condiciones_terreno: str
    falla_reportada: str
