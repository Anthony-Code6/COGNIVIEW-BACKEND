from fastapi import APIRouter,Depends,HTTPException
from app.domain.paciente.schemas import PacienteResponse,PacienteResponseUpd
from app.application.services.paciente_services import obtener_pacientes,obtener_paciente_por_id,crear_paciente,eliminar_pacientes,modificar_paciente,listar_paciente_analisis
from app.config.security import validar_token
import logging

paciente_route = APIRouter()
logging = logging.getLogger("uvicorn")


@paciente_route.get('/',summary="Listar Pacientes", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_pacientes": Pacientes[]
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_pacientes": Lista de Pacientes
}
""")
def paciente_sellst(auth=Depends(validar_token)):
    try:

        logging.info('Listar la informacion de los pacientes por usuarios')

        if "error" in auth:
            raise Exception(auth["error"])
        pacientes = obtener_pacientes(auth['uid'])
        return {
            "exito": True,
            "mensajeError": '',
            "_pacientes":pacientes
        }

    except HTTPException as e:
        logging.error(f"Error al listar a los pacientes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al listar a los pacientes: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }


@paciente_route.post('/',summary="Crear Paciente", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_paciente": Pacientes
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_paciente": Lista al Paciente
}
""")
def paciente_inst(datos:PacienteResponse,auth=Depends(validar_token)):
    try:
        logging.info('Iniciando la creacion de un nuevo paciente')

        if "error" in auth:
            raise Exception(auth["error"])
        
        # # VALIDAD QUE EL DNI TENGA 8 CARACTERES
        # if len(datos.dni) <= 7:
        #     return {
        #         "exito": False,
        #         "mensajeError": 'El dni debe tener 8 caracteres.'
            # }
        
        paciente = crear_paciente(uid=auth['uid'],datos=datos)
        return {
            "exito": True,
            "mensajeError": '',
            "_paciente":paciente
        }
    except HTTPException as e:
        logging.error(f"Error al crear a un paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al crear a un paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }

@paciente_route.delete('/{idPaciente}',summary="Eliminar Paciente", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_paciente": Pacientes
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_paciente": Lista al Paciente
}
""")
def paciente_dlt(idPaciente:str,auth=Depends(validar_token)):
    try:
        logging.info('Iniciando la eliminacion de un paciente')
        if "error" in auth:
            raise Exception(auth["error"])
        
        paciente = eliminar_pacientes(uid=auth['uid'],idPaciente=idPaciente)
        return {
            "exito": True,
            "mensajeError": '',
            "_paciente":paciente
        }
    except HTTPException as e:
        logging.error(f"Error al eliminar al paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al eliminar al paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }


@paciente_route.get('/{idPaciente}',summary="Buscar Paciente", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_paciente": Pacientes
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_paciente": Lista al Paciente
}
""")
def paciente_get(idPaciente:str,auth=Depends(validar_token)):
    try:
        logging.info('Iniciando la busquedad de un paciente')
        if "error" in auth:
            raise Exception(auth["error"])
        
        paciente = obtener_paciente_por_id(uid=auth['uid'],idPaciente=idPaciente)
        return {
            "exito": True,
            "mensajeError": '',
            "_paciente":paciente
        }
    except HTTPException as e:
        logging.error(f"Error al buscar al paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al buscar al paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }

@paciente_route.put('/',summary="Actualizar Paciente", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_paciente": Pacientes
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_paciente": Lista al Paciente
}
""")
def paciente_upd(datos:PacienteResponseUpd,auth=Depends(validar_token)):
    try:

        logging.info('Iniciando la actualzacion de un paciente')

        if "error" in auth:
            raise Exception(auth["error"])
        
        # # VALIDAD QUE EL DNI TENGA 8 CARACTERES
        # if len(datos.dni) <= 7:
        #     return {
        #         "exito": False,
        #         "mensajeError": 'El dni debe tener 8 caracteres.'
        #     }
        
        paciente = modificar_paciente(uid=auth['uid'],datos=datos)
        return {
            "exito": True,
            "mensajeError": '',
            "_paciente":paciente
        }
    except HTTPException as e:
        logging.error(f"Error al actualizar al paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": e.detail 
        }
    except Exception as e:
        logging.error(f"Error al actualizar al paciente: {str(e)}")
        return {
            "exito": False,
            "mensajeError": str(e)
        }



@paciente_route.get('/analisis/',summary="Lista la informacion de los analisis por el paciente", description="""
Simple Response:

```json
Types
{
  "exito": bool,
  "mensajeError": string,
  "mensaje": string,
  "_analisisPacientes":PacienteAnalisis[]
}
                 
Description
{
  "exito": Indicador de exito,
  "mensajeError": Mensaje de Error,
  "mensaje": Mensaje,
  "_analisisPacientes": Lista los pacientes con sus analisis
}
""")
def PacienteAnalisis_Sellst(auth=Depends(validar_token)):
    try:
        logging.info('Iniciando el analisis de la imagenes')

        if "error" in auth:
            raise Exception(auth["error"])
        
        response = listar_paciente_analisis(id_usuario=auth['uid'])
        
        return {
            "exito": True,
            "mensajeError": '',
            "_analisisPacientes":response
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