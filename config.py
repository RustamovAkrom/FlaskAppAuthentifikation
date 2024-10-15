from dotenv import load_dotenv
import os

load_dotenv(".env")

class Config:

    SECRET_KEY =  "lsfajlkdjfaldkjf"
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True

    # File upload settings
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1204 # 16 MB limit
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf", "txt"}

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    WTF_CSRF_ENABLED = False
