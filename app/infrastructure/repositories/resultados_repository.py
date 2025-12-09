from config.supabase_config import supabase
from app.domain.resultados.schemas import ResultadoAnalisisResponse,ResultadosResponse

def Resultados_Inst(datos:ResultadosResponse):
    try:
        response = supabase.table('Resultados').insert({
            "imagen":datos.imagen,
            "grados":datos.grados,
            "confianza":datos.confianza
        }).execute()
        return response.data
    except Exception as e:
        print(f"Error al registrar los resultados del paciente: {e}")
        return None
    

def ResultadosAnalisis_Inst(datos:ResultadoAnalisisResponse):
    try:
        response = supabase.table('ResultadoAnalisis').insert({
            "idResultados":datos.idResultado,
            "idAnalisis":datos.idAnalisis,
        }).execute()
        return response.data
    except Exception as e:
        print(f"Error al registrar los resultados y los analisis del paciente: {e}")
        return None
    
def ResultadosAnalisis_Sel(idAnalisis:str):
    try:
        response = supabase.table('ResultadoAnalisis').select('*, Resultados(*)').eq("idAnalisis", idAnalisis).execute()
        
        resultados = []
        for r in response.data:
            if 'Resultados' in r and r['Resultados']:
                resultados.append(r['Resultados'])  # ← Aquí es un solo objeto, no lista

        return resultados
    
    except Exception as e:
        print(f"Error al listar los resultados del analisis: {e}")
        return []