# backend/core/config.py
# from core.config import settings
from functools import lru_cache

class Settings():
    app_name: str = "DS API"
    api_key: str
    debug: bool = True

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()