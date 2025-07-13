from sqlalchemy import text
from app.config import engine

def obtener_usuario_por_email(email: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM usuarios WHERE email = :email"),
            {"email": email}
        ).fetchone()
        return result

def crear_usuario(nombre: str, email: str, password: str):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO usuarios (nombre, email, password)
                VALUES (:nombre, :email, :password)
            """),
            {
                "nombre": nombre,
                "email": email,
                "password": password
            }
        )
        conn.commit()
