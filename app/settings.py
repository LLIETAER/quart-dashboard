# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Application information
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
OWNER = os.getenv("OWNER", "Mike Ryan")
WEBSITE = os.getenv("WEBSITE", "https://devsetgo.com")
LICENSE_TYPE = os.getenv("LICENSE_TYPE", "MIT")
LICENSE_LINK = os.getenv(
    "LICENSE_LINK", "https://github.com/devsetgo/starlette-SRTDashboard"
)

# Demo Data
CREATE_SAMPLE_DATA = os.getenv("CREATE_SAMPLE_DATA", True)


# Application Configurations
HOST_DOMAIN = os.getenv("HOST_DOMAIN", "https://devsetgo.com")
RELEASE_ENV = os.getenv("RELEASE_ENV", "prd")
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI", "sqlite:///sqlite_db/api.db"
)

# Loguru settings
LOGURU_RETENTION = os.getenv("LOGURU_RETENTION", "10 days")
LOGURU_ROTATION = os.getenv("LOGURU_ROTATION", "10 MB")

# Access Token Settings
SECRET_KEY = os.getenv("SECRET_KEY", "secret-key-1234567890")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 10080)
