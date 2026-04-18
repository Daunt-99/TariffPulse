import json
from pathlib import Path
from typing import Any

from app.core.config import settings


def load_mock_payload(filename: str) -> list[dict[str, Any]]:
    base_path = Path.cwd().parent.parent
    mock_path = base_path / settings.mock_data_path
    if filename != "events.json":
        mock_path = mock_path.with_name(filename)
    return json.loads(mock_path.read_text(encoding="utf-8"))

