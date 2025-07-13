import datetime
from decimal import Decimal
from sqlalchemy import text
from app.config import engine

def obtener_predicciones():
    query = """
    SELECT 
        hp.id AS prediccion_id, 
        hp.fecha_prediccion,
        hp.resultado_prediccion, 
        hp.confianza, 
        m.id AS maquinaria_id,
        m.nombre AS nombre_maquinaria, 
        m.modelo, 
        m.descripcion 
    FROM historial_predicciones hp 
    JOIN maquinarias m ON hp.maquinaria_id = m.id 
    ORDER BY hp.fecha_prediccion DESC;
    """
    
    with engine.connect() as conn:
        result = conn.execute(text(query)).fetchall()

    predicciones = []
    for row in result:
        row_dict = dict(row._mapping)

        #datetime a string
        if isinstance(row_dict["fecha_prediccion"], (datetime.datetime, datetime.date)):
            row_dict["fecha_prediccion"] = row_dict["fecha_prediccion"].isoformat()
        
        #Decimal a float
        if isinstance(row_dict["confianza"], Decimal):
            row_dict["confianza"] = float(row_dict["confianza"])

        predicciones.append(row_dict)

    return predicciones
