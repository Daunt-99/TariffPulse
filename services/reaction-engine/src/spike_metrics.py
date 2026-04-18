import pandas as pd


def compute_volume_spike(volume_series: pd.Series) -> float:
    baseline = volume_series.iloc[:-1].mean() if len(volume_series) > 1 else 1.0
    return float(volume_series.iloc[-1] / baseline) if baseline else 0.0


def compute_volatility_spike(return_series: pd.Series) -> float:
    rolling_std = return_series.std() or 1.0
    return float(abs(return_series.iloc[-1]) / rolling_std)

