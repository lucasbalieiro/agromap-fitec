from functools import lru_cache

from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str


    model_config = {
        "case_sensitive": True,
        "env_file": ".env",
    }


@lru_cache()
def get_settings() -> Environment:
    return Environment()
