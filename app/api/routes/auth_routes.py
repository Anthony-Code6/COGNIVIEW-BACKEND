from fastapi import APIRouter,HTTPException
from app.domain.auth.login import Login
from app.application.services.auth_services import crear_usuario,login_usuario
import logging

auth_route = APIRouter()
logging = logging.getLogger("uvicorn")


@auth_route.post('/',summary="Login", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_token":string
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_token": Cadena de autenticacion
}
""")
def authentication(datos:Login):
    try:
        logging.info('Iniciando el inicio de sesion')
        result = login_usuario(datos=datos)
        if result.session is None:
            return {
                "exito": False,
                "mensajeError": 'Error en la autenticacion'
            }
        return {
            "exito": True,
            "mensajeError": '',
            "_token":result.session.access_token
        }
    
    except Exception as e:
        logging.error(f"Error al iniciar la sesion: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }


@auth_route.post('/set-up',summary="Register", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_token":string
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_token": Cadena de autenticacion
}
""")
def SetUp(datos:Login):
    try:
        result = crear_usuario(datos=datos)
        return {
            "exito": True,
            "mensajeError": '',
        }

    except Exception as e:
        return {
            "exito": False,
            "mensajeError": str(e)
        }

