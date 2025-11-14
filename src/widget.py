from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_or_account: str) -> str | None:
    """ "Функция маскировки номера карты или банковского счета"""
    digit = ""
    letters = ""

    for symbols in type_card_or_account:
        if symbols.isdigit():
            digit += symbols
        else:
            letters += symbols
    if len(digit) != 16 and len(digit) != 20:
        return "Неверно заполнены данные"

    elif len(digit) == 16:
        mask_card = get_mask_card_number(digit)
        return f"{letters} {mask_card}"

    elif len(digit) == 20:
        mask_account = get_mask_account(digit)
        return f"{letters} {mask_account}"


def get_date(date_string: str) -> str:
    """Функция преобразования даты"""
    try:
        date_object = datetime.fromisoformat(date_string)
        formate_date = date_object.strftime("%d.%m.%Y")
    except ValueError:
        return "Данные введены не корректно"
    return formate_date


# print(mask_account_card('Счет 96231448929365202391'))
# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(get_date('2024-03-11T02:26:18.671407'))
