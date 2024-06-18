<<<<<<< HEAD
from flask_restx import Api, Resource, fields
from flask import request
from . import db
from .models import Item
from .auth import api as auth_ns

api = Api(
    title='Flask RESTX API',
    version='1.0',
    description='A simple demonstration of a Flask RESTX powered API'
)

ns = api.namespace('items', description='Items operations')

item_model = api.model('Item', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an item'),
    'name': fields.String(required=True, description='Item name')
})

@ns.route('/')
class ItemList(Resource):
    @ns.doc('list_items')
    @ns.marshal_list_with(item_model)
    def get(self):
        """List all items"""
        return Item.query.all()

    @ns.doc('create_item')
    @ns.expect(item_model)
    @ns.marshal_with(item_model, code=201)
    def post(self):
        """Create a new item"""
        data = request.json
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return new_item, 201

def init_app(app):
    api.add_namespace(auth_ns, path='/auth')
    api.init_app(app)
=======
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
>>>>>>> 65f65d5aac8b718ecc742a7c84190a91069b75f5
