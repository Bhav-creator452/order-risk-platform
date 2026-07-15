from datetime import datetime


def valid_order():
    """
    Returns a valid OrderRequest payload.
    """

    return {
        "transaction_amount": 1499.99,
        "quantity": 2,
        "customer_age": 28,
        "account_age_days": 365,
        "transaction_hour": 14,
        "transaction_date": datetime.now().isoformat(),

        "payment_method": "credit card",
        "product_category": "home & garden",
        "device_used": "tablet",

        "shipping_address": "Delhi",
        "billing_address": "Delhi",
    }