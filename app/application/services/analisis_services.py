from app.infrastructure.background.analisis_task import Anality_Imagen
from app.domain.analisis.schemas import AnalisisResponse
from app.infrastructure.repositories import analisis_repository as repo

def analisar_imagenes(id_analisis: str, imagenes_base64: list[str]):
    Anality_Imagen(imagenes=imagenes_base64,idAnalisis=id_analisis)

def crear_analisis(datos:AnalisisResponse):
    return repo.Analisis_Inst(datos)

def PrecisionGrado(idUsuario:str):
    return repo.PrecisionPorGrado(idUsuario=idUsuario)

def PromedioConfianza(idUsuario:str):
    return repo.PromedioConfianza(idUsuario=idUsuario)