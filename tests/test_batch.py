from src.config import API_KEY
from tests.test_data import valid_order


def test_batch_score_valid_request(client):
    """
    Test that the batch scoring endpoint
    returns one prediction per input order.
    """

    # Arrange
    headers = {
        "X-API-Key": API_KEY
    }

    payload = {
        "orders": [
            valid_order(),
            valid_order(),
        ]
    }

    # Act
    response = client.post(
        "/score/batch",
        json=payload,
        headers=headers,
    )

    # Assert
    assert response.status_code == 200

    body = response.json()

    assert "results" in body
    assert isinstance(body["results"], list)
    assert len(body["results"]) == 2

