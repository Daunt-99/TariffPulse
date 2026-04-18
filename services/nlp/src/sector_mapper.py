SECTOR_KEYWORDS = {
    "Industrials": {"machinery", "logistics", "industrial"},
    "Materials": {"steel", "aluminum", "chemicals", "battery"},
    "Information Technology": {"electronics", "semiconductor", "chip"},
    "Energy": {"oil", "gas", "battery"},
}


def map_sectors(goods: list[str], narrative: str) -> list[str]:
    text = " ".join(goods + [narrative.lower()])
    matched = [
        sector for sector, keywords in SECTOR_KEYWORDS.items() if any(keyword in text for keyword in keywords)
    ]
    return matched or ["Industrials"]

