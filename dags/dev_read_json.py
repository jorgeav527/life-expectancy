import json


def file_twb_to_read():
    with open("data/data_inyectada/banco_mundial.json", "r") as file_twb:
        data = json.load(file_twb)
    return data


def file_unpd_to_read():
    with open("data/data_inyectada/naciones_unidas.json", "r") as file_unpd:
        data = json.load(file_unpd)
    return data
