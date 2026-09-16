import requests
import datetime
from logging import getLogger


from src.config import KOYOMI_API_URL
from src.providers.koyomi_models import (
    KoyomiEvent,
    Koyomi,
)


logger = getLogger(__name__)


def fetch_koyomi_json(year):
    """ 暦JSONを取得する"""

    logger.info("暦JSONを取得します")
    url = f"{KOYOMI_API_URL}{year}"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        koyomi_json_data = response.json()
    except requests.exceptions.JSONDecodeError:
        logger.exception("暦JSONの解析に失敗しました")
        raise

    except requests.Timeout:
        logger.exception("暦JSONの取得がタイムアウトしました")
        raise

    except requests.RequestException:
        logger.exception("暦JSONのHTTP通信に失敗しました")
        raise

    except Exception:
        logger.exception("暦JSONの取得処理で予期しないエラーが発生しました")
        raise

    logger.info("暦JSONを取得しました")
    return koyomi_json_data

def parse_koyomi_json(koyomi_json_data)-> Koyomi:
    """ 暦JSONをDataclassに解析する"""

    logger.info("暦JSONを解析します")
    try:
        events = tuple(
            KoyomiEvent(
                date=datetime.date.fromisoformat(event["date"]),
                name=event["name"],
            )
            for event in koyomi_json_data["sekki"]
        )

        koyomi = Koyomi(
            year=int(koyomi_json_data["year"]),
            events=events,
        )

    except KeyError:
        logger.exception("暦JSONの解析中にKeyErrorが発生しました")
        raise

    except ValueError:
        logger.exception("暦JSONの解析中にValueErrorが発生しました")
        raise

    except Exception:
        logger.exception("暦JSONの解析に失敗しました")
        raise

    logger.info("暦JSONを解析しました")
    return koyomi

def find_events(koyomi: Koyomi, target_date: date) -> tuple[KoyomiEvent, ...]:
    """指定日の暦イベントを抽出する"""

    logger.info("指定日の暦イベントを検索します")

    events = tuple(
        event
        for event in koyomi.events
        if event.date == target_date
    )

    logger.info("指定日の暦イベントを検索しました")
    return events