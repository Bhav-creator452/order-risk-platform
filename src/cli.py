
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

        

























# import argparse
# import json
# import sys
# from pathlib import Path


# def load_order_json(filepath):
#     """Load and parse an order JSON file."""
#     try:
#         with open(filepath, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         print(f"Error: File '{filepath}' not found.", file=sys.stderr)
#         sys.exit(1)
#     except json.JSONDecodeError as e:
#         print(f"Error: Invalid JSON in '{filepath}': {e}", file=sys.stderr)
#         sys.exit(1)


# def score_order(order):
#     """
#     Score an order based on risk factors.
    
#     Returns:
#         tuple: (score, label) where score is 0-100 and label is 'low', 'medium', or 'high'
#     """
#     score = 0
    
#     # Amount-based scoring
#     amount = order.get('amount', 0)
#     if amount > 10000:
#         score += 40
#     elif amount > 5000:
#         score += 25
#     elif amount > 1000:
#         score += 10
    
#     # Customer history
#     if order.get('is_new_customer', False):
#         score += 20
    
#     # Payment method risk
#     payment_method = order.get('payment_method', 'credit_card').lower()
#     if payment_method == 'wire_transfer':
#         score += 15
#     elif payment_method == 'cryptocurrency':
#         score += 30
    
#     # Geographic risk
#     country = order.get('country', 'US').upper()
#     high_risk_countries = ['NG', 'RU', 'KP', 'IR']
#     if country in high_risk_countries:
#         score += 25
    
#     # Velocity check
#     recent_orders = order.get('recent_orders_24h', 0)
#     if recent_orders > 5:
#         score += 20
    
#     # Clamp score to 0-100
#     score = min(100, max(0, score))
    
#     # Determine label
#     if score >= 70:
#         label = 'high'
#     elif score >= 40:
#         label = 'medium'
#     else:
#         label = 'low'
    
#     return score, label


# def main():
#     """Main entry point for the CLI tool."""
#     parser = argparse.ArgumentParser(
#         description='Score orders for risk assessment'
#     )
#     parser.add_argument(
#         'order_file',
#         type=str,
#         help='Path to the order JSON file'
#     )
    
#     args = parser.parse_args()
    
#     # Load order
#     order = load_order_json(args.order_file)
    
#     # Score order
#     score, label = score_order(order)
    
#     # Print results
#     print(f"Score: {score}")
#     print(f"Label: {label}")


# if __name__ == '__main__':
#     main()
