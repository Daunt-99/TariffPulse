from pydantic import BaseModel, ConfigDict

from app.schemas.common import LagLabelEnum, SectorEnum


class PredictionRead(BaseModel):
    id: str
    event_id: str
    sector: SectorEnum
    predicted_reaction_speed: LagLabelEnum
    predicted_magnitude: float
    confidence: float
    similar_past_events: list[str]
    model_name: str
    model_config = ConfigDict(from_attributes=True)

