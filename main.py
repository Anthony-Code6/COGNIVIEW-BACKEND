from app import create_app
from fastapi import FastAPI

app = create_app()

# === RUTA RAÍZ PARA RENDER ===
@app.get("/")
def root():
    return {"status": "ok", "message": "Backend activo y funcionando en Render"}

#from app import create_app

#app = create_app()

# uvicorn main:app --reload

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload



# http://127.0.0.1:8000/paciente/

# http://localhost:8000/paciente/