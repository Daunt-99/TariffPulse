from datetime import date, timedelta

from pipelines.macro_data import ingest_macro_series
from pipelines.market_data import ingest_market_data
from pipelines.news_data import ingest_news
from pipelines.policy_releases import ingest_policy_releases


def run_scheduled_ingestion() -> dict[str, list[dict]]:
    """Entry point for cron, Airflow, or standalone worker execution."""
    today = date.today()
    return {
        "market": ingest_market_data(["SPY", "XLI", "XLB", "XLK"], today - timedelta(days=30), today),
        "macro": ingest_macro_series(["DGS10", "DTWEXBGS"]),
        "news": ingest_news("tariff OR trade duty OR customs policy"),
        "policy": ingest_policy_releases(),
    }


if __name__ == "__main__":
    print(run_scheduled_ingestion())

