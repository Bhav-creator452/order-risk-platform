
from pathlib import Path
import joblib

# Get the folder where this script is located
BASE_DIR = Path(__file__).resolve().parent

# Go to the project root
PROJECT_ROOT = BASE_DIR.parent

# Models folder
MODELS_DIR = PROJECT_ROOT / "models"

# Load model and test data
loaded_model = joblib.load(MODELS_DIR / "Random_Forest_model.joblib")
X_test = joblib.load(MODELS_DIR / "X_test.joblib")
y_test = joblib.load(MODELS_DIR / "y_test.joblib")

# Predict first five transactions
predictions = loaded_model.predict(X_test.iloc[:5])

print("Predictions:", predictions)
print("Actual Labels:", y_test.iloc[:5].values)