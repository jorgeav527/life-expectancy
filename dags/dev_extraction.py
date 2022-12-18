import requests
import pandas as pd

# from dev_variable import *
from dev_countries import *
from dev_read_json import *


def consultar_twb(pais: str, indicador: str, pagina: int = 1):

    """Función que contacta a la API y devuelve la respuesta
    que brinda la misma en formato json"""

    # Página de la api y path al recurso solicitado
    api_url = "http://api.worldbank.org/v2/es"
    path = f"/country/{pais}/indicator/{indicador}"
    url = api_url + path

    # Creamos el diccionario con los parametros
    # para el método get
    args = {
        "date": "1990:2020",
        "page": pagina,
        "per_page": 1000,
        "format": "json",
        "prefix": "Getdata",
    }

    return requests.get(url, params=args).json()


def extraccion_incremental_twb(pais="all", indicador=""):
    """Función que a partir de un país y un indicador
    llama a consultar y establece qué tipo de contenido tiene
    según eso devuelve o no un dataframe con todos los datos"""

    consulta = consultar_twb(pais, indicador)
    try:
        # La primera parte de la respuesta nos indica en
        # cuantas páginas de encuentra la información
        paginas = consulta[0]["pages"]

        # La segunda parte nos retorna una lista de
        # diccionarios con la información que queríamos
        datos = consulta[1]

    except:
        print("No hay datos para:", indicador, pais)
        pass
    else:
        if paginas >= 1:
            # Agregamos los valores de las otras páginas a
            # nuestra lista de diccionarios
            for pagina in range(2, paginas + 1):
                datos.extend(consultar_twb(pais, indicador, pagina)[1])

            # Creo el DataFrame con todos los datos
            data = pd.json_normalize(datos)
            return data
        return pd.DataFrame([["error"]], columns=["no_data"])


def extraccion_incremental_unpd(indicator_code: int):
    base_url_UNPD = "https://population.un.org/dataportalapi/api/v1"
    country = get_numbers_for_merge_countries()
    start_year = 1990
    end_year = 2020

    target = (
        base_url_UNPD
        + f"/data/indicators/{indicator_code}/locations/{country}/start/{start_year}/end/{end_year}"
    )

    response = requests.get(target)
    j = response.json()
    df_UNPD = pd.json_normalize(j["data"])

    # Mientras la respuesta contenga información en el campo 'nextPage',
    # el loop continuará descargando datos y agregando a lo anterior
    while j["nextPage"] is not None:
        response = requests.get(j["nextPage"])
        j = response.json()
        df_temp = pd.json_normalize(j["data"])
        df_UNPD = pd.concat([df_UNPD, df_temp], ignore_index=True)

    return df_UNPD


def extraccion_twb():
    banco_mundial = file_twb_to_read()
    for indicador in banco_mundial:
        datos = extraccion_incremental_twb(pais="all", indicador=indicador)
        # Guardo el dataframe resultante
        datos.to_parquet(f"data/datos_brutos/df_TWB_{indicador}.parquet")
        print(f"Datos sobre {banco_mundial[indicador]} guardados")


def extraccion_unpd():
    naciones_unidas = file_unpd_to_read()
    for indicador in naciones_unidas:
        datos = extraccion_incremental_unpd(indicador)
        datos.to_parquet(
            f"data/datos_brutos/df_UNPD_{naciones_unidas[indicador][0]}_{indicador}.parquet",
            index=False,
        )
        print(f"Datos sobre {naciones_unidas[indicador][1]} guardados")
