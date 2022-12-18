import pandas as pd
import os

from dev_read_json import *

naciones_unidas = file_unpd_to_read()

banco_mundial = file_twb_to_read()

problemas = ["mort_22", "mort_24", "mort_60", "pop_49"]


def read_and_transformation():

    directorio = "data/datos_brutos/"
    with os.scandir(directorio) as ficheros:
        # Tomamos unicamente la fecha y el iso3 para usarlo como indice
        df_twb = pd.read_parquet("data/datos_brutos/df_TWB_SP.DYN.LE00.IN.parquet")[
            ["date", "countryiso3code"]
        ]

        df_unpd = pd.read_parquet("data/datos_brutos/df_TWB_SP.DYN.LE00.IN.parquet")[
            ["date", "countryiso3code"]
        ]
        df_unpd.set_index(["countryiso3code", "date"], inplace=True)

        for fichero in ficheros:
            if fichero.name.startswith("df_TWB"):
                # obtengo el cógigo de indicador que se encuentra en el nombre del fichero
                codigo_fichero = fichero.name[7:-8]
                # busco el código en mi lista de códigos
                # y procedo a renombrar la columna de interés

                df = pd.read_parquet(directorio + fichero.name)

                df_twb[banco_mundial[codigo_fichero]] = df.value

            elif fichero.name.startswith("df_UNPD"):
                codigo_fichero = fichero.name[8:-8]
                codigo_fichero_number = "".join(
                    [n for n in fichero.name[8:-8] if n.isdigit()]
                )

                if codigo_fichero in problemas:
                    temp = pd.read_parquet(directorio + fichero.name)

                    # Creo 3 tablas según el sexo sea hombre, mujer o ambos
                    # y selecciono las columnas de interés
                    temp_male = temp.loc[
                        temp.sex == "Male", ["iso3", "timeLabel", "value"]
                    ]
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
                    temp = pd.read_parquet(directorio + fichero.name)

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
