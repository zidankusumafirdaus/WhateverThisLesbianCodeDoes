import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

def _parse_cors_origins(value):
    if not value:
        return ["http://localhost:5173"]
    if value.strip() == "*":
        return "*"
    return [origin.strip() for origin in value.split(",") if origin.strip()]

class Config:
    # Flask / JWT
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES")))

    # database
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
    CORS_ORIGINS = _parse_cors_origins(os.getenv("CORS_ORIGINS"))
