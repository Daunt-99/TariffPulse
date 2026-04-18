from datetime import date

from pydantic import BaseModel, ConfigDict

from app.schemas.common import LagLabelEnum, SectorEnum


class SectorReactionRead(BaseModel):
    id: str
    event_id: str
    sector: SectorEnum
    window_start: date
    window_end: date
    abnormal_return: float
    cumulative_abnormal_return: float
    volume_spike: float
    volatility_spike: float
    lag_label: LagLabelEnum
    model_config = ConfigDict(from_attributes=True)

