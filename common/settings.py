from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    key: str
    digestmod: str = "sha256"
    expire_seconds: int = 60


@lru_cache()
def get_settings():
    return Settings()

env = get_settings()
