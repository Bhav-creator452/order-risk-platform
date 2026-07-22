"""
predictor.py

Loads the trained Random Forest model and provides
methods for generating fraud predictions.
"""

from __future__ import annotations
from typing import Any

import joblib

import pandas as pd

from core.logger import logger
from core.config import (
    MODEL_PATH,
    FEATURE_NAMES_PATH,
    SCALER_PATH,
)

logger.info("Loading Random Forest model...")

class FraudPredictor:
    """
    Wrapper around the trained Random Forest model.
    Loads the model once and reuses it for every prediction.
    """

    def __init__(self) -> None:

        self.model = joblib.load(MODEL_PATH)
        
        logger.info("Random Forest model loaded successfully.")

        self.feature_names = joblib.load(FEATURE_NAMES_PATH)

        self.scaler = joblib.load(SCALER_PATH)
        
    @property
    def expected_features(self) -> list[str]:
        """
        Returns the feature names used during training.
        """

        return self.feature_names

    def predict(
    self,
    features: pd.DataFrame,
    ) -> int:
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

    def predict_probability(
    self,
    features: pd.DataFrame,
    ) -> float:
        """
        Predict fraud probability.

        Returns
        -------
        float
            Fraud probability.
        """

        probabilities = self.model.predict_proba(features)

        return float(probabilities[0][1])

    def score(
    self,
    features: pd.DataFrame,
    ) -> dict[str,Any]:
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
        if probability < 0.30:
            risk_level = "LOW"
        elif probability < 0.70:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"

        return {
            "prediction": prediction,
            "label": label,
            "risk_level": risk_level,
            "fraud_probability": round(probability, 4),
            "fraud_probability_percentage": f"{probability * 100:.2f}%",
        }