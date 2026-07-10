"""
predictor.py

Loads the trained Random Forest model and provides
methods for generating fraud predictions.
"""

from __future__ import annotations

from pathlib import Path
import joblib


class FraudPredictor:
    """
    Wrapper around the trained Random Forest model.
    Loads the model once and reuses it for every prediction.
    """

    def __init__(self) -> None:

        project_root = Path(__file__).resolve().parent.parent
        model_dir = project_root / "models"

        self.model = joblib.load(
            model_dir / "Random_Forest_model.joblib"
        )

        self.feature_names = joblib.load(
            model_dir / "feature_names.joblib"
        )
        self.scaler = joblib.load(
            model_dir / "scaler.joblib"
        )
        
        

    @property
    def expected_features(self) -> list[str]:
        """
        Returns the feature names used during training.
        """

        return self.feature_names

    def predict(self, features):
        """
        Predict fraud label.

        Parameters
        ----------
        features : pandas.DataFrame

        Returns
        -------
        int
            0 = Legitimate
            1 = Fraudulent
        """

        prediction = self.model.predict(features)

        return int(prediction[0])

    def predict_probability(self, features):
        """
        Predict fraud probability.

        Returns
        -------
        float
            Fraud probability.
        """

        probabilities = self.model.predict_proba(features)

        return float(probabilities[0][1])

    def score(self, features):
        """
        Complete prediction.

        Returns
        -------
        dict
        """

        probability = self.predict_probability(features)

        prediction = self.predict(features)

        label = (
            "Fraud"
            if prediction == 1
            else "Legitimate"
        )

        return {
            "prediction": prediction,
            "label": label,
            "fraud_probability": round(probability, 4),
        }