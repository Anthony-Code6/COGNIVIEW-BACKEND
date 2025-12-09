
from app.domain.analisis.schemas import Analisis
from app.domain.paciente.schemas import Paciente
from pydantic import BaseModel
from typing import List


class Resultados(BaseModel):
    idResultado:str
    imagen:str
    grados:str
    confianza:str
    fecha:str

# class ResultadoAnalisis(BaseModel):
#     id:str
#     idResultado:str
#     idAnalisis:str


class ResultadosResponse(BaseModel):
    imagen:str
    grados:str
    confianza:str


class ResultadoAnalisisResponse(BaseModel):
    idResultado:str
    idAnalisis:str


class AnalisisResultados(BaseModel):
    Analisis: Analisis
    Resultados: List[Resultados]

class PacienteAnalisis(BaseModel):
    Paciente: Paciente
    AnalisisResultados: List[AnalisisResultados]