import models
import rules

customer1=models.Customer(
    id="C1001",
    email="jane@doeexample.com",
    country="CA",
    total_past_orders=10,
    account_age_days=200
)
order1=models.Order(
    id="O1001",
    amount=120.0,
    currency="CAD",
    customer=customer1,
    item_count=15,
    shipping_country="CA"
)
customer2=models.Customer(
    id="C1002",
    email="john.doe@example.com",
    country="US",
    total_past_orders=5
)
order2=models.Order(
    id="O1002",
    amount=1500.0,
    currency="USD",
    customer=customer2,
    item_count=3,
    shipping_country="CA")

# order = models.Order(
#     id="O1001",
#     amount=500,
#     currency="CAD",
#     shipping_country="CA",
#     item_count=15,
#     customer=customer1
# )
# print("Customer Email:", customer1.email)
# print("Customer ID:", customer1.id)

# print("Order Summary:", order1.summary())
# print("Is this high value order:", order1.is_high_value())

# print("Customer Email:", customer2.email)
# print("Customer ID:", customer2.id)

# print("Order Summary:", order2.summary())
# print("Is this high value order:", order2.is_high_value())
#print("Customer1", customer1, "Order", order1)
Rules = [
    rules.HighAmount(threshold=1000),
    rules.AccountAge(),
    rules.NewCustomer(),
    rules.CountryMismatch(),
    rules.LargeItemCount()
]

Risk_Score=0
for rule in Rules:
    Risk_Score+=rule.evaluate(order1)
    print("Risk Score for Order1:", Risk_Score)

 

    
