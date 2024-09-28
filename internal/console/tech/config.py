import datetime
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from auth_provider.provider.auth import AuthConfig

load_dotenv()


class Configs(BaseSettings):
    # database
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_USER: str = os.getenv("DB_USER")
    DB_PWD: str = os.getenv("DB_PWD")

    DATABASE_URL: str = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        user=DB_USER,
        host=DB_HOST,
        password=DB_PWD,
        port=DB_PORT,
        database=DB_NAME,
    )

    REDIS_PORT: str = os.getenv("REDIS_PORT")
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_DB: str = os.getenv("REDIS_DB")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD")
    REDIS_USER_PASSWORD: str = os.getenv("REDIS_USER_PASSWORD")
    REDIS_USER: str = os.getenv("REDIS_USER")
    auth_config: AuthConfig = AuthConfig(secret=os.getenv("AUTH_SECRET"), access_token_time=datetime.timedelta(minutes=15),
                             refresh_token_time=datetime.timedelta(minutes=15))

    class Config:
        case_sensitive = True


configs = Configs()
