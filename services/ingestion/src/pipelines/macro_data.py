from clients.macro import FredClient


def ingest_macro_series(series_ids: list[str]) -> list[dict]:
    client = FredClient()
    return [item.payload for series_id in series_ids for item in client.fetch(series_id)]

