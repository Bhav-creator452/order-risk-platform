from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OrderRequest(BaseModel):
    transaction_amount: float
    transaction_hour: int
    customer_age: int
    account_age_days: int
    quantity: int
    transaction_day: int
    transaction_month: int
    transaction_weekday: int


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
def score_order(order: OrderRequest):
    return {
        "score": 0.50, #Static score for review
        "label": "review",
        "received": order.model_dump()
    }
