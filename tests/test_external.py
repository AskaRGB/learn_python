from unittest.mock import patch

from src.external_api import amount_sum

a = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


@patch("requests.get")
def test_amount_summ(mock_get):
    mock_get.return_value.json.return_value = {"result": 678233.551389}
    assert amount_sum(a) == 678233.551389
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/currency_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": "aufgPUOZ9yUFvwoZm1cweV0OW6wy0bqs"},
    )
