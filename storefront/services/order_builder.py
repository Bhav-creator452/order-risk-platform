from datetime import datetime


def build_order(form_data):
    """
    Convert HTML form data into the structure
    expected by the API.
    """

    now = datetime.now()

    order = {
        "transaction_amount": float(form_data["transaction_amount"]),
        "quantity": int(form_data["quantity"]),
        "customer_age": int(form_data["customer_age"]),
        "account_age_days": int(form_data["account_age_days"]),
        "payment_method": form_data["payment_method"],
        "product_category": form_data["product_category"],
        "shipping_address": form_data["shipping_address"],
        "billing_address": form_data["billing_address"],
        "transaction_date": now.isoformat(),
        "transaction_hour": now.hour,
        "device_used": form_data.get("device_used", "desktop"),
    }

    return order