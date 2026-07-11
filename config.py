import os
from datetime import timedelta


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

# Create instance folder if it doesn't exist
os.makedirs(INSTANCE_DIR, exist_ok=True)


class Config:
    # Secret Key
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "taskflow-dev-secret-change-me"
    )

    # Database Configuration
    DATABASE_URL = os.environ.get("DATABASE_URL")

    if DATABASE_URL:
        # Render PostgreSQL compatibility
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = DATABASE_URL or (
        "sqlite:///" + os.path.join(INSTANCE_DIR, "database.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session Configuration
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
