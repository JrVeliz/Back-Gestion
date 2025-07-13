from sqlalchemy import text
from app.config import engine

def obtener_maquinaria(nombre: str, modelo: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM maquinarias WHERE nombre = :nombre AND modelo = :modelo"),
            {"nombre": nombre, "modelo": modelo}
        ).fetchone()
    return result

def obtener_maquinarias():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM maquinarias")
        ).fetchall()
    return [dict(row._mapping) for row in result]

def crear_maquinarias(nombre: str, modelo : str, descripcion : str):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO maquinarias (nombre, modelo, descripcion)
                VALUES (:nombre, :modelo, :descripcion)
            """),
            {
                "nombre": nombre,
                "modelo": modelo,
                "descripcion": descripcion
            }
        )
        conn.commit()
