import pandas as pd

from models.xgboost_baseline import XGBoostBaseline
from pipelines.features import build_feature_frame


def train_model(events: pd.DataFrame, reactions: pd.DataFrame) -> dict:
    features = build_feature_frame(events, reactions)
    baseline = XGBoostBaseline()
    return baseline.train(features)

