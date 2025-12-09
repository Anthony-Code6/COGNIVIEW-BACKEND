from pydantic import BaseModel

class Resultados(BaseModel):
    idResultado:str
    imagen:str
    grados:str
    confianza:str
    fecha:str

class ResultadosResponse(BaseModel):
    imagen:str
    grados:str
    confianza:str

class ResultadoAnalisis(BaseModel):
    id:str
    idResultado:str
    idAnalisis:str

class ResultadoAnalisisResponse(BaseModel):
    idResultado:str
    idAnalisis:str

