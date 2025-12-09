import numpy as np
import cv2
import tensorflow as tf
import uuid
from PIL import Image
from io import BytesIO
import base64
import os
import threading

from typing import List
from app.infrastructure.repositories.resultados_repository import Resultados_Inst, ResultadosAnalisis_Inst
from app.domain.resultados.resultados import ResultadosResponse,ResultadoAnalisisResponse
from app.infrastructure.storages.supabase_s3 import Upload

# === CONFIGURACIÓN VISUAL ===
FONT_SIZE = 0.8
FONT_THICKNESS = 2
RECT_COLOR = (0, 255, 0)

# === Cargar modelo y clasificadores solo una vez ===
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'modelo_esquizofrenia.tflite'))
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']
etiquetas = ["Leve", "Moderado", "Grave"]
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def Resultados_Analisis(idAnalisis, frame, grado, confianza):
    nombre_imagen = f"{uuid.uuid4()}.jpg"
    url = Upload(frame=frame, nombre_archivo=nombre_imagen)
    confianza_str = f"{confianza:.2f}"
    datos = ResultadosResponse(imagen=url, grados=grado, confianza=confianza_str)
    resultado = Resultados_Inst(datos=datos)
    if resultado:
        id_resultado = resultado[0]['idResultado']
        datosResulAnality = ResultadoAnalisisResponse(idResultado=id_resultado,idAnalisis=idAnalisis)
        ResultadosAnalisis_Inst(datosResulAnality)


def Anality_Imagen(imagenes: List[str], idAnalisis: str):
    for item in imagenes:
        image_data = item.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            face_roi = gray[y:y + h, x:x + w]
            resized = cv2.resize(face_roi, (48, 48)) / 255.0
            input_data = np.expand_dims(resized, axis=(0, -1)).astype(np.float32)

            interpreter.set_tensor(input_index, input_data)
            interpreter.invoke()
            prediction = interpreter.get_tensor(output_index)

            predicted_class = np.argmax(prediction)
            confidence = np.max(prediction) * 100
            texto = etiquetas[predicted_class]

            cv2.rectangle(frame, (x, y), (x + w, y + h), RECT_COLOR, 2)
            cv2.putText(frame, texto, (x, y + h + 25), cv2.FONT_HERSHEY_SIMPLEX,
                        FONT_SIZE, RECT_COLOR, FONT_THICKNESS)

            print(f"Predicción: {texto} con confianza {confidence:.2f}%")
            # Guardar el resultado en segundo plano
            threading.Thread(target=Resultados_Analisis, args=(idAnalisis, frame.copy(), texto, confidence)).start()
