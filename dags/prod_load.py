import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

from prod_local_to_S3 import client
from prod_dir_creation import DATOS_PROCESADOS

DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


def renombrar_columnas_paises():
    df2 = pd.read_parquet("data/datos_brutos/df_countries_TWB.parquet")
    df2.reset_index(inplace=True)

    df2.rename(
        columns={
            "id": "Iso3",
        },
        inplace=True,
    )

    df2.to_parquet("data/datos_pre_procesados/temp_df2.parquet")


def crear_columnas_indicadores():

    df1 = pd.read_parquet("data/datos_pre_procesados/df_unpd_twb.parquet")

    df2 = pd.read_parquet("data/datos_pre_procesados/temp_df2.parquet")

    df_copy_df1 = (
        df1[["countryiso3code", "date", "INB_percapita", "nivel_ingreso"]]
        .copy()
        .replace("", np.nan)
    )

    df_copy_df1[["nivel_ingreso_codes"]] = (
        df_copy_df1[["nivel_ingreso"]]
        .apply(lambda col: pd.Categorical(col).codes)
        .replace(-1, np.nan)
    )
    df_copy_df1[["countryiso3code_codes"]] = (
        df_copy_df1[["countryiso3code"]]
        .apply(lambda col: pd.Categorical(col).codes)
        .replace(-1, np.nan)
    )

    df_copy_df1.rename(
        columns={
            "countryiso3code": "Iso3",
        },
        inplace=True,
    )

    df_copy_df1_merge_df2 = pd.merge(df_copy_df1, df2, how="inner", on="Iso3")

    # Creación de tablas temporales
    df_copy_df1_merge_df2.to_parquet("data/datos_pre_procesados/temp_merge.parquet")

    df_copy_df1.to_parquet("data/datos_pre_procesados/temp_copy_df1.parquet")


def crear_ingresos():

    df_copy_df1_merge_df2 = pd.read_parquet(
        "data/datos_pre_procesados/temp_merge.parquet"
    )

    df_ingresos = df_copy_df1_merge_df2[
        ["countryiso3code_codes", "date", "INB_percapita", "nivel_ingreso_codes"]
    ].copy()

    df_ingresos.rename(
        columns={
            "countryiso3code_codes": "pais_id",
            "date": "año",
            "nivel_ingreso_codes": "nivel_id",
        },
        inplace=True,
    )

    # Creación de parquet final
    df_ingresos.to_parquet("data/datos_procesados/ingreso.parquet")


def crear_paises():

    df_copy_df1 = pd.read_parquet("data/datos_pre_procesados/temp_copy_df1.parquet")

    df2 = pd.read_parquet("data/datos_pre_procesados/temp_df2.parquet")

    df_paises = df_copy_df1[["countryiso3code_codes", "Iso3"]].copy()
    df_paises.drop_duplicates(inplace=True, ignore_index=True)
    df_paises.rename(
        columns={
            "countryiso3code_codes": "id",
        },
        inplace=True,
    )

    df_paises_merge_df2 = pd.merge(df_paises, df2, how="left", on="Iso3")
    df_paises_merge_df2.dropna(inplace=True)
    df_paises_merge_df2

    df_paises_agregados = df_paises_merge_df2[
        ["id", "iso2Code", "Iso3", "name", "longitude", "latitude", "region.value"]
    ].copy()

    df_paises_agregados.rename(
        columns={
            "name": "nombre",
            "iso2Code": "Iso2",
            "Longitude": "longitud",
            "Latitude": "latitud",
            "region.value": "región",
        },
        inplace=True,
    )

    df_paises_agregados.to_parquet("data/datos_procesados/pais.parquet")


def crear_niveles():

    df_copy_df1 = pd.read_parquet("data/datos_pre_procesados/temp_copy_df1.parquet")

    df_niveles = df_copy_df1[["nivel_ingreso_codes", "nivel_ingreso"]].copy()
    df_niveles.dropna(inplace=True)
    df_niveles.drop_duplicates(inplace=True, ignore_index=True)
    df_niveles.rename(
        columns={
            "nivel_ingreso_codes": "id",
            "nivel_ingreso": "cuartil",
        },
        inplace=True,
    )

    df_niveles.to_parquet("data/datos_procesados/nivel.parquet")


def crear_indices():

    df1 = pd.read_parquet("data/datos_pre_procesados/df_unpd_twb.parquet")

    df_paises_agregados = pd.read_parquet("data/datos_procesados/pais.parquet")

    df_copy_df2 = (
        df1[df1.columns.difference(["nivel_ingreso", "INB_percapita"])]
        .copy()
        .replace("", np.nan)
    )

    df_copy_df2[["countryiso3code_codes"]] = (
        df_copy_df2[["countryiso3code"]]
        .apply(lambda col: pd.Categorical(col).codes)
        .replace(-1, np.nan)
    )

    df_copy_df2.rename(
        columns={
            "countryiso3code": "Iso3",
            "date": "años",
        },
        inplace=True,
    )

    df_copy_df2_merge_df2 = pd.merge(
        df_copy_df2, df_paises_agregados, how="inner", on="Iso3"
    )

    df_indices = (
        df_copy_df2_merge_df2[
            df_copy_df2_merge_df2.columns.difference(
                [
                    "Iso3",
                    "nombre",
                    "longitude",
                    "latitude",
                    "región",
                    "countryiso3code_codes",
                ]
            )
        ]
        .copy()
        .reset_index()
    )

    df_indices.rename(
        columns={
            "index": "id",
            "id": "pais_id",
        },
        inplace=True,
    )

    df_indices.to_parquet("data/datos_procesados/indice.parquet")


def upload_datos_procesados_S3_bucket(folder=DATOS_PROCESADOS):
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


def cargar_base_de_datos():

    df_ingresos = pd.read_parquet(
        "https://airflow.us-southeast-1.linodeobjects.com/datos_procesados/ingreso.parquet"
    )

    df_paises_agregados = pd.read_parquet(
        "https://airflow.us-southeast-1.linodeobjects.com/datos_procesados/pais.parquet"
    )

    df_niveles = pd.read_parquet(
        "https://airflow.us-southeast-1.linodeobjects.com/datos_procesados/nivel.parquet"
    )

    df_indices = pd.read_parquet(
        "https://airflow.us-southeast-1.linodeobjects.com/datos_procesados/indice.parquet"
    )

    # Remote Linode db
    DATABASE_URL = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Postgres DB state connection:", connection)

    df_ingresos.to_sql(
        "ingreso", con=engine, index=True, if_exists="replace", index_label="id"
    )

    df_niveles.to_sql(
        "nivel", con=engine, index=False, if_exists="replace", index_label="id"
    )

    df_paises_agregados.to_sql(
        "pais", con=engine, index=False, if_exists="replace", index_label="id"
    )

    df_indices.to_sql(
        "indice", con=engine, index=False, if_exists="replace", index_label="id"
    )

    connection.close()
