# order_risk_sdk/client.py

import requests

from .config import SDKConfig
from .exceptions import APIError

from typing import Any

class OrderRiskClient:
    """
    Client for interacting with the Order Risk API.
    """
    def __init__(
        self,
        config: SDKConfig | None = None,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        timeout: int | None = None,
    ):
        """
        Initialize the client.

        You can either provide an SDKConfig object or individual
        configuration values.
        """

        if config is not None:
            self.config = config
            return
        default_config = SDKConfig()

        self.config = SDKConfig(
        base_url = (
        base_url
        if base_url is not None
        else default_config.base_url
        ),
        api_key=api_key,
        timeout=timeout or default_config.timeout,
    )
        
    @property
    def headers(self) -> dict[str, str]:
        """
        Build the headers for API requests.
        """
        headers = {}

        if self.config.api_key:
            headers["X-API-Key"] = self.config.api_key

        return headers
    
    def score_order(
    self,
    order: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Send an order to the API and return the prediction.
        """
        try:
            response = requests.post(
                url=f"{self.config.base_url}/score",
                json=order,
                headers=self.headers,
                timeout=self.config.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as e:
            raise APIError(
                f"API returned {response.status_code}: {response.text}"
            ) from e

        except requests.exceptions.ConnectionError as e:
            raise APIError(
                "Could not connect to the Order Risk API."
            ) from e

        except requests.exceptions.Timeout as e:
            raise APIError(
                "The request timed out."
            ) from e

        except requests.exceptions.RequestException as e:
            raise APIError(
                f"Unexpected request error: {e}"
            ) from e