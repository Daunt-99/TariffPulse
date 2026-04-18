import re


COUNTRY_PATTERN = re.compile(r"\b(United States|China|European Union|Mexico|Canada)\b", re.I)
GOODS_PATTERN = re.compile(r"\b(steel|aluminum|battery|electronics|machinery|semiconductor)\b", re.I)
RATE_PATTERN = re.compile(r"(\d{1,2}(?:\.\d+)?)%")


def extract_entities(text: str) -> dict[str, list[str] | float | None]:
    """Simple rule-driven extraction prior to LLM refinement."""
    countries = sorted({match.group(0) for match in COUNTRY_PATTERN.finditer(text)})
    goods = sorted({match.group(0).lower() for match in GOODS_PATTERN.finditer(text)})
    rate_match = RATE_PATTERN.search(text)
    return {
        "countries": countries,
        "goods": goods,
        "tariff_rate": float(rate_match.group(1)) if rate_match else None,
    }

