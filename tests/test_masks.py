import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value_card, expected_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("ffasfdasfasdvav", "Номер карты введен не корректно"),
        ("", "Номер карты введен не корректно"),
        ("70007922896061", "Номер карты введен не корректно"),
    ],
)
def test_mask_number_card(value_card, expected_card):
    assert get_mask_card_number(value_card) == expected_card


@pytest.mark.parametrize(
    "value_account, expected_account",
    [
        ("73654108430135874305", "**4305"),
        ("", "Номер счета введен не корректно"),
        ("fsadfasvaravrv", "Номер счета введен не корректно"),
        ("2141151453411234214", "Номер счета введен не корректно"),
    ],
)
def test_mask_account(value_account, expected_account):
    assert get_mask_account(value_account) == expected_account
