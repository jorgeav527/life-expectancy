import requests

import pandas as pd


def country_twb():
    incomes = ["HIC", "INX", "LIC", "LMC", "LMY", "MIC", "UMC"]
    trabajo = pd.DataFrame()

    for income in incomes:
        url = "http://api.worldbank.org/v2/es/country"  # Aqui vemos la lista de niveles de Ingreso y sus respectivos códigos
        args = {"format": "json", "prefix": "Getdata", "incomelevel": income}
        dic_Income_Level = requests.get(url, params=args)
        datos = dic_Income_Level.json()[1]
        data = pd.json_normalize(datos)
        trabajo = pd.concat([trabajo, data], ignore_index=True)

    trabajo.replace("", float("NaN"), inplace=True)
    trabajo.dropna(subset=["longitude", "latitude"], inplace=True)

    # Sección para conseguir el nombre de todos los países
    # con su respectiva ubicación
    temp = trabajo[
        ["id", "iso2Code", "name", "longitude", "latitude", "region.id", "region.value"]
    ]

    Agregar = pd.DataFrame(
        [
            [
                "USA",
                "US",
                "Estados Unidos",
                "-95.712891",
                "37.0902",
                "NAC",
                "América del Norte",
            ]
        ],
        columns=[
            "id",
            "iso2Code",
            "name",
            "longitude",
            "latitude",
            "region.id",
            "region.value",
        ],
    )

    temp = pd.concat([temp, Agregar], ignore_index=True)
    temp = temp.groupby("id").agg(pd.Series.mode)
    temp.reset_index(inplace=True)
    temp.to_parquet("data/datos_brutos/df_countries_TWB.parquet")


def country_unpd():

    # Base url
    base_url = "https://population.un.org/dataportalapi/api/v1"

    # Creates the target URL, indicators, in this instance.
    target = base_url + "/locations/"

    # Get the response, which includes the first page of data as well as information on pagination and number of records.
    response = requests.get(target)

    # Converts call into JSON.
    j = response.json()

    # Converts JSON into a pandas DataFrame.
    df_locations = pd.json_normalize(
        j["data"]
    )  # pd.json_normalize flattens the JSON to accomodate nested lists within the JSON structure.

    # Loop until there are new pages with data.
    while j["nextPage"] != None:
        # Reset the target to the next page.
        target = j["nextPage"]

        # call the API for the next page.
        response = requests.get(target)

        # Convert response to JSON format.
        j = response.json()

        # Store the next page in a data frame.
        df_temp = pd.json_normalize(j["data"])

        # Append next page to the data frame.
        df_locations = pd.concat([df_locations, df_temp], ignore_index=True)
        df_locations.to_parquet("data/datos_brutos/df_countries_UNPD.parquet")


def get_numbers_for_merge_countries():

    # Let's load the dataframe for the two APIs.
    c_twb = pd.read_parquet("data/datos_brutos/df_countries_TWB.parquet")
    c_twb.rename(
        columns={
            "id": "iso3",
        },
        inplace=True,
    )
    c_unpd = pd.read_parquet("data/datos_brutos/df_countries_UNPD.parquet")

    # merge the two dataframes
    numbers_of_countries = c_twb.merge(c_unpd, how="left", on="iso3")

    # Stores indicator codes in a list
    numbers_of_countries_list = [str(i) for i in numbers_of_countries["id"].values]

    # Converts indicator code list into string to be used in later API call
    numbers_of_countries_string = ",".join(numbers_of_countries_list)
    return numbers_of_countries_string
