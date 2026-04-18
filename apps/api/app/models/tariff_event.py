from datetime import date, datetime

from sqlalchemy import Date, DateTime, Float, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class TariffEventORM(Base):
    __tablename__ = "tariff_events"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    source: Mapped[str] = mapped_column(String(128), nullable=False)
    event_date: Mapped[date] = mapped_column(Date, nullable=False)
    countries: Mapped[list[str]] = mapped_column(JSONB, default=list)
    goods: Mapped[list[str]] = mapped_column(JSONB, default=list)
    tariff_rate: Mapped[float | None] = mapped_column(Float, nullable=True)
    event_category: Mapped[str] = mapped_column(String(64), nullable=False)
    severity_score: Mapped[float] = mapped_column(Float, nullable=False)
    sectors: Mapped[list[str]] = mapped_column(JSONB, default=list)
    status: Mapped[str] = mapped_column(String(32), default="draft")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

