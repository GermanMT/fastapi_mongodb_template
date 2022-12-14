from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str | None = None

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()