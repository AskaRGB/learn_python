import csv

import pandas as pd


def reading_csv(path_to_file: str) -> list[dict]:
    """Функция преобразования данных из csv-файла в список словарей"""
    file_content = []
    with open(path_to_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:

            creating_dict = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            }
            file_content.append(creating_dict)

        return file_content


def reading_xlsx(path_file: str) -> list[dict]:
    """Функция преобразования данных из exel файла в список словарей"""
    data_from_exel = []
    df = pd.read_excel(path_file).fillna("")
    for _, row in df.iterrows():
        creating_dict = {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {"name": row["currency_name"], "code": row["currency_code"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        }
        data_from_exel.append(creating_dict)
    return data_from_exel
