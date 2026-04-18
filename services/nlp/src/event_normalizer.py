from schemas import ExtractedTariffEvent


def normalize_event(payload: dict) -> ExtractedTariffEvent:
    """Normalize raw extraction output into the shared event contract."""
    return ExtractedTariffEvent.model_validate(payload)

