import logging
from models import Order
from rules import RiskRule

logger = logging.getLogger(__name__)


class RiskScorer:
    """
    Assembles and runs all risk rules against an order to produce a risk score and label.
    
    Score-to-Label Mapping:
    - 0-2: LOW risk
    - 3-5: MEDIUM risk
    - 6+: HIGH risk
    """
    
    # Thresholds for mapping numeric scores to risk labels
    LOW_THRESHOLD = 0
    MEDIUM_THRESHOLD = 3
    HIGH_THRESHOLD = 6
    
    def __init__(self, rules: list[RiskRule]):
        """
        Initialize the RiskScorer with a collection of rules.
        
        Arguments:
            rules: List of RiskRule classobjects to apply during scoring
        """
        self.rules = rules
    
    def score(self, order: Order) -> tuple[int, str]:
        """
        Score an order by running all rules and aggregating their contributions.
        
        Arguments:
            order: containing order data
            
        Returns:
            Tuple of (numeric_score, risk_label) where:
            - numeric_score is the sum of all rule contributions
            - risk_label is one of 'LOW', 'MEDIUM', or 'HIGH'
        """
        total_score = 0
        
        # Run each rule and sum the contributions
        for rule in self.rules:
            contribution = rule.evaluate(order)
            total_score += contribution
        
        # Map numeric score to risk label
        risk_label = self._map_score_to_label(total_score)
        
        # Log the final score and label
        logger.info(
            f"Order{order.id} scored - /nScore: {total_score}, Label: {risk_label}"
        
        )
        
        return total_score, risk_label
    
    def _map_score_to_label(self, score: int) -> str:
        """
        Map a numeric score to a risk label.
        
        Arguments:
            score: Numeric risk score
            
        Returns:
            Risk label: 'LOW', 'MEDIUM', or 'HIGH'
        """
        if score >= self.HIGH_THRESHOLD:
            return 'HIGH'
        elif score >= self.MEDIUM_THRESHOLD:
            return 'MEDIUM'
        else:
            return 'LOW'
