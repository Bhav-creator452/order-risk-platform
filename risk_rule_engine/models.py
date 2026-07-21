from dataclasses import dataclass
from typing import Optional
@dataclass
class Customer:
    id: str
    email: Optional[str] = None
    country: Optional[str] = None
    total_past_orders: int=0
    account_age_days :int = 0

    
@dataclass
class Order:
    id:str
    amount: float
    currency: str
    customer:Customer
    item_count: int
    shipping_country: str

    