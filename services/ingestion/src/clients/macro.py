from .base import BaseClient, SourceRecord


class FredClient(BaseClient):
    source_name = "fred"

    def fetch(self, series_id: str) -> list[SourceRecord]:
        # TODO: integrate fredapi for macro and trade index pulls.
        return [SourceRecord(source=self.source_name, payload={"series_id": series_id})]

