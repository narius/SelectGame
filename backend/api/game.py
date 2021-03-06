from flask_restplus import Resource, abort
from flask import request, session, jsonify
from db import get_db
import json
import hashlib
from api.decorators import login_required


class GameWebAPI(Resource):
    # all = True means that we take all locations, if false only the ones owned by user
    @login_required
    def get(self,id, **kwargs):
        userid = userid = kwargs['userid']
        [conn, cursor] = get_db()
        game_sql = """SELECT game.id, game.name, (SELECT COUNT(id) FROM game_library WHERE game_library.game_id={0} and game_library.user_id={1}) FROM game WHERE id={0}""".format(int(id),int(userid))
        cursor.execute(game_sql)
        game = cursor.fetchone()
        my_rating_sql = """SELECT * FROM game_rating WHERE user_id={0} AND game_id={1}""".format(int(userid),int(id))
        cursor.execute(my_rating_sql)
        my_rating = cursor.fetchone()

        result = {
            'game': game,
            'my_rating':my_rating
        }
        return jsonify(result)

    @login_required
    def put(self,id,**kwargs):
        userid = userid = kwargs['userid']
        data = json.loads(request.data)
        [conn, cursor] = get_db()
        rating = data['rate']
        sql = """
        INSERT INTO game_rating(user_id,game_id, rating) VALUES({0},{1},{2})\
        ON CONFLICT (user_id,game_id) DO UPDATE SET rating={2}"""
        sql = sql.format(userid,id,rating)
        cursor.execute(sql);
        conn.commit()
        return
