from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class KoyomiEvent:
    """暦イベントを表すモデル"""

    date: date
    name: str


@dataclass(frozen=True)
class Koyomi:
    """1年分の暦情報を表すモデル"""

    year: int
    events: tuple[KoyomiEvent, ...]
