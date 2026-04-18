from dataclasses import dataclass

import pandas as pd


@dataclass
class XGBoostBaseline:
    model_name: str = "xgboost_baseline_v1"

    def train(self, frame: pd.DataFrame) -> dict:
        # TODO: fit classifier/regressor targets once labels are finalized.
        return {"rows": len(frame), "model_name": self.model_name}

    def predict(self, frame: pd.DataFrame) -> list[dict]:
        return [
            {
                "sector": row["sector"],
                "predicted_reaction_speed": row.get("lag_label", "lagged"),
                "predicted_magnitude": round(float(row.get("cumulative_abnormal_return", -1.2)), 2),
                "confidence": 0.74,
            }
            for _, row in frame.iterrows()
        ]

