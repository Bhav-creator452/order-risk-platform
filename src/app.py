from fastapi import FastAPI

app = FastAPI()

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
