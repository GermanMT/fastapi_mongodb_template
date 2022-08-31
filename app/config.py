from pydantic import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):

    DATABASE_URL: str | None = None

    class Config:
        env_file = '.env'

@lru_cache()
def get_settings():
    return Settings()


settings: Settings = get_settings()