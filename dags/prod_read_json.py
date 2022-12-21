import os
import requests

from prod_local_to_S3 import client
from prod_dir_creation import DATOS_INYECTADOS


def file_twb_to_read():
    url = "https://airflow.us-southeast-1.linodeobjects.com/datos_inyectados/banco_mundial.json"
    response = requests.get(url)
    return response.json()


def file_unpd_to_read():
    url = "https://airflow.us-southeast-1.linodeobjects.com/datos_inyectados/naciones_unidas.json"
    response = requests.get(url)
    return response.json()


def upload_datos_injectados_S3_bucket(folder=DATOS_INYECTADOS):
    """
    Subimos todos los archivos en formato parquet
    """
    data_ = folder.split("/", 1)[1]
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)
        client.upload_file(
            Filename=f"{f}",
            Bucket="airflow",
            Key=f"{data_}/{filename}",
            ExtraArgs={"ACL": "public-read"},
        )
