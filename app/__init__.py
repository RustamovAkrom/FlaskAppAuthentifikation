from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from config import Config


db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
migrate = Migrate()


def create_app(config_class = Config):
    app = Flask(__name__)

    # Configure settings
    app.config.from_object(config_class)

    # initializing database
    db.init_app(app)

    # initializing csrf 
    csrf.init_app(app)

    # initializing login manager
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # initializing migrations
    migrate.init_app(app, db)
     
    from app import routers

    # registration routers
    app.register_blueprint(routers.dp)

    return app