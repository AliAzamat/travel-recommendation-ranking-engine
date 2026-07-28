import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """All runtime config in one typed place, read from the environment."""
    database_url: str = os.environ.get("DATABASE_URL", "postgresql://localhost/travel")
    pool_min: int = int(os.environ.get("DB_POOL_MIN", "1"))
    pool_max: int = int(os.environ.get("DB_POOL_MAX", "10"))


settings = Settings()
