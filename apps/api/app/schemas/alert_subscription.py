from pydantic import BaseModel, ConfigDict, EmailStr

from app.schemas.common import LagLabelEnum, SectorEnum


class AlertSubscriptionBase(BaseModel):
    email: EmailStr
    sectors: list[SectorEnum]
    minimum_severity: float
    lag_labels: list[LagLabelEnum]
    delivery_channel: str = "email"


class AlertSubscriptionRead(AlertSubscriptionBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

