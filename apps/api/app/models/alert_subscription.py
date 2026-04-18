from datetime import datetime

from sqlalchemy import DateTime, Float, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class AlertSubscriptionORM(Base):
    __tablename__ = "alert_subscriptions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    sectors: Mapped[list[str]] = mapped_column(JSONB, default=list)
    minimum_severity: Mapped[float] = mapped_column(Float, default=0.5)
    lag_labels: Mapped[list[str]] = mapped_column(JSONB, default=list)
    delivery_channel: Mapped[str] = mapped_column(String(32), default="email")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

