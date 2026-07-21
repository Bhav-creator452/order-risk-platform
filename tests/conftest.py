import pytest
from fastapi.testclient import TestClient

from app.app import app
from core.config import API_KEY

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