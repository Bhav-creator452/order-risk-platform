import time

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request

from src.auth import verify_api_key

from src.schemas import (
    OrderRequest,
    ScoreResponse,
) 
from src.logger import logger

from src.predictor import FraudPredictor
from src.preprocessing import FeaturePreprocessor

app = FastAPI(
    title = "Order Risk Platform API",
    description = """

## Overview

The Order Risk Platform API predicts the fraud risk of an e-commerce order
using a trained Random Forest machine learning model.

### Features

- Fraud prediction using a trained ML model
- Automatic request validation with Pydantic
- Feature engineering before inference
- API Key authentication
- Structured request logging
- Interactive Swagger UI documentation

### Authentication

All requests to the `/score` endpoint require a valid `X-API-Key` header.
""",
    version = "1.0.0",
    contact = {
        "name": "Bhavdeep Kaur",
        "email": "bhavyakaur10@gmail.com",
    },
    
)

predictor = FraudPredictor()

preprocessor = FeaturePreprocessor(
    feature_names=predictor.expected_features,
    scaler=predictor.scaler
)

@app.get(
    "/",
    tags = ["General"],
    summary = "API information",
    description = "Returns basic information about the service."
)
def root() -> dict[str,str]:
    return {"service": "Order Risk Platform API", "version": app.version}

@app.get(
    "/health",
    tags = ["General"],
    summary = "Health check",
    description = "Returns the service health status."
)
def health() -> dict[str,str]:
    """
    Health check endpoint.

    Returns:
        dict: Service status.
    """
    return {"status": "healthy"}


@app.post(
    "/score",
    tags = ["Fraud Detection"],
    summary = "Predict Fraud Risk",
    response_model = ScoreResponse,
    responses = {
        200: {
            "description": "Prediction generated successfully."
        },
        401: {
            "description": "Missing or invalid API key."
        },
        422: {
            "description": "Validation error."
        },
        500: {
            "description": "Unexpected server error."
        },
    },
)
def score_order(
    order: OrderRequest,
    _: str = Depends(verify_api_key),
) -> ScoreResponse:
    """
    Predict fraud risk for an incoming order.

    The request is authenticated using an API key,
    validated with Pydantic,
    preprocessed into model features,
    and scored using the trained Random Forest model.

    Returns:
        ScoreResponse
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

@app.middleware("http")
async def log_requests(request: Request, call_next):

    start = time.perf_counter()

    response = await call_next(request)

    elapsed = time.perf_counter() - start

    logger.info(
        "%s %s | Status=%d | Duration=%.3fs",
        request.method,
        request.url.path,
        response.status_code,
        elapsed,
    )

    return response