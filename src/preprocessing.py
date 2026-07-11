"""
preprocessing.py

Transforms an incoming order into the exact feature format
expected by the trained Random Forest model.
"""

from __future__ import annotations
from typing import Any

import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeaturePreprocessor:
    """
    Converts API request data into model-ready features.
    """

    def __init__(self, feature_names: list[str], scaler: StandardScaler):
        self.feature_names = feature_names
        self.scaler=scaler

    def _rename_columns(
    self,
    df: pd.DataFrame,
    ) -> pd.DataFrame:

        column_mapping = {
            "transaction_amount": "Transaction Amount",
            "quantity": "Quantity",
            "customer_age": "Customer Age",
            "account_age_days": "Account Age Days",
            "transaction_hour": "Transaction Hour",
            "transaction_date": "Transaction Date",
            "payment_method": "Payment Method",
            "product_category": "Product Category",
            "device_used": "Device Used",
            "shipping_address": "Shipping Address",
            "billing_address": "Billing Address"
    }

        return df.rename(columns=column_mapping)

    def prepare(self, order: dict[str,Any]) -> pd.DataFrame:
        """
        Complete preprocessing pipeline.
        """

        df = pd.DataFrame([order])

        df = self._rename_columns(df)

        df = self._create_date_features(df)

        df = self._create_address_match(df)

        df = self._create_account_age_group(df)

        df = self._drop_unused_columns(df)

        df = self._one_hot_encode(df)

        df = self._align_columns(df)

        df = self._scale_numeric_features(df)

        return df

    # -------------------------------------------------------
    # Feature Engineering
    # -------------------------------------------------------

    def _create_date_features(
    self,
    df: pd.DataFrame,
    ) -> pd.DataFrame:

        df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

        df["Transaction Month"] = df["Transaction Date"].dt.month
        df["Transaction Day"] = df["Transaction Date"].dt.day
        df["Transaction Weekday"] = df["Transaction Date"].dt.dayofweek

        df["Is Weekend"] = (
            df["Transaction Weekday"] >= 5
        ).astype(int)

        return df

    def _create_address_match(self, df: pd.DataFrame) -> pd.DataFrame:

        df["Address Match"] = (
            df["Shipping Address"]
            ==
            df["Billing Address"]
        ).astype(int)

        return df

    def _create_account_age_group(self, df: pd.DataFrame) -> pd.DataFrame:

        df["Account Age Group"] = pd.cut(
            df["Account Age Days"],
            bins=[0, 30, 90, 180, float("inf")],
            labels=[
                "0-30",
                "31-90",
                "91-180",
                "181+"
            ]
        )

        return df

    # -------------------------------------------------------
    # Encoding
    # -------------------------------------------------------

    def _one_hot_encode(self, df: pd.DataFrame) -> pd.DataFrame:


        categorical_columns = [
        "Payment Method",
        "Product Category",
        "Device Used",
        "Account Age Group"
]

        df = pd.get_dummies(
            df,
            columns=categorical_columns,
            drop_first=False
        )

        return df

    # -------------------------------------------------------
    # Cleanup
    # -------------------------------------------------------

    def _drop_unused_columns(self, df: pd.DataFrame) -> pd.DataFrame:

        columns_to_drop = [
            "Transaction Date",
            "Shipping Address",
            "Billing Address"
        ]

        return df.drop(columns=columns_to_drop)

    # -------------------------------------------------------
    # Column Alignment
    # -------------------------------------------------------

    def _align_columns(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.reindex(
            columns=self.feature_names,
            fill_value=0
        )
        
        return df
    
    def _scale_numeric_features(self, df):

        numeric_columns = [
            "Transaction Amount",
            "Customer Age",
            "Quantity",
            "Account Age Days",
            "Transaction Hour",
            "Transaction Month",
            "Transaction Day",
            "Transaction Weekday"
    ]

        df[numeric_columns] = self.scaler.transform(
            df[numeric_columns]
    )

        return df

