from flask import Flask
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'  

    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)

    from .routes import init_app
    init_app(app)

    with app.app_context():
        db.create_all()
=======
from .config import DevelopmentConfig
from .extensions import db, migrate
from .routes import api_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)
>>>>>>> 65f65d5aac8b718ecc742a7c84190a91069b75f5

    return app
