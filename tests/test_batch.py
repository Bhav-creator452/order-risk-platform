from src.config import API_KEY
from tests.test_data import valid_order


def test_batch_score_valid_request(client,auth_headers):
    """
    Test that the batch scoring endpoint
    returns one prediction per input order.
    """

    # Arrange

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
        headers=auth_headers,
    )

    # Assert
    assert response.status_code == 200

    body = response.json()

    assert "results" in body
    assert isinstance(body["results"], list)
    assert len(body["results"]) == 2

