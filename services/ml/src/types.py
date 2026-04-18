from dataclasses import dataclass


@dataclass
class SectorPrediction:
    sector: str
    predicted_reaction_speed: str
    predicted_magnitude: float
    confidence: float
    similar_past_events: list[str]

