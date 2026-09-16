from datetime import date

from providers.koyomi_models import KoyomiEvent


def format_koyomi_events(
    events: tuple[KoyomiEvent, ...] | None,
    target_date: date,
) -> str | None:
    """暦イベントをメール用の文章に整形する"""

    if not events:
        return None

    event_names = "、".join(event.name for event in events)

    weekday = "月火水木金土日"[target_date.weekday()]

    return (
        f"明日、{target_date.year}年{target_date.month}月"
        f"{target_date.day}日（{weekday}）は、"
        f"【{event_names}】です。"
    )