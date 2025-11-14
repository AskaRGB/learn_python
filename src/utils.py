import json
import logging
import os
from typing import Dict, List

logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_data_json(path_to_file: str) -> List[Dict]:
    """Функция возвращения данных о финансовых транзакциях из json файла"""
    try:
        logger.info("проверяем наличие файла")
        if os.path.isfile(path_to_file):
            with open(path_to_file, "r", encoding="utf-8") as f:
                try:
                    logger.info("файл найден, сохраняем данные по транзакциям")
                    list_dict_transaction = json.load(f)
                    if list_dict_transaction:
                        logger.info("Данные не пустые, возвращаем переменную list_dict_transaction")
                        return list_dict_transaction
                    else:
                        logger.info("Данные пустые, возвращаем пустой список")
                        return []
                except json.JSONDecodeError as ex:
                    logger.error(f"произошла ошибка {ex}")
                    return []
        logger.info("Файл не найден, возвращаем пустой список")
        return []
    except Exception as ex:
        logger.error(f"произошла ошибка {ex}")
        return []
