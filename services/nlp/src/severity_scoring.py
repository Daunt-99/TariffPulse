def score_severity(tariff_rate: float | None, official_source: bool, sectors: list[str]) -> float:
    base = 0.35
    if tariff_rate:
        base += min(tariff_rate / 50, 0.4)
    if official_source:
        base += 0.15
    base += min(len(sectors) * 0.04, 0.1)
    return round(min(base, 0.99), 2)

