import logging

logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты"""
    try:
        logger.info(f"Выполняем проверку номера карты {card_number}")
        card_number_without_spaces = card_number.replace(" ", "")
        if len(card_number_without_spaces) != 16:
            logger.info(f"Номер карты введен не корректно {card_number}")
            return "Номер карты введен не корректно"

        card_number_mask = (
            f"{card_number_without_spaces[:4]} {card_number_without_spaces[4:6]}** "
            f"**** {card_number_without_spaces[-4:]}"
        )
        logger.info(f"Номер карты введен корректно и зашифрован {card_number_mask}")
        return card_number_mask
    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        return ""


# print(get_mask_card_number('7365410843013587'))


# print(get_mask_card_number('ffasfdasfasdvav'))
def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета"""
    try:
        logger.info(f"Проверяем номер счета {account_number}")
        if len(account_number) != 20:
            logger.info("номер счета введен не корректно")
            return "Номер счета введен не корректно"
        else:
            logger.info("номер счета введен корректно")
            mask_account_number = f"**{account_number[-4:]}"
            logger.info(f"номер счета зашифрован {mask_account_number}")
            return mask_account_number
    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        return ""


# print(get_mask_account("73654108430135874305"))
