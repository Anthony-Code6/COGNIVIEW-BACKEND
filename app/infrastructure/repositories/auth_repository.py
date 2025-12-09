from config.supabase_config import supabase
from app.domain.auth.login import Login

def authentications(datos:Login):
    try:
        result = supabase.auth.sign_in_with_password({
            "email":datos.email,
            "password":datos.password
        })
        return result
    except Exception as e:
        raise Exception(f"No se pudo iniciar sesión: {str(e)}")

def setUp(datos:Login):
    try:
        result = supabase.auth.sign_up({
            "email":datos.email,
            "password":datos.password
        })
        return result
    except Exception as e:
        raise Exception(f"No se pudo registrar el usuario: {str(e)}")