from flask import Flask
from flask_restplus import Api


app = Flask(__name__)
api = Api(app)

from . import views
from .views import api as ns

api.add_namespace(ns)
