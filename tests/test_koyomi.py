import pytest
import requests
import datetime
from unittest.mock import Mock, patch


from src.config import KOYOMI_API_URL
from src.providers.koyomi import (
    fetch_koyomi_json,
    parse_koyomi_json,
    find_events,
)
from src.providers.koyomi_models import (
    KoyomiEvent,
    Koyomi,
)



def test_fetch_koyomi_json_success():
    mock_response = Mock()
    mock_response.json.return_value = {"test": "data"}

    with patch(
        "src.providers.koyomi.requests.get",
        return_value=mock_response,
    ) as mock_get:
        result = fetch_koyomi_json(2026)

    assert result == {"test": "data"}

    mock_get.assert_called_once_with(
        f"{KOYOMI_API_URL}2026",
        timeout=20,
    )
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()


def test_fetch_koyomi_json_decode_error():
    mock_response = Mock()
    mock_response.json.side_effect = requests.exceptions.JSONDecodeError(
        "Invalid JSON",
        "invalid json",
        0,
    )

    with patch(
        "src.providers.koyomi.requests.get",
        return_value=mock_response,
    ):
        with pytest.raises(requests.exceptions.JSONDecodeError):
            fetch_koyomi_json(2026)


def test_fetch_koyomi_json_timeout():
    with patch(
        "src.providers.koyomi.requests.get",
        side_effect=requests.Timeout(),
    ):
        with pytest.raises(requests.Timeout):
            fetch_koyomi_json(2026)


def test_fetch_koyomi_json_request_exception():
    with patch(
        "src.providers.koyomi.requests.get",
        side_effect=requests.RequestException(),
    ):
        with pytest.raises(requests.RequestException):
            fetch_koyomi_json(2026)


def test_fetch_koyomi_json_other_exception():
    with patch(
        "src.providers.koyomi.requests.get",
        side_effect=Exception(),
    ):
        with pytest.raises(Exception):
            fetch_koyomi_json(2026)


def test_parse_koyomi_json_success():
    koyomi_json_data = {
        "year": "2026",
        "sekki": [
            {
                "date": "2026-09-20",
                "name": "彼岸",
            },
            {
                "date": "2026-09-20",
                "name": "秋分",
            },
        ],
    }

    result = parse_koyomi_json(koyomi_json_data)

    assert result == Koyomi(
        year=2026,
        events=(
            KoyomiEvent(
                date=datetime.date(2026, 9, 20),
                name="彼岸",
            ),
            KoyomiEvent(
                date=datetime.date(2026, 9, 20),
                name="秋分",
            ),
        ),
    )


def test_parse_koyomi_json_key_error():
    koyomi_json_data = {
        "year": "2026",
    }

    with pytest.raises(KeyError):
        parse_koyomi_json(koyomi_json_data)


def test_parse_koyomi_json_value_error():
    koyomi_json_data = {
        "year": "2026",
        "sekki": [
            {
                "date": "invalid-date",
                "name": "彼岸",
            },
        ],
    }

    with pytest.raises(ValueError):
        parse_koyomi_json(koyomi_json_data)


def test_parse_koyomi_json_other_exception():
    koyomi_json_data = {
        "year": "2026",
        "sekki": "invalid",
    }

    with pytest.raises(TypeError):
        parse_koyomi_json(koyomi_json_data)


def test_find_events_found():
    koyomi = Koyomi(
        year=2026,
        events=(
            KoyomiEvent(
                date=datetime.date(2026, 9, 20),
                name="彼岸",
            ),
            KoyomiEvent(
                date=datetime.date(2026, 9, 20),
                name="秋分",
            ),
            KoyomiEvent(
                date=datetime.date(2026, 9, 23),
                name="別のイベント",
            ),
        ),
    )

    result = find_events(
        koyomi,
        datetime.date(2026, 9, 20),
    )

    assert result == (
        KoyomiEvent(
            date=datetime.date(2026, 9, 20),
            name="彼岸",
        ),
        KoyomiEvent(
            date=datetime.date(2026, 9, 20),
            name="秋分",
        ),
    )


def test_find_events_not_found():
    koyomi = Koyomi(
        year=2026,
        events=(
            KoyomiEvent(
                date=datetime.date(2026, 9, 20),
                name="彼岸",
            ),
        ),
    )

    result = find_events(
        koyomi,
        datetime.date(2026, 9, 21),
    )

    assert result == ()