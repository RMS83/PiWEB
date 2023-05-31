import os

PG_USER = os.getenv("PG_USER", default="user")
PG_PASSWORD = os.getenv("PG_PASSWORD", default="1234")
PG_HOST = os.getenv("PG_HOST", default="127.0.0.1")
PG_PORT = int(os.getenv("PG_PORT", default=5431))
PG_DB = os.getenv("PG_DB", default="hero")

PG_DSN = os.getenv("PG_DSN", f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")
DB_URL = os.getenv("DB_URL", "https://swapi.dev/api")