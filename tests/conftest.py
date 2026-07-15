import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.config import API_KEY

from tests.sample_data import valid_order

@pytest.fixture
def client():
    """ 
    Create a reusable TestClient for FastAPI app
    """
    return TestClient(app)

@pytest.fixture
def auth_headers():
    """
    Valid authentication headers for API requests.
    """
    return {
        "X-API-Key": API_KEY
    }

@pytest.fixture
def valid_order_payload():
    """
    Returns a fresh valid order payload for each test.
    """
    return valid_order()