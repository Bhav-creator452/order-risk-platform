from order_risk_sdk import OrderRiskClient
from config import SDK_API_KEY, SDK_BASE_URL
from .order_builder import build_order

client = OrderRiskClient(
    base_url=SDK_BASE_URL,
    api_key=SDK_API_KEY,
)

def score_order(form_data):
    """
    Build an order and send it to the SDK.
    """

    order = build_order(form_data)

    return client.score_order(order)