from flask_restplus import Resource, abort
from flask import request, session, jsonify
from db import get_db
import json
import hashlib
from api.decorators import login_required


class EventWebAPI(Resource):
    # all = True means that we take all locations, if false only the ones owned by user
    @login_required
    def get(self,event_id=None, **kwargs):
        userid = userid = kwargs['userid']
        [conn, cursor] = get_db()
        event_sql = "SELECT * FROM event"
        if event_id is not None:
            event_sql = event_sql+" WHERE id={}".format(int(event_id))
            cursor.execute(event_sql)
            event = cursor.fetchone()
            participants_sql  = """SELECT users.id, users.surname, users.firstname, 'ACCEPTED' status FROM event
INNER JOIN users ON users.id=event.owner
WHERE event.id=1
UNION
SELECT users.id, users.surname, users.firstname, event_participant.status FROM event_participant
INNER JOIN users ON users.id=event_participant.user_id 
WHERE event_participant.event_id=1;"""
            cursor.execute(participants_sql)
            participants = cursor.fetchall()
            users_ids = []
            for p in participants:
                users_ids.append(int(p['id']))
            games_sql = """SELECT * FROM game_library 
            INNER JOIN game ON game.id=game_library.game_id
            WHERE user_id in {}""".format(tuple(users_ids))
            cursor.execute(games_sql)
            games = cursor.fetchall()
            location_sql = """SELECT * FROM locations WHERE id={}""".format(int(event['location']))
            cursor.execute(location_sql)
            location = cursor.fetchone()

            rating_sql = """SELECT game.name, game_rating.rating, users.firstname, users.surname FROM game_rating 
            INNER JOIN game ON game.id=game_rating.game_id
            INNER JOIN users ON users.id=game_rating.user_id
            WHERE game_rating.user_id in {}
            ORDER BY game.name""".format(tuple(users_ids))
            cursor.execute(rating_sql)
            rating = cursor.fetchall()
            result = {'event': event,
                      'participants': participants,
                      'games': games,
                      'location': location,
                      'ratings': rating
                      }
            return jsonify(result)
        cursor.execute(event_sql)
        result = cursor.fetchall()
        return jsonify(result)
