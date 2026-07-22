import os

class Config:

    SECRECT_KEY = "sha256"
    SECRET_KEY = "sha256"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///employee.db"
    )
    SQLALCHEMY_TRACK_MODIFICATION = False

    APP_NAME = "Employee Management System"
    UPLOAD_FOLDER = "uploads"
    API_KEY = "12341asdasd"
    DEBUG = True