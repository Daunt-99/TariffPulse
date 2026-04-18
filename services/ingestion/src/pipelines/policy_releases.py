from clients.policy import USTRFeedClient, WTOFeedClient


def ingest_policy_releases() -> list[dict]:
    clients = [USTRFeedClient(), WTOFeedClient()]
    return [item.payload for client in clients for item in client.fetch()]

