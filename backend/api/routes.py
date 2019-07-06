from flask import Blueprint, request, session,g
from flask_restplus import reqparse, abort, Api, Resource
from api.user.user import UsersWebAPI
from api.registration.registration import RegistrationWebAPI
from api.locations import LocationsWebAPI
from api.login import LoginWebAPI
from api.game import GameWebAPI
blueprint = Blueprint('', __name__, url_prefix='/api')
api = Api(blueprint)

endpoints = [
    (['/users/<int:userid>'], UsersWebAPI),
    (['/registration'], RegistrationWebAPI),
    (['/locations'], LocationsWebAPI),
    (['/login'], LoginWebAPI),
    (['/games'], GameWebAPI),
]

for endpoint in endpoints:
    api.add_resource(endpoint[1], *endpoint[0])
