import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = "fjskdfjsdlfksjdfkj"
    FLASK_ADMIN_SWATCH = "cerulean"