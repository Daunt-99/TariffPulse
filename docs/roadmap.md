# Roadmap

## Phase 1

- wire live ingestion clients with retries and persistence
- implement SQLAlchemy repositories and Alembic migrations
- replace mock API responses with database-backed services
- add frontend filtering, detail drawers, and search

## Phase 2

- productionize the NLP extraction pipeline with evaluation sets
- implement event similarity via pgvector
- add alert delivery workers and Redis-backed scheduling
- build sector exposure calibration logic

## Phase 3

- deliver XGBoost baseline with backtesting
- implement TFT training and inference orchestration
- add model evaluation dashboards and monitoring
- support user-defined watchlists and scenario analysis
