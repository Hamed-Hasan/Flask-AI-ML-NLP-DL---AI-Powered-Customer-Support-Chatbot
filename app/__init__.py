from flask import Flask
from .config import DevelopmentConfig
from .extensions import db, migrate
from .routes import api_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)

    return app
