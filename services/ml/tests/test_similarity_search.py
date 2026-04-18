from retrieval.similarity_search import retrieve_similar_events


def test_similarity_search() -> None:
    assert retrieve_similar_events("evt-2026-advanced-manufacturing")
