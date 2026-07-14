import pytest
from fastapi.testclient import TestClient

from src.app import app

@pytest.fixture
def client():
    '''
    Create a reusable TestClient for FastAPI app
    '''
    return TestClient(app)