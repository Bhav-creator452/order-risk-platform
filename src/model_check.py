import models
customer1=models.customer(
    id="C1001",
    email=1,
    country="CA",
    total_past_orders=10
)
order1=models.order(
    id="O1001",
    amount=120.0,
    currency="CAD",
    customer=customer1,
    item_count=2,
    shipping_country="CA"
)
customer2=models.customer(
    id="C1002",
    email="john.doe@example.com",
    country="US",
    total_past_orders=5
)
order2=models.order(
    id="O1002",
    amount=1500.0,
    currency="USD",
    customer=customer2,
    item_count=3,
    shipping_country="US"
)

print("Customer ID:", customer1)
print("Order Amount:", order1.amount)
print("Is this high value order:", order1.is_high_value())
print("Customer ID:", customer2.id)
print("Order Amount:", order2.amount)
print("Is this high value order:", order2.is_high_value())


print(dir(models.order))