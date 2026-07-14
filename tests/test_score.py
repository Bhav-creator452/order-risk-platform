from src.config import API_KEY
from tests.test_data import valid_order


def test_score_valid_order(client):
    """
    Test that a valid order returns a successful prediction.
    """

    # Arrange
    headers = {
        "X-API-Key": API_KEY
    }

    payload = valid_order()
    

    # Act
    response = client.post(
        "/score",
        json=payload,
        headers=headers,
    )

    # Assert
    assert response.status_code == 200

def test_score_invalid_body_missing_field(client):
    """
    Test that a request missing a required field
    returns a 422 validation error.
    """

    # Arrange
    headers = {
        "X-API-Key": API_KEY
    }

    payload = valid_order()

    # Remove one required field
    payload.pop("transaction_amount")

    # Act
    response = client.post(
        "/score",
        json=payload,
        headers=headers,
    )

    # Assert
    assert response.status_code == 422

def test_score_missing_api_key(client):
    """
    Test that a request without an API key
    is rejected.
    """

    # Arrange
    payload = valid_order()

    # Act
    response = client.post(
        "/score",
        json=payload,
    )

    # Assert
    assert response.status_code == 401

    body = response.json()

    assert "detail" in body
    assert body["detail"] == "Invalid or missing API key"

def test_score_invalid_api_key(client):
    """
    Test that an invalid API key
    is rejected.
    """

    # Arrange
    payload = valid_order()

    headers = {
        "X-API-Key": "this-is-not-a-valid-key"
    }

    # Act
    response = client.post(
        "/score",
        json=payload,
        headers=headers,
    )

    # Assert
    assert response.status_code == 401

    body = response.json()

    assert "detail" in body
    assert body["detail"] == "Invalid or missing API key"
    