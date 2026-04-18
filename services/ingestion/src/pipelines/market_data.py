from datetime import date

from clients.market import AlphaVantageClient, YFinanceClient


def ingest_market_data(tickers: list[str], start: date, end: date) -> list[dict]:
    """Fetch market and sector ETF data for event-study analysis."""
    yf_client = YFinanceClient()
    av_client = AlphaVantageClient()
    records: list[dict] = []
    for ticker in tickers:
        records.extend(item.payload for item in yf_client.fetch(ticker, start, end))
        records.extend(item.payload for item in av_client.fetch(ticker))
    return records

