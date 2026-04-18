export const SECTORS = [
  "Industrials",
  "Materials",
  "Energy",
  "Consumer Discretionary",
  "Consumer Staples",
  "Information Technology",
  "Financials",
  "Health Care",
  "Utilities",
  "Communication Services",
  "Real Estate",
] as const;

export const EVENT_CATEGORIES = [
  "tariff_increase",
  "tariff_reduction",
  "trade_negotiation",
  "retaliatory_measure",
  "export_control",
  "customs_enforcement",
] as const;

export const LAG_LABELS = ["immediate", "lagged", "mixed", "neutral"] as const;

export const API_ROUTES = {
  health: "/api/v1/health",
  events: "/api/v1/events",
  sectors: "/api/v1/sectors",
  reactions: "/api/v1/reactions",
  predictions: "/api/v1/predictions",
  alerts: "/api/v1/alerts",
} as const;

