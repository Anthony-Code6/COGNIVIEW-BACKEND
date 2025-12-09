from config.supabase_config import supabase,BUCKET,SUPABASE_URL
import cv2
import os
import tempfile

def Files():
    try:
        archivos_bucket = supabase.storage.from_(BUCKET).list()
        return archivos_bucket
    except Exception as e:
        return []


def Delete(url):
    try:
        supabase.storage.from_(BUCKET).remove([url])
    except Exception as e:
        print(f"Error al eliminar imagen de Supabase: {e}")
        raise


def Upload(frame, nombre_archivo):
    # Usar carpeta temporal segura del sistema
    ruta_local = os.path.join(tempfile.gettempdir(), nombre_archivo)

    # Validar si se guardó correctamente
    success = cv2.imwrite(ruta_local, frame)
    if not success:
        raise Exception(f"No se pudo guardar la imagen en {ruta_local} con cv2.imwrite")

    # Verifica que el archivo fue creado realmente
    if not os.path.exists(ruta_local):
        raise FileNotFoundError(f"El archivo no existe: {ruta_local}")

    with open(ruta_local, "rb") as f:
        supabase.storage.from_(BUCKET).upload(
            f"{nombre_archivo}", f, {"content-type": "image/jpeg"}
        )

    # Limpieza opcional
    os.remove(ruta_local)

    return f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{nombre_archivo}"
