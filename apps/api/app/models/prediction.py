from datetime import datetime

from sqlalchemy import DateTime, Float, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class PredictionORM(Base):
    __tablename__ = "predictions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    event_id: Mapped[str] = mapped_column(String(64), index=True)
    sector: Mapped[str] = mapped_column(String(64), nullable=False)
    predicted_reaction_speed: Mapped[str] = mapped_column(String(32), nullable=False)
    predicted_magnitude: Mapped[float] = mapped_column(Float, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    similar_past_events: Mapped[list[str]] = mapped_column(JSONB, default=list)
    model_name: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

