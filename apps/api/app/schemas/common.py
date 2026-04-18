from enum import Enum


class SectorEnum(str, Enum):
    INDUSTRIALS = "Industrials"
    MATERIALS = "Materials"
    ENERGY = "Energy"
    CONSUMER_DISCRETIONARY = "Consumer Discretionary"
    CONSUMER_STAPLES = "Consumer Staples"
    INFORMATION_TECHNOLOGY = "Information Technology"
    FINANCIALS = "Financials"
    HEALTH_CARE = "Health Care"
    UTILITIES = "Utilities"
    COMMUNICATION_SERVICES = "Communication Services"
    REAL_ESTATE = "Real Estate"


class EventCategoryEnum(str, Enum):
    TARIFF_INCREASE = "tariff_increase"
    TARIFF_REDUCTION = "tariff_reduction"
    TRADE_NEGOTIATION = "trade_negotiation"
    RETALIATORY_MEASURE = "retaliatory_measure"
    EXPORT_CONTROL = "export_control"
    CUSTOMS_ENFORCEMENT = "customs_enforcement"


class LagLabelEnum(str, Enum):
    IMMEDIATE = "immediate"
    LAGGED = "lagged"
    MIXED = "mixed"
    NEUTRAL = "neutral"

