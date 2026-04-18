import pandas as pd


def build_feature_frame(events: pd.DataFrame, reactions: pd.DataFrame) -> pd.DataFrame:
    """Join normalized event intelligence with reaction-engine outputs."""
    merged = events.merge(reactions, left_on="id", right_on="event_id", how="left")
    merged["country_count"] = merged["countries"].apply(len)
    merged["goods_count"] = merged["goods"].apply(len)
    merged["sector_count"] = merged["sectors"].apply(len)
    return merged

