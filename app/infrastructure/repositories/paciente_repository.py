from config.supabase_config import supabase
from app.domain.paciente.paciente import PacienteResponse,PacienteResponseUpd

def pacientes_int(uid:str,datos:PacienteResponse):
    try:
        response = supabase.table('Paciente').insert({
            "idUsuario":uid,
            "nombre":datos.nombre,
            "apellido":datos.apellido,
            "dni":datos.dni
        }).execute()

        return response.data
    except Exception as e:
        print(f"Error al crear a un paciente: {e}")
        return None

def paciente_sellst(uid:str):
    try:
        response = supabase.table('Paciente').select('*').eq('idUsuario',uid).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error al listar los paciente: {e}")
        return []

def paciente_dlt(uid:str,idPaciente:str):
    try:
        response = supabase.table('Paciente').delete().eq('idUsuario',uid).eq('idPaciente',idPaciente).execute()
        return response.data
    except Exception as e:
        print(f"Error al eliminar a un paciente: {e}")
        return None
    
def paciente_sel(uid:str,idPaciente:str):
    try:
        response = supabase.table('Paciente').select("*").eq('idUsuario',uid).eq('idPaciente',idPaciente).execute()
        return response.data
    except Exception as e:
        print(f"Error al buscar a un paciente: {e}")
        return None

def paciente_upd(uid:str,datos:PacienteResponseUpd):
    try:
        response = supabase.table('Paciente').update({
            "nombre":datos.nombre,
            "apellido":datos.apellido,
            "dni":datos.dni
        }).eq('idPaciente',datos.idPaciente).eq('idUsuario',uid).execute()

        return response.data
    except Exception as e:
        print(f"Error al actualizar a un paciente: {e}")
        return None