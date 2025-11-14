import re
from collections import Counter


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


