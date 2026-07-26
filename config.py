import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "sha256")

    # MySQL Database Configuration (Primary for Assignment Requirements)
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
    MYSQL_DB = os.environ.get("MYSQL_DB", "employee_db")

    # Safely URL-encode user and password to handle special characters like '@'
    encoded_user = quote_plus(MYSQL_USER)
    encoded_password = quote_plus(MYSQL_PASSWORD)

    # MySQL URI using PyMySQL driver
    MYSQL_DATABASE_URI = f"mysql+pymysql://{encoded_user}:{encoded_password}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

    # Database Selection Strategy:
    # 1. DATABASE_URL environment variable if set
    # 2. SQLite if USE_SQLITE=True
    # 3. MySQL URI (Default)
    if os.environ.get("USE_SQLITE", "").lower() in ("true", "1"):
        SQLALCHEMY_DATABASE_URI = "sqlite:///employee.db"
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", MYSQL_DATABASE_URI)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_NAME = "Employee Management System"
    UPLOAD_FOLDER = "uploads"
    API_KEY = "12341asdasd"
    DEBUG = True