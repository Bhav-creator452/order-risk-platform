import os
from pathlib import Path

from dotenv import load_dotenv

# Project root (one level above the storefront directory)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

SDK_BASE_URL = os.getenv(
    "SDK_BASE_URL",
    "http://127.0.0.1:8000",
)
SDK_API_KEY = os.getenv("API_KEY")