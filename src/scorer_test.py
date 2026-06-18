from models import Order , Customer
from scorer import RiskScorer
from rules import(
    HighAmount,
    LargeItemCount,
    NewCustomer,
    AccountAge,
    CountryMismatch
)
rules = [
    HighAmount(1000),
    NewCustomer(),
    AccountAge(),
    LargeItemCount(),
    CountryMismatch()
]

#customer with low risk
customer1 = Customer(
    id="C1",
    email="a@test.com",
    country="CA",
    total_past_orders=20,
    account_age_days=200
)

order1 = Order(
    id="O1",
    amount=100,
    currency="CAD",
    shipping_country="CA",
    item_count=1,
    customer=customer1
)

scorer = RiskScorer(rules)
score,label=scorer.score(order1)
print("Risk Score of the Order is:",score)
print("Label according to the Risk Score :", label)

#Customer with Medium Risk
customer2 = Customer(
    id="C2",
    email="b@test.com",
    country="CA",
    total_past_orders=0,
    account_age_days=200
)

order2 = Order(
    id="O2",
    amount=100,
    currency="CAD",
    shipping_country="US",
    item_count=15,
    customer=customer2
)
scorer = RiskScorer(rules)
score,label=scorer.score(order2)
print("Risk Score of the Order is:",score)
print("Label according to the Risk Score :", label)

#Customer with High Risk
customer3 = Customer(
    id="C3",
    email="c@test.com",
    country="CA",
    total_past_orders=0,
    account_age_days=2
)

order3 = Order(
    id="O3",
    amount=10000,
    currency="CAD",
    shipping_country="US",
    item_count=15,
    customer=customer3
)
scorer = RiskScorer(rules)
score,label=scorer.score(order3)
print("Risk Score of the Order is:",score)
print("Label according to the Risk Score :", label)