from sqlalchemy import text
from app.config import engine

def guardar_prediccion(maquinaria_id: int, resultado_prediccion: str, confianza):
    confianza = float(confianza)
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO historial_predicciones (maquinaria_id, resultado_prediccion, confianza)
                VALUES (:maquinaria_id, :resultado_prediccion, :confianza)
            """),
            {
                "maquinaria_id": maquinaria_id,
                "resultado_prediccion": resultado_prediccion,
                "confianza": confianza
            }
        )
        conn.commit()
