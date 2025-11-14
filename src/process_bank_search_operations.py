# import json
import re
from collections import Counter

# with open(r'C:\Users\gabid\Desktop\skypro\pythonProject\data\operations.json', 'r', encoding='utf-8') as file:
#     data_json = json.load(file)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Получение списка словарей по определенному слову"""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    list_try_elements = []
    for i in data:
        if i.get("description", ""):
            description = str(i["description"])
            if pattern.search(description):
                list_try_elements.append(i)

    return list_try_elements


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Получение названия категории и количества операций в данной категории"""
    counter_operation = []
    for i in data:
        if i.get("description", ""):
            description = i["description"]
            if description in categories:
                counter_operation.append(description)

    counted = Counter(counter_operation)
    return dict(counted)


# user = 'открытие'
# print(data_json)
# user_input_description = ["Перевод организации","Перевод с карты на карту"]
# print(process_bank_operations(data_json, user_input_description))
# print(process_bank_search(data_json, user))
#####
