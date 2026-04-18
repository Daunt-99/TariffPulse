import json
from pathlib import Path

from fastapi import APIRouter

from app.schemas.sector_reaction import SectorReactionRead

router = APIRouter()


def _reactions_path() -> Path:
    return Path(__file__).resolve().parents[6] / "data" / "mock" / "reactions.json"


@router.get("", response_model=list[SectorReactionRead])
def list_reactions() -> list[SectorReactionRead]:
    payload = json.loads(_reactions_path().read_text(encoding="utf-8"))
    return [SectorReactionRead.model_validate(item) for item in payload]

