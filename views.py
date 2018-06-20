from . import app
from flask import render_template
from flask_restplus import Api, Namespace, Resource, fields


api = Namespace('data', description='fake browsing data')


data = api.model('Data', {
    'id': fields.String(required=True, description='user id'),
    'click': fields.Integer(required=True, description='number click in current session'),
    'url': fields.String(required=True, description='current url'),
})

DATA = [
    {'id': '1', 'click': 1, 'url': 'https://www.google.com/'},
    {'id': '1', 'click': 2, 'url': 'https://www.google.com/search?source=hp&ei=EY4qW-jNH6PI5gKopLfQDA&q=nyc+parks&oq=nyc+parks&gs_l=psy-ab.3..0i131k1j0l9.27948.29059.0.29212.11.10.0.0.0.0.91.708.9.10.0....0...1.1.64.psy-ab..1.9.708.0...59.V91ud9oAb98'},
    {'id': '1', 'click': 3, 'url': 'https://www.google.com/maps?q=nyc+parks&um=1&ie=UTF-8&sa=X&ved=0ahUKEwizubzX4eLbAhWB6oMKHeUuDcMQ_AUICigB'},
    {'id': '1', 'click': 4, 'url': 'https://www.google.com/maps/place/Greeley+Square+Park/@40.7509795,-73.9888683,15z/data=!4m8!1m2!2m1!1snyc+parks!3m4!1s0x89c259a929abe511:0x60bf9cdac8a5aa83!8m2!3d40.7487156!4d-73.9882971'},
    {'id': '1', 'click': 5, 'url': 'https://www.google.com/maps/dir//Greeley+Square+Park,+North+Broadway,+New+York,+NY+10001/@40.7509795,-73.9888683,15z/data=!4m8!4m7!1m0!1m5!1m1!1s0x89c259a929abe511:0x60bf9cdac8a5aa83!2m2!1d-73.9882971!2d40.7487156'},
    {'id': '2', 'click': 1, 'url': 'https://images.google.com/?gws_rd=ssl'},
    {'id': '2', 'click': 2, 'url': 'https://www.google.com/search?tbm=isch&source=hp&biw=1394&bih=736&ei=J48qW76kOojW5gL98oqwCA&q=golden+retriever&oq=golden&gs_l=img.3.0.0l10.531.1736.0.3168.11.8.2.1.1.0.147.557.6j1.7.0....0...1ac.1.64.img..1.10.566.0...0.PQ5cA3t8aDY'},
]

@api.route('/')
class ShowData(Resource):
    @api.doc('show_data')
    @api.marshal_list_with(data)
    def get(self):
        return DATA

@api.route('/<id>')
@api.param('id', 'User Id')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(data)
    def get(self, id):
        for user in DATA:
            if data['id'] == id:
                return user
        api.abort(404)
