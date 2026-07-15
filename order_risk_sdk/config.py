# order_risk_sdk/config.py

from dataclasses import dataclass


@dataclass
class SDKConfig:
    """
    Configuration for the Order Risk SDK.
    """

    base_url: str = "http://127.0.0.1:8000"
    api_key: str | None = None
    timeout: int = 30