<<<<<<< HEAD
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
=======
from .extensions import db
>>>>>>> 65f65d5aac8b718ecc742a7c84190a91069b75f5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
<<<<<<< HEAD
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
=======
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
>>>>>>> 65f65d5aac8b718ecc742a7c84190a91069b75f5
