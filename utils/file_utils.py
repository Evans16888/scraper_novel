# utils/file_utils.py
import os

def crear_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def limpiar_directorio(ruta):
    if os.path.exists(ruta):
        for archivo in os.listdir(ruta):
            archivo_ruta = os.path.join(ruta, archivo)
            if os.path.isfile(archivo_ruta):
                os.remove(archivo_ruta)

def obtener_ruta_pdf(nombre_archivo):
    crear_directorio("pdfs")
    return os.path.join("pdfs", nombre_archivo)