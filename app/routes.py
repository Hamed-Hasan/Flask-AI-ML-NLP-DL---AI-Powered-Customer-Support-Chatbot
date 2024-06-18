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
