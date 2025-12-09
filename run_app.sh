#!/bin/bash

# Ruta a tu aplicación principal FastAPI
APP_MODULE="main:app"


# Nombre del entorno virtual (ajusta si usas otro)
VENV_PATH="virtual/Scripts/activate"

# Activar entorno virtual (si lo estás usando)
if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
fi


# Iniciar el servidor FastAPI con Uvicorn
echo "Iniciando servidor FastAPI..."
uvicorn $APP_MODULE --reload

