from .base import BaseClient, SourceRecord


class USTRFeedClient(BaseClient):
    source_name = "ustr"

    def fetch(self) -> list[SourceRecord]:
        return [SourceRecord(source=self.source_name, payload={"feed": "press-releases"})]


class WTOFeedClient(BaseClient):
    source_name = "wto"

    def fetch(self) -> list[SourceRecord]:
        return [SourceRecord(source=self.source_name, payload={"feed": "trade-remedies"})]

