# Tariff Shock Intelligence System

Tariff Shock Intelligence System is a research and analytics platform for detecting tariff and trade-policy shocks, extracting structured event intelligence, mapping affected sectors, measuring market reaction timing, and predicting whether sector-level reactions are immediate or delayed.

This repository is organized as a full-stack monorepo with:

- `apps/api`: FastAPI backend and API contracts
- `apps/web`: Next.js dashboard for analytics and alerting
- `services/ingestion`: source connectors and ingestion jobs
- `services/nlp`: tariff event extraction and normalization pipelines
- `services/reaction-engine`: event studies and lag classification logic
- `services/ml`: feature engineering, baseline models, inference, similarity
- `packages/shared`: shared TypeScript contracts/constants
- `infra`: Docker, compose, deployment notes
- `scripts`: bootstrap and mock-seed scripts
- `docs`: architecture and implementation plans

## Quick Start

1. Copy `.env.example` to `.env`.
2. Start infrastructure with `docker compose up -d postgres redis`.
3. Install API dependencies and run the backend:

```bash
cd apps/api
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

4. Install frontend dependencies and run the web app:

```bash
npm install
npm run dev:web
```

The scaffold ships with fake event fixtures so the API and dashboard can render before live data sources are connected.

## Monorepo Commands

- `npm run dev:web` - run the Next.js dashboard
- `npm run lint:web` - lint the frontend workspace
- `npm run typecheck:web` - type-check the frontend workspace
- `make api` - run FastAPI locally
- `make seed` - generate sample tariff events
- `make test-api` - run backend tests

## Local URLs

- API docs: `http://localhost:8000/docs`
- Web app: `http://localhost:3000`

## Current Scope

This repo intentionally provides a polished foundation instead of a fully finished system. Most modules include:

- typed interfaces
- realistic placeholder abstractions
- TODO markers for implementation depth
- mock data for development
- clear extension points for teams

See [docs/architecture.md](docs/architecture.md) for the system flow and [docs/roadmap.md](docs/roadmap.md) for implementation priorities.
