import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        (
            [
                {"id": 41428829, "state": "DONT_EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
    ],
)
def test_filter_by_state(value, expected):
    assert filter_by_state(value) == expected


@pytest.mark.parametrize(
    "value_sorted_date, expected_sorted_date",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2024.11.11:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2022.09.21:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2023.08.12:35:29.512364"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2024.11.11:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2023.08.12:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2022.09.21:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(value_sorted_date, expected_sorted_date):
    assert sort_by_date(value_sorted_date) == expected_sorted_date
