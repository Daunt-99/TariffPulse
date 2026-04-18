from .base import BaseClient, SourceRecord


class NewsApiClient(BaseClient):
    source_name = "newsapi"

    def fetch(self, query: str) -> list[SourceRecord]:
        return [SourceRecord(source=self.source_name, payload={"query": query})]


class GDELTClient(BaseClient):
    source_name = "gdelt"

    def fetch(self, query: str) -> list[SourceRecord]:
        return [SourceRecord(source=self.source_name, payload={"query": query})]

