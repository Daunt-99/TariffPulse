from fastapi import APIRouter

from app.api.v1.routes import alerts, events, health, predictions, reactions, sectors

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(sectors.router, prefix="/sectors", tags=["sectors"])
api_router.include_router(reactions.router, prefix="/reactions", tags=["reactions"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["alerts"])

