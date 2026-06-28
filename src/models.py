from dataclasses import dataclass
from typing import Optional
@dataclass
class Customer:
    id: str
    email: Optional[str] = None
    country: Optional[str] = None
    #total_past_orders: int=0
    account_age_days :int = 0

    # def id_valid(self):
    #     if not isinstance(self.id, str) or not self.id.startswith("C"):
    #         raise ValueError("Customer ID must be a string starting with 'C'")
    
    # def email_valid(self):
    #     if not isinstance(self.email, str) or "@" not in self.email:
    #         raise TypeError("Customer email must be a valid email address")
    #     elif not self.email.endswith((".com", ".net", ".org")):
    #         raise ValueError("Customer email must end with .com, .net, or .org")
    #     elif self.email.count("@") != 1:
    #         raise ValueError("Customer email must contain exactly one '@' symbol")
    #     elif self.email.startswith("@") or self.email.endswith("@"):
    #         raise ValueError("Customer email cannot start or end with '@' symbol")
    #     elif self.email.startswith(".") or self.email.endswith("."):
    #         raise ValueError("Customer email cannot start or end with '.' symbol")
        
    # def country_valid(self):
    #     if not isinstance(self.country, str) or len(self.country) != 2:
    #         raise ValueError("Customer country must be a 2-letter country code")
        
    # def total_past_orders_valid(self):
    #     if not isinstance(self.total_past_orders, int) or self.total_past_orders < 0:
    #         raise ValueError("Customer total past orders must be a non-negative integer")
    
    # def __post_init__(self):
    #     # self.id_valid()
    #     # self.email_valid()
    #     # self.country_valid()
    #     # self.total_past_orders_valid()
    #     pass
@dataclass
class Order:
    id:str
    amount: float
    currency: str
    customer:Customer
    item_count: int
    shipping_country: str

    # def is_high_value(self, threshold: float = 1000.0) -> bool:
    #     return self.amount > threshold

    # def validate_order(self):
    #     if not isinstance(self.id, str) or not self.id.startswith("O"):
    #         raise ValueError("Order ID must be a string starting with 'O'")
    #     if not isinstance(self.amount, (int, float)) or self.amount < 0:
    #         raise ValueError("Order amount must be a non-negative number")
    #     if not isinstance(self.currency, str) or len(self.currency) != 3:
    #         raise ValueError("Order currency must be a 3-letter currency code")
    #     if not isinstance(self.customer, Customer):
    #         raise ValueError("Order customer must be a valid Customer object")
    #     if not isinstance(self.item_count, int) or self.item_count < 0:
    #         raise ValueError("Order item count must be a non-negative integer")
    #     if not isinstance(self.shipping_country, str) or len(self.shipping_country) != 2:
    #         raise ValueError("Order shipping country must be a 2-letter country code")
    
    # def summary(self):
    #     return f"Order{self.id}:{self.amount} {self.currency} to {self.shipping_country} ({self.item_count} items)"
        
    # def __post_init__(self):
    #     # self.validate_order()
    #     # self.summary()
    #     pass
