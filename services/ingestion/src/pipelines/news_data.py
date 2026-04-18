from clients.news import GDELTClient, NewsApiClient


def ingest_news(query: str) -> list[dict]:
    """Fetch tariff-related news headlines and article metadata."""
    clients = [NewsApiClient(), GDELTClient()]
    return [item.payload for client in clients for item in client.fetch(query)]

