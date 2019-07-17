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
            participants_sql  = """SELECT users.id, users.surname, users.firstname, 'event.status.accepted' status FROM event
INNER JOIN users ON users.id=event.owner
WHERE event.id={0}
UNION
SELECT users.id, users.surname, users.firstname, event_participant.status FROM event_participant
INNER JOIN users ON users.id=event_participant.user_id 
WHERE event_participant.event_id={0} AND event_participant.status='event.status.accepted';""".format(event_id)
            cursor.execute(participants_sql)
            participants = cursor.fetchall()
            users_ids = []
            for p in participants:
                users_ids.append(int(p['id']))
            length_user_id = len(users_ids)
            t = tuple(users_ids)
            user_tuple = t if length_user_id > 1 else str(t).replace(',','')
            games_sql = """SELECT * FROM game_library 
            INNER JOIN game ON game.id=game_library.game_id
            WHERE user_id in {}""".format(user_tuple)
            cursor.execute(games_sql)
            games = cursor.fetchall()
            sent_sql = """SELECT users.id, users.surname, users.firstname, event_participant.status FROM event_participant
INNER JOIN users ON users.id=event_participant.user_id 
WHERE event_participant.event_id={0} AND event_participant.status='event.status.sent';""".format(event_id)
            cursor.execute(sent_sql)
            sent = cursor.fetchall()

            rejected_sql = """SELECT users.id, users.surname, users.firstname, event_participant.status FROM event_participant
INNER JOIN users ON users.id=event_participant.user_id 
WHERE event_participant.event_id={0} AND event_participant.status='event.status.rejected';""".format(event_id)
            cursor.execute(rejected_sql)
            rejected = cursor.fetchall()

            location_sql = """SELECT * FROM locations WHERE id={}""".format(int(event['location']))
            cursor.execute(location_sql)
            location = cursor.fetchone()

            rating_sql = """SELECT game.name, game_rating.rating, users.firstname, users.surname FROM game_rating 
            INNER JOIN game ON game.id=game_rating.game_id
            INNER JOIN users ON users.id=game_rating.user_id
            WHERE game_rating.user_id in {}
            ORDER BY game.name""".format(user_tuple)
            cursor.execute(rating_sql)
            rating = cursor.fetchall()

            my_status_sql = """SELECT * FROM event_participant WHERE user_id={0} AND event_id={1}""".format(userid,event_id)
            cursor.execute(my_status_sql)
            my_status = cursor.fetchone()
            result = {'event': event,
                      'participants': participants,
                      'sent': sent,
                      'rejected': rejected,
                      'games': games,
                      'location': location,
                      'ratings': rating,
                      'my_status': my_status
                      }
            return jsonify(result)
        cursor.execute(event_sql)
        result = cursor.fetchall()
        return jsonify(result)
