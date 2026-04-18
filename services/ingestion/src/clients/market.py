from datetime import date

from .base import BaseClient, SourceRecord


class YFinanceClient(BaseClient):
    source_name = "yfinance"

    def fetch(self, ticker: str, start: date, end: date) -> list[SourceRecord]:
        # TODO: call yfinance download and normalize OHLCV output.
        return [
            SourceRecord(
                source=self.source_name,
                payload={"ticker": ticker, "start": start.isoformat(), "end": end.isoformat()},
            )
        ]


class AlphaVantageClient(BaseClient):
    source_name = "alpha_vantage"

    def fetch(self, symbol: str) -> list[SourceRecord]:
        # TODO: call Alpha Vantage endpoints with API key and rate limiting.
        return [SourceRecord(source=self.source_name, payload={"symbol": symbol})]

