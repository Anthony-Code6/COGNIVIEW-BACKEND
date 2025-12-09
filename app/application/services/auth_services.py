from app.domain.auth.login import Login
from app.infrastructure.repositories.auth_repository import (setUp,authentications)

def login_usuario(datos:Login):
    return authentications(datos)

def crear_usuario(datos:Login):
    return setUp(datos)