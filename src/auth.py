"""
Authentication utilities.
"""

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import APIKeyHeader

from src.config import API_KEY


api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False,
)


def verify_api_key(
    api_key: str = Depends(api_key_header),
):
    """
    Validate API key from request header.
    """

    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )

    return api_key