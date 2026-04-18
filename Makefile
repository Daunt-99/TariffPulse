SHELL := /bin/sh

.PHONY: api web seed test-api lint-api

api:
	cd apps/api && uvicorn app.main:app --reload --port 8000

web:
	npm run dev:web

seed:
	python scripts/seed_fake_events.py

test-api:
	cd apps/api && pytest

lint-api:
	ruff check apps/api services

