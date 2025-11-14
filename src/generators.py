def filter_by_currency(transactions: list[dict], currency: str):
    for i in transactions:
        try:
            if i["operationAmount"]["currency"]["code"] == currency:
                yield i
        except (KeyError, TypeError):
            # Пропускаем элементы с некорректной структурой
            continue


def transaction_descriptions(list_of_transaction_dictionaries):
    for descriptions in list_of_transaction_dictionaries:
        yield descriptions.get("description")


def card_number_generator(start_value, stop_value):
    for number in range(start_value, stop_value + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:16]
