from datetime import date

from pydantic import BaseModel, ConfigDict

from app.schemas.common import EventCategoryEnum, SectorEnum


class TariffEventBase(BaseModel):
    title: str
    summary: str
    source: str
    event_date: date
    countries: list[str]
    goods: list[str]
    tariff_rate: float | None = None
    event_category: EventCategoryEnum
    severity_score: float
    sectors: list[SectorEnum]
    status: str = "draft"


class TariffEventRead(TariffEventBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

