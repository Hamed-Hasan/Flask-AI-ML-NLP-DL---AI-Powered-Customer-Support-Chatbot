from flask import Blueprint, request, jsonify, make_response
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required
from .models import User, db

auth_bp = Blueprint('auth', __name__)
api = Namespace('auth', description='Authentication operations')

signup_model = api.model('Signup', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The password')
})

login_model = api.model('Login', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The password')
})

@api.route('/signup')
class Signup(Resource):
    @api.expect(signup_model)
    def post(self):
        """Signup a new user"""
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if User.query.filter_by(username=username).first():
            return make_response(jsonify({"msg": "User already exists"}), 400)

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify({"msg": "User created successfully"}), 201)

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Login an existing user"""
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return make_response(jsonify({"msg": "Bad username or password"}), 401)

        access_token = create_access_token(identity=username)
        return make_response(jsonify(access_token=access_token), 200)

@api.route('/protected')
class Protected(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint"""
        return make_response(jsonify({"msg": "This is a protected route"}), 200)
