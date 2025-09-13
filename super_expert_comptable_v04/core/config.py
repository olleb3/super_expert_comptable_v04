from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    NEO4J_URI: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str
    QDRANT_URL: str
    QDRANT_API_KEY: str | None = None
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()
