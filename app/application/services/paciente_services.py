from typing import List
from app.domain.resultados.schemas import Resultados,PacienteAnalisis,AnalisisResultados
from app.domain.paciente.schemas import Paciente
from app.domain.analisis.schemas import Analisis
from app.domain.paciente.schemas import PacienteResponse,PacienteResponseUpd
from app.infrastructure.repositories.paciente_repository import (pacientes_int,paciente_upd,paciente_dlt,paciente_sel,paciente_sellst)
from app.infrastructure.repositories.analisis_repository import (AnalisisPacientes_Sel)
from app.infrastructure.repositories.resultados_repository import(ResultadosAnalisis_Sel)

def crear_paciente(uid:str,datos:PacienteResponse):
    return pacientes_int(uid,datos)

def obtener_pacientes(uid:str):
    return paciente_sellst(uid)

def obtener_paciente_por_id(uid: str, idPaciente: str):
    return paciente_sel(uid,idPaciente)

def modificar_paciente(uid:str,datos:PacienteResponseUpd):
    return paciente_upd(uid,datos)

def eliminar_pacientes(uid: str, idPaciente: str):
    return paciente_dlt(uid,idPaciente)

def listar_paciente_analisis(id_usuario: str) -> List[PacienteAnalisis]:
    paciente_raw = paciente_sellst(id_usuario)
    resultado: List[PacienteAnalisis] = []

    for c in paciente_raw:
        paciente = Paciente(**c)
        analisis_raw = AnalisisPacientes_Sel(paciente.idPaciente)
        analisis_resultados: List[AnalisisResultados] = []

        for a in analisis_raw:
            analisis = Analisis(**a)
            resultados_raw = ResultadosAnalisis_Sel(analisis.idAnalisis)
            resultados = [Resultados(**r) for r in resultados_raw]

            analisis_resultados.append(AnalisisResultados(
                Analisis=analisis,
                Resultados=resultados
            ))

        resultado.append(PacienteAnalisis(
            Paciente=paciente,
            AnalisisResultados=analisis_resultados
        ))

    return resultado