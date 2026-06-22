import models
import rules
from scorer import RiskScorer

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



Rules = [
    rules.HighAmount(threshold=1000),
    rules.AccountAge(),
    rules.NewCustomer(),
    rules.CountryMismatch(),
    rules.LargeItemCount()
]

score, label = RiskScorer(Rules).score(order1)


 

    
