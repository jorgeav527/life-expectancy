import pandas as pd
import os

from prod_read_json import file_twb_to_read, file_unpd_to_read
from prod_local_to_S3 import client
from prod_dir_creation import DATOS_PRE_PROCESADOS

# Get the countries from the datos_inyectados
naciones_unidas = file_unpd_to_read()
banco_mundial = file_twb_to_read()
problemas = ["mort_22", "mort_24", "mort_60", "pop_49"]


def read_and_transformation():

    response = client.list_objects(Bucket="airflow", Prefix="datos_brutos/")
    # Tomamos unicamente la fecha y el iso3 para usarlo como indice
    df_twb = pd.read_parquet(
        "https://airflow.us-southeast-1.linodeobjects.com/datos_brutos/df_TWB_SP.DYN.LE00.IN.parquet"
    )[["date", "countryiso3code"]]

    df_unpd = pd.read_parquet(
        "https://airflow.us-southeast-1.linodeobjects.com/datos_brutos/df_TWB_SP.DYN.LE00.IN.parquet"
    )[["date", "countryiso3code"]]
    df_unpd.set_index(["countryiso3code", "date"], inplace=True)

    for obj in response["Contents"]:
        fichero = obj["Key"].split("/")[1]
        if fichero.startswith("df_TWB"):
            # obtengo el cógigo de indicador que se encuentra en el nombre del fichero
            codigo_fichero = fichero[7:-8]
            # busco el código en mi lista de códigos
            # y procedo a renombrar la columna de interés

            df = pd.read_parquet(
                f"https://airflow.us-southeast-1.linodeobjects.com/datos_brutos/df_TWB_{codigo_fichero}.parquet"
            )

            df_twb[banco_mundial[codigo_fichero]] = df.value

        elif fichero.startswith("df_UNPD"):
            codigo_fichero = fichero[8:-8]
            codigo_fichero_number = "".join([n for n in fichero[8:-8] if n.isdigit()])

            if codigo_fichero in problemas:
                temp = pd.read_parquet(
                    f"https://airflow.us-southeast-1.linodeobjects.com/datos_brutos/df_UNPD_{codigo_fichero}.parquet"
                )

                # Creo 3 tablas según el sexo sea hombre, mujer o ambos
                # y selecciono las columnas de interés
                temp_male = temp.loc[temp.sex == "Male", ["iso3", "timeLabel", "value"]]
                temp_female = temp.loc[
                    temp.sex == "Female", ["iso3", "timeLabel", "value"]
                ]
                temp_both = temp.loc[
                    temp.sex == "Both sexes", ["iso3", "timeLabel", "value"]
                ]

                # Renombro la columna de interés según el diccionario
                temp_both.rename(
                    columns={
                        "value": f"{naciones_unidas[codigo_fichero_number][1]}_ambos"
                    },
                    inplace=True,
                )
                temp_male.rename(
                    columns={
                        "value": f"{naciones_unidas[codigo_fichero_number][1]}_masc"
                    },
                    inplace=True,
                )
                temp_female.rename(
                    columns={
                        "value": f"{naciones_unidas[codigo_fichero_number][1]}_fem"
                    },
                    inplace=True,
                )

                # Asigno un index multiple
                temp_male.set_index(["iso3", "timeLabel"], inplace=True)
                temp_female.set_index(["iso3", "timeLabel"], inplace=True)
                temp_both.set_index(["iso3", "timeLabel"], inplace=True)

                df_unpd = df_unpd.join(temp_both, on=["countryiso3code", "date"])
                df_unpd = df_unpd.join(temp_male, on=["countryiso3code", "date"])
                df_unpd = df_unpd.join(temp_female, on=["countryiso3code", "date"])

            else:
                temp = pd.read_parquet(
                    f"https://airflow.us-southeast-1.linodeobjects.com/datos_brutos/df_UNPD_{codigo_fichero}.parquet"
                )

                temp.set_index(["iso3", "timeLabel"], inplace=True)

                temp.rename(
                    columns={"value": naciones_unidas[codigo_fichero_number][1]},
                    inplace=True,
                )

                df_unpd = df_unpd.join(
                    temp[[naciones_unidas[codigo_fichero_number][1]]],
                    on=["countryiso3code", "date"],
                )

    # Eliminamos todos los valores nulos que existen en unpd
    df_unpd.dropna(how="all", inplace=True)
    # Preparamos el dataframe para unirlo
    df_twb.set_index(["countryiso3code", "date"], inplace=True)
    # unimos los dataframes en una sola tabla
    tabla = df_twb.join(df_unpd, on=["countryiso3code", "date"])

    tabla.to_parquet("data/datos_pre_procesados/df_unpd_twb.parquet")


def final_transformations():

    tabla = pd.read_parquet("data/datos_pre_procesados/df_unpd_twb.parquet")

    # Se etiqueta los países según su ingreso nacional por año
    tabla["nivel_ingreso"] = pd.cut(
        tabla["INB_percapita"],
        bins=[0, 1025, 3995, 12375, 200000],
        labels=[
            "Ingreso Bajo",
            "Ingreso medio bajo",
            "Ingreso medio alto",
            "Ingreso Alto",
        ],
        include_lowest=True,
    )

    # Se eliminan todos los nulos que existan sobre esperanza de vida
    tabla.dropna(subset=["esperanza_vida_total"], inplace=True)

    tabla.reset_index(inplace=True)

    tabla.to_parquet("data/datos_pre_procesados/df_unpd_twb.parquet")


def upload_datos_pre_procesados_S3_bucket(folder=DATOS_PRE_PROCESADOS):
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
