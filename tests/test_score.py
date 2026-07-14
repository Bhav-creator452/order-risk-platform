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