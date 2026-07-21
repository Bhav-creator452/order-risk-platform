from datetime import date

from pydantic import BaseModel
from pydantic import Field
from datetime import datetime

from core.enums import (
    PaymentMethod,
    ProductCategory,
    DeviceUsed,
)

class OrderRequest(BaseModel):
    transaction_amount: float = Field(
        ...,
        ge=0,
        description="Total transaction amount.",
        json_schema_extra={
        "example": 1499.99
    },
)

    quantity: int = Field(
        ...,
        ge=1,
        description="Number of items purchased.",
        json_schema_extra={
        "example": 2
    },
    )

    customer_age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age of the customer.",
        json_schema_extra={
        "example": 28
    },
    )

    account_age_days: int = Field(
        ...,
        ge=0,
        description="Customer account age in days.",
        json_schema_extra={
        "example": 365
    },
    )

    transaction_hour: int = Field(
        ...,
        ge=0,
        le=23,
        description="Hour of transaction (24-hour format).",
        json_schema_extra={
        "example": 14
    },
    )

    transaction_date: datetime = Field(
    ...,
        json_schema_extra={
        "example": "2025-06-20 15:20:04"
    },
)

    payment_method: PaymentMethod = Field(
        ...,
        description="Payment method used for the transaction."
    )

    product_category: ProductCategory = Field(
        ...,
        description="Category of the purchased product."
    )

    device_used: DeviceUsed = Field(
        ...,
        description="Device used to place the order."
    )

    shipping_address: str = Field(
        ...,
        description="Shipping Address",
        json_schema_extra={
        "example": "Delhi"
    },
)

    billing_address: str = Field(
        ...,
        description="Billing address.",
        json_schema_extra={
        "example": "Delhi"
    },
    )

class ScoreResponse(BaseModel):
    """
    Response returned after fraud prediction.
    """

    prediction: int = Field(
        ...,
        description="Predicted fraud class. 0 = Legitimate, 1 = Fraud.",
        json_schema_extra={
        "example": 0
    },
    )

    label: str = Field(
        ...,
        description="Human-readable prediction label.",
        json_schema_extra={
        "example": "Legitimate"
    },
    )

    fraud_probability: float = Field(
        ...,
        ge=0,
        le=1,
        description="Probability that the order is fraudulent.",
        json_schema_extra={
        "example": 0.0842
    },
    )

class BatchScoreRequest(BaseModel):
    """
    Request body for batch fraud scoring.
    """

    orders: list[OrderRequest]


class BatchScoreResponse(BaseModel):
    """
    Response body for batch fraud scoring.
    """

    results: list[ScoreResponse]