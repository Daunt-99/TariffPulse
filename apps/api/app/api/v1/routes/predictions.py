import json
from pathlib import Path

from fastapi import APIRouter

from app.schemas.prediction import PredictionRead

router = APIRouter()


def _predictions_path() -> Path:
    return Path(__file__).resolve().parents[6] / "data" / "mock" / "predictions.json"


@router.get("", response_model=list[PredictionRead])
def list_predictions() -> list[PredictionRead]:
    payload = json.loads(_predictions_path().read_text(encoding="utf-8"))
    return [PredictionRead.model_validate(item) for item in payload]

