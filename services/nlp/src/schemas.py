from pydantic import BaseModel, Field


class ExtractedTariffEvent(BaseModel):
    title: str
    summary: str
    countries: list[str] = Field(default_factory=list)
    goods: list[str] = Field(default_factory=list)
    tariff_rate: float | None = None
    event_date: str
    severity_score: float
    sectors: list[str] = Field(default_factory=list)
    event_category: str

