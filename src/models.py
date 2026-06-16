from dataclasses import dataclass
@dataclass
class customer:
    id: str
    email: str
    country: str
    total_past_orders: int
    
@dataclass
class order:
    id:str
    amount: float
    currency: str
    customer:customer
    item_count: int
    shipping_country: str

    def is_high_value(self, threshold: float = 1000.0) -> bool:
        return self.amount > threshold
