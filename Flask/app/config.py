import os

PG_USER = os.getenv("PG_USER", default="ads")
PG_PASSWORD = os.getenv("PG_PASSWORD", default="12345")
PG_HOST = os.getenv("PG_HOST", default="127.0.0.1")
PG_PORT = int(os.getenv("PG_PORT", default=5431))
PG_DB = os.getenv("PG_DB", default="ads")

PG_DSN = os.getenv("PG_DSN", f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")
TOKEN_TTL = int(os.getenv("TOKEN_TTL", 86400))
PASSWORD_LENGTH = int(os.getenv("PASSWORD_LENGTH", 12))