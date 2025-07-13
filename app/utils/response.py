from fastapi.responses import JSONResponse

def success_response(message: str = "Operación exitosa", data: dict = None):
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": message,
            "data": data or {}
        }
    )

def error_response(message: str = "Error en la operación", status_code: int = 400, error: str = ""):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": message,
            "error": error
        }
    )
