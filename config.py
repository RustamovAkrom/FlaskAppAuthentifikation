from dotenv import load_dotenv
import os


base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv(".env")

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
    