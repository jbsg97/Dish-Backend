from fastapi import APIRouter

from app.api.api_v1.endpoints import clients

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/client", tags=["Clients"])
