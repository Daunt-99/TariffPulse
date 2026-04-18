import json
from pathlib import Path

from fastapi import APIRouter, status

from app.schemas.alert_subscription import AlertSubscriptionBase, AlertSubscriptionRead

router = APIRouter()


def _alerts_path() -> Path:
    return Path(__file__).resolve().parents[6] / "data" / "mock" / "alerts.json"


@router.get("", response_model=list[AlertSubscriptionRead])
def list_alerts() -> list[AlertSubscriptionRead]:
    payload = json.loads(_alerts_path().read_text(encoding="utf-8"))
    return [AlertSubscriptionRead.model_validate(item) for item in payload]


@router.post("", response_model=AlertSubscriptionRead, status_code=status.HTTP_201_CREATED)
def create_alert(payload: AlertSubscriptionBase) -> AlertSubscriptionRead:
    return AlertSubscriptionRead(id="alert-local-preview", **payload.model_dump())

