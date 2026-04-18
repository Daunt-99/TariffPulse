import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.schemas.tariff_event import TariffEventRead

router = APIRouter()


def _events_path() -> Path:
    return Path(__file__).resolve().parents[6] / "data" / "mock" / "events.json"


@router.get("", response_model=list[TariffEventRead])
def list_events() -> list[TariffEventRead]:
    payload = json.loads(_events_path().read_text(encoding="utf-8"))
    return [TariffEventRead.model_validate(item) for item in payload]


@router.get("/{event_id}", response_model=TariffEventRead)
def get_event(event_id: str) -> TariffEventRead:
    events = list_events()
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

