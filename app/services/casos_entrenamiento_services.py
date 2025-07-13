from sqlalchemy import text
from app.config import engine
from typing import List

def insertar_casos(casos: List[dict]):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO casos_entrenamiento (
                    tipo_maquinaria, tiempo_uso_horas, temperatura_motor, vibracion_general,
                    presion_hidraulica, nivel_aceite_motor, nivel_combustible, rpm_motor,
                    velocidad_avance, carga_trabajo, sensor_fugas, sensor_ruido, codigo_error,
                    modo_operacion, tiempo_operacion_sesion, ultima_mantencion_dias,
                    condiciones_terreno, falla_reportada
                ) VALUES (
                    :tipo_maquinaria, :tiempo_uso_horas, :temperatura_motor, :vibracion_general,
                    :presion_hidraulica, :nivel_aceite_motor, :nivel_combustible, :rpm_motor,
                    :velocidad_avance, :carga_trabajo, :sensor_fugas, :sensor_ruido, :codigo_error,
                    :modo_operacion, :tiempo_operacion_sesion, :ultima_mantencion_dias,
                    :condiciones_terreno, :falla_reportada
                )
            """),
            casos
        )
        conn.commit()