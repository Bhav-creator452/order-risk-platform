from fastapi import FastAPI
from pydantic import BaseModel

from src.predictor import FraudPredictor
from src.preprocessing import FeaturePreprocessor

from fastapi import Depends
from src.auth import verify_api_key

from fastapi import HTTPException

import logging

app = FastAPI(
    title="Order Risk Platform API",
    version="1.0.0"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

class OrderRequest(BaseModel):
    transaction_amount: float
    quantity: int
    customer_age: int
    account_age_days: int
    transaction_hour: int

    transaction_date: str

    payment_method: str
    product_category: str
    device_used: str

    shipping_address: str
    billing_address: str

predictor=FraudPredictor()

preprocessor=FeaturePreprocessor(
    feature_names=predictor.expected_features,
    scaler=predictor.scaler
)

@app.get("/")
def root():
    return {
        "message" : "Order Risk Platform API"
    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

'''
The FastAPI application was successfully started using Uvicorn.
Accessing the /health endpoint returned an HTTP 200 response with the JSON object {"status": "healthy"}, confirming that the API server is running correctly.
'''

@app.post("/score")
def score_order(
    order: OrderRequest,
    _: str = Depends(verify_api_key),
):
    """
    Predict fraud risk for an order.
    """

    try:

        order_dict = order.model_dump()

        features = preprocessor.prepare(
            order_dict
        )

        prediction = predictor.score(
            features
        )

        return prediction

    except HTTPException:
        raise

    except Exception:

        logger.exception(
            "Unexpected error while scoring order."
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        )