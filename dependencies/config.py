import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class DefaultConfig(BaseSettings):
    postgresql_endpoint: str = os.getenv("POSTGRESQL_ENDPOINT", "svc.sel4.cloudtype.app")
    postgresql_port: int = os.getenv("POSTGRESQL_PORT", "30461")
    postgresql_table: str = os.getenv("POSTGRESQL_TABLE", "pgv")
    postgresql_user: str = os.getenv("POSTGRESQL_USER", "root")
    postgresql_password: str = os.getenv("POSTGRESQL_PASSWORD", "1234")
    movie_api_key: str = os.getenv("MOVIE_API_KEY", "0878b3e586d2b43cabce61aec20da98a")
    img_api_key:str = os.getenv("IMG_API_KEY", "3fe4aa745646d87e505640e8e7baa642")
    jwt_secret_key: str = os.getenv(
        "JWT_SECRET_KEY",
        "5c2fea6305c8c209714e73b265958703e65c4b40dec4c388dddac06f3f791ec7",
    )
    jwt_expire_minutes: int = os.getenv("JWT_TOKEN_EXPIRE_MINUTES", 600)


@lru_cache
def get_config():
    return DefaultConfig()
