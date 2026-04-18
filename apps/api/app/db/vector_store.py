from dataclasses import dataclass

from app.core.config import settings


@dataclass
class SimilarityMatch:
    event_id: str
    score: float


class VectorStore:
    """Minimal abstraction so pgvector or Pinecone can be swapped later."""

    def __init__(self, provider: str) -> None:
        self.provider = provider

    def upsert_event_embedding(self, event_id: str, vector: list[float]) -> None:
        # TODO: persist vectors to pgvector or Pinecone.
        _ = (event_id, vector)

    def find_similar_events(self, vector: list[float], top_k: int = 5) -> list[SimilarityMatch]:
        # TODO: replace mock similarity with actual nearest-neighbor retrieval.
        _ = vector
        return [
            SimilarityMatch(event_id="evt-2025-steel-escalation", score=0.91),
            SimilarityMatch(event_id="evt-2024-ev-components-review", score=0.84),
        ][:top_k]


def get_vector_store() -> VectorStore:
    return VectorStore(provider=settings.vector_store_provider)

