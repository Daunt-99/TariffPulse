from dataclasses import dataclass
import os


@dataclass
class IngestionSettings:
    alpha_vantage_api_key: str | None = os.getenv("ALPHA_VANTAGE_API_KEY")
    fred_api_key: str | None = os.getenv("FRED_API_KEY")
    news_api_key: str | None = os.getenv("NEWS_API_KEY")
    gdelt_base_url: str = os.getenv("GDELT_BASE_URL", "https://api.gdeltproject.org/api/v2")


settings = IngestionSettings()

