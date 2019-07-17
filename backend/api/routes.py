from flask import Blueprint, request, session,g
from flask_restplus import reqparse, abort, Api, Resource
from api.user.user import UsersWebAPI
from api.registration.registration import RegistrationWebAPI
from api.locations import LocationsWebAPI
from api.login import LoginWebAPI
from api.event import EventWebAPI
from api.event_invite import EventInviteWebAPI
from api.game import GameWebAPI
from api.games import GamesWebAPI
from api.game_library import GameLibraryWebAPI
from api.news import NewsWebAPI
blueprint = Blueprint('', __name__, url_prefix='/api')
api = Api(blueprint)

endpoints = [
    (['/users/<int:userid>'], UsersWebAPI),
    (['/registration'], RegistrationWebAPI),
    (['/locations'], LocationsWebAPI),
    (['/login'], LoginWebAPI),
    (['/games'], GamesWebAPI),
    (['/game/<int:id>'], GameWebAPI),
    (['/game/rate/<int:id>'], GameWebAPI),
    (['/library'], GameLibraryWebAPI),
    (['/library/<int:game_id>'], GameLibraryWebAPI),
    (['/event'], EventWebAPI),
    (['/event/invite'], EventInviteWebAPI),
    (['/event/<int:event_id>'], EventWebAPI),
    (['/news'], NewsWebAPI),
]

for endpoint in endpoints:
    api.add_resource(endpoint[1], *endpoint[0])
