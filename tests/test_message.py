from src.formatters.message import create_message


def test_create_message_with_koyomi():
    weather_section = "明日の天気は晴れです。"
    koyomi_section = "明日は【白露】です。"

    result = create_message(weather_section, koyomi_section)

    assert result == ("明日の天気は晴れです。\n\n明日は【白露】です。")


def test_create_message_without_koyomi():
    weather_section = "明日の天気は晴れです。"

    result = create_message(weather_section, None)

    assert result == "明日の天気は晴れです。"
