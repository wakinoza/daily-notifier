from logging import getLogger, basicConfig, INFO
from datetime import date, timedelta

from src.config import Settings
from src.providers import weather_json, koyomi
from src.formatters import weather_formatter, koyomi_formatter, message
from src.mailer import send_mail


basicConfig(
    level=INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

logger = getLogger(__name__)


def main() -> None:
    logger.info("daily-notifierを開始します")

    settings = Settings.from_environment()

    forecast_json = weather_json.fetch_forecast_json()
    weather_info = weather_json.extract_weather_info(forecast_json)

    weather_section = weather_formatter.format_weather_section(weather_info)

    target_date = date.today() + timedelta(days=1)
    koyomi_json_data = koyomi.fetch_koyomi_json(target_date.year)
    koyomi_data = koyomi.parse_koyomi_json(koyomi_json_data)
    events = koyomi.find_events(koyomi_data, target_date)

    koyomi_section = koyomi_formatter.format_koyomi_events(events, target_date)

    mail_message = message.create_message(weather_section, koyomi_section)
    send_mail("daily-notifier", mail_message, settings)

    logger.info("daily-notifierが正常終了しました")


if __name__ == "__main__":
    main()
