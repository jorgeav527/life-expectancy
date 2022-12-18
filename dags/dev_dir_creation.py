import os


def creacion_directorios():
    os.makedirs("data/datos_pre_procesados", exist_ok=True)
    os.makedirs("data/datos_procesados", exist_ok=True)
    os.makedirs("data/datos_brutos", exist_ok=True)
