
import joblib

# Load the saved model
loaded_model = joblib.load("models/Random_Forest_model.joblib")

# Load test data
X_test = joblib.load("models/X_test.joblib")

# Original model predictions (from the loaded model)
loaded_predictions = loaded_model.predict(X_test.iloc[:5])

print("Reloaded Model Predictions:", loaded_predictions)

