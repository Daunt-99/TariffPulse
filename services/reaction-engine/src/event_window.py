from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class EventWindow:
    start: date
    event_date: date
    end: date


def build_event_window(event_date: date, pre_days: int = 5, post_days: int = 10) -> EventWindow:
    """Construct a simple T-5 to T+10 event window."""
    return EventWindow(
        start=event_date - timedelta(days=pre_days),
        event_date=event_date,
        end=event_date + timedelta(days=post_days),
    )

