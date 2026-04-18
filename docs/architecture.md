# Architecture

## System Flow

1. **Data sources**
   - market data from yfinance and Alpha Vantage
   - macro/trade data from FRED
   - news from NewsAPI and GDELT
   - official policy releases from USTR and WTO
2. **Ingestion**
   - scheduled jobs fetch raw documents, market series, and metadata
   - normalized records are stored for downstream processing
3. **NLP**
   - rule-based and NER passes identify countries, tariff rates, products, and dates
   - LLM refinement converts candidates into structured tariff events
   - sector mapping and severity scoring attach downstream intelligence
4. **Storage**
   - PostgreSQL stores events, reactions, predictions, and subscriptions
   - Redis caches hot API reads and job coordination state
   - pgvector or Pinecone stores embeddings for event similarity search
5. **Reaction Engine**
   - computes event windows, abnormal returns, CAR, and spike features
   - labels sector responses as immediate, lagged, mixed, or neutral
6. **ML Layer**
   - baseline gradient boosting predicts reaction speed and magnitude
   - Temporal Fusion Transformer becomes the primary sequential model
   - similarity retrieval surfaces comparable historical shocks
7. **API**
   - FastAPI exposes typed endpoints for dashboard, alerts, and predictions
8. **Frontend**
   - Next.js dashboard renders event timeline, heatmaps, shock profiles, and alerts

## Design Principles

- clean separation between ingestion, extraction, analytics, and serving
- storage abstractions that can evolve without breaking API contracts
- mock-first development so the product can be demoed before live integrations
- typed schemas shared across frontend and backend naming conventions
