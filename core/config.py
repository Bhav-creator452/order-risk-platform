"""
Application configuration.

Reads configuration values from environment variables.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent

API_KEY = os.getenv("API_KEY")

MODEL_PATH = PROJECT_ROOT / os.getenv(
    "MODEL_PATH",
    "models/Random_Forest_model.joblib"
)

FEATURE_NAMES_PATH = PROJECT_ROOT / os.getenv(
    "FEATURE_NAMES_PATH",
    "models/feature_names.joblib"
)

SCALER_PATH = PROJECT_ROOT / os.getenv(
    "SCALER_PATH",
    "models/scaler.joblib"
)


# -------------------------------
# Startup validation
# -------------------------------

if not API_KEY:
    raise RuntimeError(
        "API_KEY is missing in .env"
    )

if not MODEL_PATH.exists():
    raise RuntimeError(
        f"Model file not found: {MODEL_PATH}"
    )

if not FEATURE_NAMES_PATH.exists():
    raise RuntimeError(
        f"Feature names file not found: {FEATURE_NAMES_PATH}"
    )

if not SCALER_PATH.exists():
    raise RuntimeError(
        f"Scaler file not found: {SCALER_PATH}"
    )

