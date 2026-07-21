from ml.predictor import FraudPredictor
from ml.preprocessing import FeaturePreprocessor

# Load predictor once
predictor = FraudPredictor()

# Create preprocessor once
preprocessor = FeaturePreprocessor(
    feature_names=predictor.expected_features,
    scaler=predictor.scaler,
)

"""
Shared application dependencies.

These objects are created once when the application starts
and reused throughout the application.
"""