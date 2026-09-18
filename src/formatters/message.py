def create_message(
    weather_section: str,
    koyomi_section: str | None,
) -> str:
    """天気情報と暦情報からメール本文を作成する"""

    sections = [weather_section]

    if koyomi_section is not None:
        sections.append(koyomi_section)

    return "\n\n".join(sections)
