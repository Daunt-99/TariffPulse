from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = Field(default="Tariff Shock Intelligence System")
    environment: str = Field(default="development")
    app_version: str = Field(default="0.1.0")
    api_v1_prefix: str = Field(default="/api/v1")
    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/tariff_shock"
    )
    redis_url: str = Field(default="redis://localhost:6379/0")
    vector_store_provider: str = Field(default="pgvector")
    pinecone_api_key: str | None = None
    pinecone_index: str | None = None
    mock_data_path: str = Field(default="data/mock/events.json")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> "Settings":
    return Settings()


settings = get_settings()

