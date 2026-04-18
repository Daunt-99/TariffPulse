from datetime import date, datetime

from sqlalchemy import Date, DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SectorReactionORM(Base):
    __tablename__ = "sector_reactions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    event_id: Mapped[str] = mapped_column(String(64), index=True)
    sector: Mapped[str] = mapped_column(String(64), nullable=False)
    window_start: Mapped[date] = mapped_column(Date, nullable=False)
    window_end: Mapped[date] = mapped_column(Date, nullable=False)
    abnormal_return: Mapped[float] = mapped_column(Float, default=0.0)
    cumulative_abnormal_return: Mapped[float] = mapped_column(Float, default=0.0)
    volume_spike: Mapped[float] = mapped_column(Float, default=0.0)
    volatility_spike: Mapped[float] = mapped_column(Float, default=0.0)
    lag_label: Mapped[str] = mapped_column(String(32), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

