import os

DATA = "data"
DATOS_INYECTADOS = f"{DATA}/datos_inyectados"
DATOS_BRUTOS = f"{DATA}/datos_brutos"
DATOS_PRE_PROCESADOS = f"{DATA}/datos_pre_procesados"
DATOS_PROCESADOS = f"{DATA}/datos_procesados"


def creacion_directorios():
    os.makedirs(DATOS_BRUTOS, exist_ok=True)
    os.makedirs(DATOS_PRE_PROCESADOS, exist_ok=True)
    os.makedirs(DATOS_PROCESADOS, exist_ok=True)
