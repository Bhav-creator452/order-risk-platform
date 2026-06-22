
"""
CLI tool for scoring orders using the risk assessment model.
"""
import json
import sys

from models import Customer, Order
from rules import (
HighAmount,
NewCustomer,
AccountAge,
LargeItemCount,
CountryMismatch
)
from scorer import RiskScorer

def load_order(path: str) -> Order:
    with open(path, "r") as file:
        data = json.load(file)

    customer_data = data["customer"]
    order_data = data["order"]

    customer = Customer(
        id=customer_data["id"],
        email=customer_data["email"],
        country=customer_data["country"],
        total_past_orders=customer_data["total_past_orders"],
        account_age_days=customer_data["account_age_days"]
)

    order = Order(
        id=order_data["id"],
        amount=order_data["amount"],
        currency=order_data["currency"],
        shipping_country=order_data["shipping_country"],
        item_count=order_data["item_count"],
        customer=customer
)

    return order

def main():

    if len(sys.argv) != 2:
        print("Usage: python cli.py <order_json_file>")
        sys.exit(1)

    path = sys.argv[1]

    order = load_order(path)

    rules = [
        HighAmount(1000),
        NewCustomer(),
        AccountAge(),
        LargeItemCount(),
        CountryMismatch()
    
]

    scorer = RiskScorer(rules)

    score, label = scorer.score(order)

    print("\n===== Risk Assessment =====")
    print(f"Order ID : {order.id}")
    print(f"Score    : {score}")
    print(f"Label    : {label}")
    print("===========================\n")

if __name__ == "__main__":
    main()

        

























