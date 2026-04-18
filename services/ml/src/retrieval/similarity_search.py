def retrieve_similar_events(event_id: str, top_k: int = 3) -> list[str]:
    """Temporary stand-in for pgvector or Pinecone retrieval."""
    library = {
        "evt-2026-advanced-manufacturing": [
            "evt-2025-steel-escalation",
            "evt-2024-machinery-review",
            "evt-2024-semiconductor-controls",
        ]
    }
    return library.get(event_id, [])[:top_k]

