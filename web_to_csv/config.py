"""Configurations for the app."""

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path().parent.resolve()
APP_DIR = ROOT_DIR / "web_to_csv"

# Environmental variables
DOTENV_PATH = APP_DIR / ".env"
load_dotenv(DOTENV_PATH)

# Development config
FLASK_ENV = "development"
DEBUG = True  # TODO: WARNING! Must be False in production!
SECRET_KEY = os.environ.get("SECRET_KEY")

# Development database
DATABASE_FILE = "db.sqlite3"
SCHEMA_FILE = "schema.sql"

DB_DIR = APP_DIR / "database"
DATABASE_PATH = DB_DIR / DATABASE_FILE
SCHEMA_PATH = DB_DIR / SCHEMA_FILE
