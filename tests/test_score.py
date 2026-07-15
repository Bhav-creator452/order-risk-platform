from src.config import API_KEY
from tests.sample_data import valid_order


def test_score_valid_order(client, auth_headers,valid_order_payload):
    """
    Test that a valid order returns a successful prediction.
    """
    # Act
    response = client.post(
        "/score",
        json=valid_order_payload,
        headers=auth_headers,
    )

    # Assert
    assert response.status_code == 200

def test_score_invalid_body_missing_field(client,auth_headers,valid_order_payload):
    """
    Test that a request missing a required field
    returns a 422 validation error.
    """

    # Remove one required field
    valid_order_payload.pop("transaction_amount")

    # Act
    response = client.post(
        "/score",
        json=valid_order_payload,
        headers=auth_headers,
    )

    # Assert HTTP Response
    assert response.status_code == 422

def test_score_missing_api_key(client,valid_order_payload):
    """
    Test that a request without an API key
    is rejected.
    """

    # Act
    response = client.post(
        "/score",
        json=valid_order_payload,
    )

    # Assert HTTP Response
    assert response.status_code == 401
    
    # Assert Response Body
    body = response.json()

    assert "detail" in body
    assert body["detail"] == "Invalid or missing API key"

def test_score_invalid_api_key(client,valid_order_payload):
    """
    Test that an invalid API key
    is rejected.
    """

    headers = {
        "X-API-Key": "this-is-not-a-valid-key"
    }

    # Act
    response = client.post(
        "/score",
        json=valid_order_payload,
        headers=headers,
    )

    # Assert HTTP Response
    assert response.status_code == 401

    # Assert Response Body 
    body = response.json()

    assert "detail" in body
    assert body["detail"] == "Invalid or missing API key"
