from fastapi import FastAPI
from .controllers import api
from .core.config import settings

app = FastAPI(
    title="Super Expert Comptable v04",
    description="Une API pour l'automatisation comptable propulsée par l'IA.",
    version="0.1.0",
)

app.include_router(api.api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["Root"])
async def read_root():
    return {"status": "ok", "message": "Bienvenue sur l'API Super Expert Comptable v04"}
