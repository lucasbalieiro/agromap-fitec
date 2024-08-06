from functools import lru_cache

from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    DATABASE_URL: str

    model_config = {
        "case_sensitive": True,
        "env_file": ".env",
    }


@lru_cache()
def get_settings() -> Environment:
    return Environment()
