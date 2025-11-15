from pathlib import Path
from generators import filter_by_currency
from process_bank_search_operations import process_bank_operations, process_bank_search
from processing import filter_by_state, sort_by_date
from reading_transaction_from_csv_xlsx import reading_csv, reading_xlsx
from utils import transaction_data_json
from widget import get_date, mask_account_card


def get_data_directory() -> Path:
    """Определяет путь к папке с данными относительно текущего файла"""
    current_file_path = Path(__file__).parent
    project_root = current_file_path.parent
    data_dir = project_root / "data"

    if not data_dir.exists():
        data_dir.mkdir(exist_ok=True)
        print(f"Создана папка для данных: {data_dir}")
        print("Пожалуйста, поместите ваши файлы данных в эту папку:")
        print("operations.json, transactions.csv, transactions_excel.xlsx")

    return data_dir


def get_file_paths(data_dir: Path) -> dict:
    """Возвращает пути к файлам данных"""
    return {1: data_dir / "operations.json", 2: data_dir / "transactions.csv", 3: data_dir / "transactions_excel.xlsx"}


def check_files_exist(file_paths: dict) -> bool:
    """Проверяет существование файлов данных"""
    missing_files = []
    for file_type, path in file_paths.items():
        if not path.exists():
            missing_files.append(path.name)

    if missing_files:
        print("ВНИМАНИЕ! Отсутствуют следующие файлы данных:")
        for file in missing_files:
            print(f"  - {file}")
        print(f"\nФайлы должны находиться в папке: {file_paths[1].parent}")
        return False
    return True


READERS = {1: transaction_data_json, 2: reading_csv, 3: reading_xlsx}


def get_user_input(prompt: str, valid_options: list) -> str:
    """Функция для ввода с валидацией"""
    while True:
        user_input = input(prompt)
        if not valid_options or user_input.lower() in valid_options:
            return user_input
        else:
            print("Проверьте ввод")


def load_data() -> list[dict]:
    """Функция загрузки данных из выбранного файла"""
    data_dir = get_data_directory()
    file_paths = get_file_paths(data_dir)

    if not check_files_exist(file_paths):
        print("Пожалуйста, добавьте файлы данных и перезапустите программу.")
        exit()

    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    choice = int(get_user_input("Введите цифру: ", ["1", "2", "3"]))
    file_types = {1: "JSON", 2: "CSV", 3: "XLSX"}
    print(f"Для обработки выбран {file_types[choice]}-файл")

    return READERS[choice](file_paths[choice])


def filter_data(data_from_file: list[dict]) -> list[dict]:
    """Функция фильтрации и сортировки данных"""
    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    status = get_user_input(
        "Введите статус (EXECUTED, CANCELED, PENDING): ", ["executed", "canceled", "pending"]
    ).upper()
    print(f"Операции отфильтрованы по статусу {status}")
    filtered_data = filter_by_state(data_from_file, status)

    # Сортировка по дате (опционально)
    if get_user_input("Отсортировать операции по дате? Да/Нет: ", ["да", "нет"]) == "да":
        if get_user_input("По возрастанию или по убыванию?: ", ["по возрастанию", "по убыванию"]) == 'по возрастанию':
            filtered_data = sort_by_date(filtered_data, True)
        else:
            filtered_data = sort_by_date(filtered_data, False)

    # Фильтрация по валюте (опционально)
    if get_user_input("Выводить только рублевые транзакции? Да/Нет: ", ["да", "нет"]) == "да":
        filtered_data = list(filter_by_currency(filtered_data, "RUB"))

    return filtered_data


def search_by_description(sorted_data: list[dict]) -> dict:
    """Поиск операций по описанию"""
    if (
        get_user_input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ", ["да", "нет"])
        == "да"
    ):
        search_word = input("Введите слово: ")
        result_data_filter = process_bank_search(sorted_data, search_word)

        if result_data_filter:  # Проверка на пустой результат
            description = [item["description"] for item in result_data_filter if item.get("description")]
            result_data_count = process_bank_operations(result_data_filter, description)
        else:
            result_data_count = {}

        return {"result_data": result_data_filter, "result_data_count": result_data_count}
    else:
        # Если пропустили поиск по описанию, возвращаем исходные данные
        description = [item["description"] for item in sorted_data if item.get("description")]
        result_data_count = process_bank_operations(sorted_data, description)
        return {"result_data": sorted_data, "result_data_count": result_data_count}


def display_results(result: dict) -> None:
    """Отображение результатов транзакций"""
    if not result:
        print("Нет данных для отображения.")
        return

    result_data = result["result_data"]
    result_data_counted = result["result_data_count"]

    # Безопасный подсчет количества операций
    if result_data_counted:
        digit = sum(result_data_counted.values())
    else:
        digit = len(result_data) if result_data else 0

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {digit}")

    if not result_data:
        print("Нет транзакций для отображения.")
        return

    for i in result_data:
        if i.get("from") and i.get("from") != "":
            print(
                f"""{get_date(i['date'])}, {i['description']}
{mask_account_card(i['from'])} -> {mask_account_card(i['to'])}
Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}
"""
            )
        else:
            print(
                f"""{get_date(i['date'])}, {i['description']}
{mask_account_card(i['to'])}
"""
            )


if __name__ == "__main__":
    try:
        data = load_data()
        processed_data = filter_data(data)
        result = search_by_description(processed_data)
        display_results(result)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Пожалуйста, проверьте наличие файлов данных и их формат.")
