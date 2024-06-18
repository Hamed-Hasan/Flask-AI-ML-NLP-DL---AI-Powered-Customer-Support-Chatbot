from flask import Flask
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

    return app
