from dataclasses import dataclass
from typing import Any


@dataclass
class SourceRecord:
    source: str
    payload: dict[str, Any]


class BaseClient:
    source_name: str = "unknown"

    def fetch(self, *args: Any, **kwargs: Any) -> list[SourceRecord]:
        raise NotImplementedError

