import os

def _build_mysql_uri():
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        return database_url

    user = os.environ.get("DB_USER", "zentrio")
    password = os.environ.get("DB_PASSWORD", "zentrio")
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "3306")
    name = os.environ.get("DB_NAME", "zentrio")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}?charset=utf8mb4"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "thesecretkey")  
    SQLALCHEMY_DATABASE_URI = _build_mysql_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 280,
    }
