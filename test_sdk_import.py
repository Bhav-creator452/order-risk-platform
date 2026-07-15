from order_risk_sdk import OrderRiskClient, SDKConfig, APIError

config = SDKConfig(
    api_key="your-api-key"
)

client = OrderRiskClient(config)

print(type(client))