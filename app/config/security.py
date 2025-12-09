from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, Request, status
from config.supabase_config import supabase

security = HTTPBearer()

async def validar_token(request: Request):

    # 1. Leer header correctamente
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no proporcionado"
        )

    # 2. Formato correcto: "Bearer <token>"
    if not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token inválido"
        )

    token = auth_header.split(" ")[1]

    if not token or token in ["null", "undefined", "None", ""]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token vacío o inválido"
        )

    # 3. Validar con Supabase
    try:
        user_response = supabase.auth.get_user(token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error al validar token"
        )

    if user_response.user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

    # 4. Retornar usuario válido
    return {
        "uid": user_response.user.id,
        "email": user_response.user.email
    }
    