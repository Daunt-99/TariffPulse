# Deployment Notes

This scaffold targets local development first and leaves room for containerized deployment later.

## Likely production shape

- `apps/api` deployed as a containerized FastAPI service
- `apps/web` deployed as a Next.js application
- `services/*` run as scheduled workers or queue consumers
- PostgreSQL with `pgvector` enabled
- Redis for cache and async coordination
- Optional Pinecone when vector retrieval needs externalization

## Future deployment tasks

- add Alembic migrations
- choose cloud scheduler or orchestrator
- externalize secrets into a secret manager
- add CI/CD for lint, tests, and image builds
