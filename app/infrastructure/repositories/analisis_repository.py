from config.supabase_config import supabase
from app.domain.analisis.schemas import AnalisisResponse

def Analisis_Inst(datos:AnalisisResponse):
    try:
        response = supabase.table('Analisis').insert({
            "idPaciente":datos.idPaciente,
            "descripcion":datos.descripcion,
        }).execute()
        return response.data
    except Exception as e:
        print(f"Error al crear el analisis para el paciente: {e}")
        return None

def AnalisisPacientes_Sel(idPaciente:str):
    try:
        response = supabase.table('Analisis').select('*').eq('idPaciente',idPaciente).order('fecha',desc=True).execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error al listar los analisis del paciente: {e}")
        return []


def PrecisionPorGrado(idUsuario: str):
    try:
        response = (
            supabase.table("Resultados")
            .select("grados, confianza, ResultadoAnalisis!inner(idAnalisis, Analisis!inner(idPaciente, Paciente!inner(idUsuario)))")
            .eq("ResultadoAnalisis.Analisis.Paciente.idUsuario", idUsuario)
            .execute()
        )
        rows = response.data if response.data else []

        if not rows:
            return {}

        grupos = {}
        for r in rows:
            grado = r.get("grados")
            confianza = float(r["confianza"]) if r.get("confianza") else 0
            if grado not in grupos:
                grupos[grado] = []
            grupos[grado].append(confianza)

        # Calcular promedio por grado
        promedios = [
            {"grado": grado, "precision": round(sum(vals) / len(vals), 2)}
            for grado, vals in grupos.items()
        ]

        return promedios

    except Exception as e:
        raise Exception(f"Error al calcular precisión por grado: {e}")

def PromedioConfianza(idUsuario: str):
    try:
        response = (
            supabase.table("Resultados")
            .select("confianza, ResultadoAnalisis!inner(idAnalisis, Analisis!inner(idPaciente, Paciente!inner(idUsuario)))")
            .eq("ResultadoAnalisis.Analisis.Paciente.idUsuario", idUsuario)
            .execute()
        )
        rows = response.data if response.data else []

        if not rows:
            return 0

        confianzas = [float(r["confianza"]) for r in rows if r.get("confianza")]

        promedio = round(sum(confianzas) / len(confianzas), 2) if confianzas else 0

        return promedio

    except Exception as e:
        raise Exception(f"Error al calcular promedio de confianza: {e}")

