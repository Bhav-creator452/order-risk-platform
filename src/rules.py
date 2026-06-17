import logging
from dataclasses import dataclass
from models import Order , Customer
from abc import ABC , abstractmethod
logging.basicConfig(level=logging.INFO
                   ,format="%(asctime)s - %(levelname)s - %(message)s")

logger=logging.getLogger(__name__)


class RiskRule(ABC):
    @abstractmethod
    def evaluate(self, order: Order) -> int:
        pass


class HighAmount(RiskRule):
    def __init__(self, threshold)->None:
        self.threshold = threshold

        
    def evaluate(self,order: Order) -> int:
        if order.amount>self.threshold:
            logger.warning(
            f"HighAmountRisk fired for {order.id} because {order.amount} exceeds {self.threshold}")
            return 2
        return 0

class InternationalShipping(RiskRule):
    def evaluate(self,order: Order) -> int:
        if order.customer.country!=order.shipping_country:
            logger.info(
            f"InternationalShippingRisk fired for {order.id}",
            order.summary())
            return 2
        return 0

class NewCustomer(RiskRule):
    def evaluate(self,order: Order) -> int:
        if order.customer.total_past_orders==0:
            logger.info(
            f"NewCustomerRisk fired for {order.customer.id}",
            order.customer.email)
            return 1
        return 0
    
class CountryMismatch(RiskRule):
    def evaluate(self,order:Order) -> int:
        if order.customer.country!=order.shipping_country:
            logger.info(
            f"CountryMismatchRule fired for {order.id}",
            order.summary())
            return 2
        return 0


# ALL_RULES: list[RiskRule] = [HighAmount(),
#                             NewCustomer(),
#                             CountryMismatch(),
#                             InternationalShipping()
#                             ]




       




