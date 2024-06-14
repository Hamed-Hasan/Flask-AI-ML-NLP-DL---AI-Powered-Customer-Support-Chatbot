from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from .models import User
from .extensions import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'username': user.username, 'email': user.email}

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data['username']
        user.email = data['email']
        db.session.commit()
        return {'message': 'User updated'}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created'}, 201

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserListResource, '/users')
