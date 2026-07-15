# 🛡️ Order Risk Platform API

A production-style Machine Learning REST API that predicts the fraud risk of e-commerce transactions using a trained **Random Forest Classifier**.

The project demonstrates the complete lifecycle of an ML application—from data preprocessing and feature engineering to model training, API development, authentication, validation, and documentation using **FastAPI**.

---

## 📌 Project Overview

Traditional fraud detection systems rely on manually written business rules that are difficult to maintain and often fail to detect complex fraud patterns.

This project replaces static rule-based scoring with a Machine Learning model trained to identify potentially fraudulent transactions based on customer behavior, transaction details, and engineered features.

The API accepts an order, validates the request, performs the same preprocessing used during model training, generates a fraud prediction, and returns the prediction along with the fraud probability.

---

## ✨ Features

- Machine Learning powered fraud prediction
- Random Forest Classifier
- Feature engineering pipeline
- Automatic request validation using Pydantic
- API Key Authentication
- Environment-based configuration
- Automatic Swagger / OpenAPI documentation
- Structured logging
- Modular project architecture
- Production-style error handling

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| API Framework | FastAPI |
| Validation | Pydantic |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Model Serialization | Joblib |
| Environment Variables | python-dotenv |
| API Documentation | Swagger UI / OpenAPI |
| Server | Uvicorn |

---

# 🧠 Machine Learning Pipeline

```
Raw Request
      │
      ▼
Request Validation
(Pydantic)
      │
      ▼
Feature Engineering
      │
      ├── Rename Columns
      ├── Date Features
      ├── Address Match
      ├── Account Age Groups
      ├── One-Hot Encoding
      ├── Feature Alignment
      └── Standard Scaling
      │
      ▼
Random Forest Model
      │
      ▼
Prediction
      │
      ▼
JSON Response
```

---

# 📂 Project Structure

```
order-risk-platform/

│
├── app.py
├── README.md
├── .env.example
├── .gitignore
│
├── models/
│   ├── Random_Forest_model.joblib
│   ├── scaler.joblib
│   └── feature_names.joblib
│
├── src/
│   ├── auth.py
│   ├── config.py
│   ├── enums.py
│   ├── predictor.py
│   └── preprocessing.py
│
└── notebooks/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Bhav-creator452/order-risk-platform.git
cd order-risk-platform
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# ⚙ Environment Variables

Create a `.env` file in the project root.

Example

```text
API_KEY=your_secure_api_key

MODEL_PATH=models/Random_Forest_model.joblib

FEATURE_NAMES_PATH=models/feature_names.joblib

SCALER_PATH=models/scaler.joblib
```

---

# ▶ Running the API

```bash
uvicorn app:app --reload
```

API

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔐 Authentication

The `/score` endpoint is protected using API Key authentication.

Include the following header in every request.

```
X-API-Key: YOUR_API_KEY
```

Requests without a valid API key return

```
401 Unauthorized
```

---

# 📌 API Endpoints

## GET /

Returns basic information about the API.

Response

```json
{
  "message": "Order Risk Platform API"
}
```

---

## GET /health

Checks whether the API is running.

Response

```json
{
  "status": "healthy"
}
```

---

## POST /score

Predicts the fraud risk of an incoming order.

### Sample Request

```json
{
  "transaction_amount": 1499.99,
  "quantity": 2,
  "customer_age": 28,
  "account_age_days": 365,
  "transaction_hour": 14,
  "transaction_date": "2025-06-20",
  "payment_method": "credit card",
  "product_category": "electronics",
  "device_used": "mobile",
  "shipping_address": "Delhi",
  "billing_address": "Delhi"
}
```

### Sample Response

```json
{
  "prediction": 0,
  "label": "Legitimate",
  "fraud_probability": 0.0842
}
```

---

# ✅ Request Validation

Incoming requests are automatically validated using Pydantic.

Examples of validations include:

- Required fields
- Numeric ranges
- Enum validation
- Data types
- Date format validation

Invalid requests return

```
422 Unprocessable Entity
```

---

# 📊 Feature Engineering

Before reaching the model, each request undergoes the same preprocessing used during model training.

The preprocessing pipeline performs:

- Column renaming
- Date feature extraction
- Address matching
- Account age grouping
- One-Hot Encoding
- Feature alignment
- Standardization

This guarantees inference consistency between training and production.

---

# 🧪 Testing

The API has been manually tested for the following scenarios.

| Test | Status |
|-------|--------|
| Health endpoint | ✅ |
| Root endpoint | ✅ |
| Valid prediction | ✅ |
| Missing API Key | ✅ |
| Invalid API Key | ✅ |
| Invalid request body | ✅ |
| Missing required field | ✅ |
| Invalid enum values | ✅ |
| Internal server error handling | ✅ |

---

# 📈 Example Workflow

```
Client
   │
POST /score
   │
   ▼
API Key Authentication
   │
   ▼
Request Validation
   │
   ▼
Feature Engineering
   │
   ▼
Random Forest Prediction
   │
   ▼
JSON Response
```

---

# 🔮 Future Improvements

Possible enhancements include:

- JWT Authentication
- Batch prediction endpoint
- Docker support
- Unit and integration tests
- CI/CD pipeline
- Cloud deployment
- Model versioning
- Database integration
- Monitoring and metrics
- Rate limiting

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Machine Learning model deployment
- REST API development
- FastAPI
- Feature engineering
- Model serialization
- Request validation
- Authentication
- Error handling
- Environment configuration
- API documentation

---

## Python SDK

Install in editable mode:

```bash
pip install -e .
```

Example:

```python
from order_risk_sdk import OrderRiskClient

client = OrderRiskClient(
    api_key="YOUR_API_KEY"
)

result = client.score_order(order)

print(result)
```


# 👩‍💻 Author

**Bhavdeep Kaur**

BCA Student | Aspiring Data Scientist / Machine Learning Engineer

GitHub: https://github.com/Bhav-creator452

LinkedIn: https://linkedin.com/in/bhavdeep-kaur2006