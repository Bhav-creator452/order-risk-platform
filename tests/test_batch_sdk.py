from order_risk_sdk import OrderRiskClient, APIError


def main():
    client = OrderRiskClient(
        base_url="http://127.0.0.1:8000",
        api_key="5c040e601dbfb8b64fb8142798d5a6b2e3e5579a4656a7041a1187c91f89c748",   # Replace with your API key
    )

    orders = [
        {
          "transaction_amount": 1499.99,
        "quantity": 2,
        "customer_age": 28,
        "account_age_days": 365,
        "transaction_hour": 14,
        "transaction_date": "2025-06-20 15:20:04",
        "payment_method": "bank transfer",
        "product_category": "electronics",
        "device_used": "mobile",
        "shipping_address": "Delhi",
        "billing_address": "Delhi"  
        },
        {
            "transaction_amount": 1499.99,
            "quantity": 2,
            "customer_age": 28,
            "account_age_days": 365,
            "transaction_hour": 14,
            "transaction_date": "2025-06-20 15:20:04",
            "payment_method": "bank transfer",
            "product_category": "electronics",
            "device_used": "mobile",
            "shipping_address": "Delhi",
            "billing_address": "Delhi"
        },
    ]

    try:
        result = client.batch_score(orders)

        print("Batch Prediction Result:")
        print(result)

    except APIError as e:
        print(f"SDK Error: {e}")


if __name__ == "__main__":
    main()