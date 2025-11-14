import requests

HEADERS = {"apikey": "aufgPUOZ9yUFvwoZm1cweV0OW6wy0bqs"}


def amount_sum(transaction):
    """Функция возвращения суммы транзакции в рублях"""
    code_currency = transaction["operationAmount"]["currency"]["code"]
    summ_money = transaction["operationAmount"]["amount"]
    if code_currency == "RUB":
        return float(summ_money)
    else:
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={code_currency}&amount={summ_money}"
        response = requests.get(url, headers=HEADERS)
        result = response.json()["result"]
        return float(result)
