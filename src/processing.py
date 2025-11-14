from typing import Dict, List

# from utils import transaction_data_json


# data = transaction_data_json(r'C:\Users\gabid\Desktop\skypro\pythonProject\data\operations.json')
def filter_by_state(list_of_dictionaries: list[dict], state: str) -> List[Dict]:
    """Функция сортировки по ключу state"""
    return [item for item in list_of_dictionaries if item.get("state", "") == state]


def sort_by_date(list_of_dictionaries: list[dict], sorting_direction: bool = True) -> List[Dict]:
    """Функция сортировки даты"""
    return sorted(list_of_dictionaries, key=lambda item: item.get("date", ""), reverse=sorting_direction)


