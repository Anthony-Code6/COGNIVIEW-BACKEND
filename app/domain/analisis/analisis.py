from pydantic import BaseModel
from typing import List

class Analisis(BaseModel):
    idAnalisis:str
    idPaciente:str
    descripcion:str
    fecha:str

class AnalisisResponse(BaseModel):
    idPaciente:str
    descripcion:str
    imagenes:List[str]
