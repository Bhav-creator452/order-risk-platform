import logging
from dataclasses import dataclass
from .models import Order 
from abc import ABC , abstractmethod
logging.basicConfig(level=logging.WARNING
                   ,format="%(asctime)s - %(levelname)s - %(message)s")

logger=logging.getLogger(__name__)


class RiskRule(ABC):
    @abstractmethod
    def evaluate(self, order: Order) -> int:
        pass


class HighAmount(RiskRule):
    def __init__(self, threshold: float)->None:
        self.threshold = threshold

        
    def evaluate(self,order: Order) -> int:
        if order.amount>self.threshold: 
            logger.warning(
            f"HighAmountRisk fired for {order.id} because {order.amount} exceeds {self.threshold}")
            Risk_points=2
            return Risk_points
        return 0

class AccountAge(RiskRule):
    def evaluate(self, order: Order) -> int:
        if order.customer.account_age_days <= 2:
            logger.info(
                f"AccountAgeRule fired for {order.customer.id} age= {order.customer.account_age_days} days"
            )
            Risk_points=2
            return Risk_points
        return 0

# class NewCustomer(RiskRule):
#     def evaluate(self,order: Order) -> int:
#         if order.customer.total_past_orders==0:
#             logger.info(
#             f"NewCustomerRisk fired for {order.customer.id}|{order.customer.email}")
#             Risk_points=1
#             return Risk_points
#         return 0
    
class CountryMismatch(RiskRule):
    def evaluate(self,order:Order) -> int:
        if order.customer.country!=order.shipping_country:
            logger.info(
            f"CountryMismatchRule fired for {order.id} | {order.summary()}")
            Risk_points=1
            return Risk_points
        return 0

class LargeItemCount(RiskRule):
    def __init__(self,threshold:int=10):
        self.threshold=threshold
       

    def evaluate(self,order:Order) -> int:
        if order.item_count>=self.threshold:
            logger.warning(
                f"LargeItemCount fired for {order.id} (items={order.item_count})")
            Risk_points=2
            return Risk_points
        return 0




       




