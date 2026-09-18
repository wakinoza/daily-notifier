from datetime import date

from src.formatters.koyomi_formatter import format_koyomi_events
from src.providers.koyomi_models import KoyomiEvent


def test_format_koyomi_events_with_events():
    target_date = date(2026, 9, 20)
    events = (
        KoyomiEvent(date(2026, 9, 20), "彼岸"),
        KoyomiEvent(date(2026, 9, 20), "秋分"),
    )

    result = format_koyomi_events(events, target_date)

    assert result == "明日、2026年9月20日（日）は、【彼岸、秋分】です。"


def test_format_koyomi_events_without_events():
    target_date = date(2026, 9, 21)
    events = ()

    result = format_koyomi_events(events, target_date)

    assert result is None


def test_format_koyomi_events_with_none():
    target_date = date(2026, 9, 21)

    result = format_koyomi_events(None, target_date)

    assert result is None
