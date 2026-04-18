from datetime import date

import pandas as pd

from abnormal_returns import compute_abnormal_returns, compute_cumulative_abnormal_returns
from event_window import build_event_window
from lag_classifier import classify_lag
from spike_metrics import compute_volume_spike, compute_volatility_spike


def analyze_sector_reaction(
    event_date: date,
    sector_returns: pd.Series,
    benchmark_returns: pd.Series,
    volume_series: pd.Series,
) -> dict:
    window = build_event_window(event_date)
    abnormal = compute_abnormal_returns(sector_returns, benchmark_returns)
    car = compute_cumulative_abnormal_returns(abnormal)
    early_car = float(abnormal.head(3).sum())
    return {
      "window_start": window.start.isoformat(),
      "window_end": window.end.isoformat(),
      "abnormal_return": float(abnormal.iloc[-1]),
      "cumulative_abnormal_return": car,
      "volume_spike": compute_volume_spike(volume_series),
      "volatility_spike": compute_volatility_spike(sector_returns),
      "lag_label": classify_lag(float(abnormal.iloc[-1]), early_car, car),
    }

