from enum import Enum


class PaymentMethod(str, Enum):
    BANK_TRANSFER = "bank transfer"
    CREDIT_CARD = "credit card"
    DEBIT_CARD = "debit card"


class ProductCategory(str, Enum):
    ELECTRONICS = "electronics"
    HEALTH_BEAUTY = "health & beauty"
    HOME_GARDEN = "home & garden"
    TOYS_GAMES = "toys & games"


class DeviceUsed(str, Enum):
    MOBILE = "mobile"
    TABLET = "tablet"