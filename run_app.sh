#!/bin/bash
APP_MODULE="main:app"
echo "Iniciando servidor FastAPI..."
python -m uvicorn $APP_MODULE --host 0.0.0.0 --port 8000
