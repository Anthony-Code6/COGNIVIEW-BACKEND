from fastapi import APIRouter,Depends,HTTPException
from app.domain.analisis.schemas import AnalisisResultadoResponse,AnalisisResponse
from app.application.services.analisis_services import (analisar_imagenes,crear_analisis,PrecisionGrado,PromedioConfianza)
from app.config.security import validar_token
import logging

analisis_route = APIRouter()
logging = logging.getLogger("uvicorn")


@analisis_route.post('/',summary="Realizar analisis de la imagen", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
}
""")
def Procesar_Analisis_IA(datos:AnalisisResultadoResponse,auth=Depends(validar_token)):
    try:
        logging.info('Iniciando el analisis de la imagenes')

        if "error" in auth:
            raise Exception(auth["error"])
        

        datosAnalisis = AnalisisResponse(idPaciente=datos.idPaciente,descripcion=datos.descripcion)

        analisis = crear_analisis(datosAnalisis)

        idAnalisis = analisis[0]['idAnalisis']

        analisar_imagenes(id_analisis=idAnalisis,imagenes_base64=datos.imagenes)
        
        return {
            "exito": True,
            "mensajeError": ''
         #   "url":url
        }
    except HTTPException as e:
        logging.error(f"Error al analizar las imagenes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al analizar las imagenes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }
    


@analisis_route.get('/precision-grado',summary="Lista las precisiones por tipo.", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "_analisis_grado": Analisis[],
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error
}
""")
def Precision_Grado(auth=Depends(validar_token)):
    try:
        logging.info('Iniciando la lista de cada precision por grado')

        if "error" in auth:
            raise Exception(auth["error"])
        

        uid = auth['uid']

        response = PrecisionGrado(idUsuario=uid)

        
        return {
            "exito": True,
            "mensajeError": '',
            "_analisis_grado":response
        }
    except HTTPException as e:
        logging.error(f"Error al analizar las imagenes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al analizar las imagenes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }
    

@analisis_route.get('/promedio-confianza',summary="Promedio de la confianza.", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "_promedio_confianza": float,
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error
}
""")
def PromedioConfiaza(auth=Depends(validar_token)):
    try:
        logging.info('Iniciando la la operacion del promedio de la confianza del software.')

        if "error" in auth:
            raise Exception(auth["error"])
        

        uid = auth['uid']

        response = PromedioConfianza(idUsuario=uid)

        
        return {
            "exito": True,
            "mensajeError": '',
            "_promedio_confianza":response
        }
    except HTTPException as e:
        logging.error(f"Error al analizar las imagenes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al analizar las imagenes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }
    
