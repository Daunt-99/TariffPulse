import pandas as pd

from models.xgboost_baseline import XGBoostBaseline
from pipelines.features import build_feature_frame
from retrieval.similarity_search import retrieve_similar_events


def run_inference(events: pd.DataFrame, reactions: pd.DataFrame) -> list[dict]:
    features = build_feature_frame(events, reactions)
    baseline = XGBoostBaseline()
    predictions = baseline.predict(features)
    for prediction, (_, row) in zip(predictions, features.iterrows(), strict=False):
        prediction["similar_past_events"] = retrieve_similar_events(row["id"])
    return predictions

