from typing import List

from src.dependencies import predictor, preprocessor
from src.schemas import (
    OrderRequest,
    ScoreResponse,
    BatchScoreRequest,
    BatchScoreResponse,
)

def score_single_order(order: OrderRequest) -> ScoreResponse:
    """
    Shared business logic for scoring a single order.

    Responsibilities:
    - Convert request model to dictionary
    - Preprocess features
    - Generate prediction
    - Return ScoreResponse
    """
    order_dict = order.model_dump()

    # Step 2: Prepare the features for the ML model
    features = preprocessor.prepare(order_dict)

    # Step 3: Generate the prediction
    prediction = predictor.score(features)

    # Step 4: Return the prediction
    return prediction


def score_batch(
    request: BatchScoreRequest,
) -> BatchScoreResponse:
    """
    Score multiple orders while preserving input order.

    Args:
        orders: List of validated order requests.

    Returns:
        List of prediction responses in the same order.
    """

    results = []

    for order in request.orders:
        results.append(
            score_single_order(order)
        )

    return BatchScoreResponse(
    results=results
)