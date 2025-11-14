import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        ("", []),
    ],
)
def test_filter_by_currency(value_test_filter_by_currency, value, expected):
    test_value = filter_by_currency(value_test_filter_by_currency, value)
    assert list(test_value) == expected


@pytest.mark.parametrize(
    "expected_transaction",
    [
        "Перевод организации",
    ],
)
def test_transaction_descriptions(value_test_filter_by_currency, expected_transaction):
    test_value_transaction = transaction_descriptions(value_test_filter_by_currency)
    assert next(test_value_transaction) == expected_transaction


@pytest.mark.parametrize("value_start_card, value_stop_card, expected_card", [(1, 1, ["0000 0000 0000 0001"])])
def test_card_number_generator(value_start_card, value_stop_card, expected_card):
    test_value_card = card_number_generator(value_start_card, value_stop_card)
    assert list(test_value_card) == expected_card
