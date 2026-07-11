from datetime import date

from pydantic import BaseModel
from pydantic import Field

from src.enums import (
    PaymentMethod,
    ProductCategory,
    DeviceUsed,
)

class OrderRequest(BaseModel):
    transaction_amount: float = Field(
        ...,
        gt=0,
        description="Total transaction amount.",
        example=1499.99,
    )

    quantity: int = Field(
        ...,
        ge=1,
        description="Number of items purchased.",
        example=2,
    )

    customer_age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age of the customer.",
        example=28,
    )

    account_age_days: int = Field(
        ...,
        ge=0,
        description="Customer account age in days.",
        example=365,
    )

    transaction_hour: int = Field(
        ...,
        ge=0,
        le=23,
        description="Hour of transaction (24-hour format).",
        example=14,
    )

    transaction_date: date = Field(
        ...,
        description="Transaction date.",
        example="2025-06-20",
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
        description="Shipping address.",
        example="Delhi",
    )

    billing_address: str = Field(
        ...,
        description="Billing address.",
        example="Delhi",
    )

class ScoreResponse(BaseModel):
    """
    Response returned after fraud prediction.
    """

    prediction: int = Field(
        ...,
        description="Predicted fraud class. 0 = Legitimate, 1 = Fraud.",
        example=0,
    )

    label: str = Field(
        ...,
        description="Human-readable prediction label.",
        example="Legitimate",
    )

    fraud_probability: float = Field(
        ...,
        ge=0,
        le=1,
        description="Probability that the order is fraudulent.",
        example=0.0842,
    )