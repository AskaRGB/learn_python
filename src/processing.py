from typing import Dict, List

# from utils import transaction_data_json


# data = transaction_data_json(r'C:\Users\gabid\Desktop\skypro\pythonProject\data\operations.json')
def filter_by_state(list_of_dictionaries: list[dict], state: str) -> List[Dict]:
    """Функция сортировки по ключу state"""
    return [item for item in list_of_dictionaries if item.get("state", "") == state]


def sort_by_date(list_of_dictionaries: list[dict], sorting_direction: bool = True) -> List[Dict]:
    """Функция сортировки даты"""
    return sorted(list_of_dictionaries, key=lambda item: item.get("date", ""), reverse=sorting_direction)


# print(filter_by_state([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state':
# 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))
# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2024.11.11:35:29.512364'},
#                     {'id': 41428829, 'state': 'EXECUTED', 'date': '2022.09.21:35:29.512364'},
#                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2023.08.12:35:29.512364'}]))
