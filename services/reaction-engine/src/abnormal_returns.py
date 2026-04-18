import pandas as pd


def compute_abnormal_returns(sector_returns: pd.Series, benchmark_returns: pd.Series) -> pd.Series:
    """Baseline abnormal return definition using SPY as market benchmark."""
    aligned_sector, aligned_benchmark = sector_returns.align(benchmark_returns, join="inner")
    return aligned_sector - aligned_benchmark


def compute_cumulative_abnormal_returns(abnormal_returns: pd.Series) -> float:
    return float(abnormal_returns.sum())

