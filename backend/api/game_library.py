from flask_restplus import Resource, abort
from flask import request, session, jsonify
from db import get_db
import json
import hashlib
from api.decorators import login_required


class GameLibraryWebAPI(Resource):
    # all = True means that we take all locations, if false only the ones owned by user
    # TODO: change SQL to pick from game_library table
    @login_required
    def get(self, **kwargs):
        user_id =  kwargs['userid']
        [conn, cursor] = get_db()
        game_sql = """
        SELECT game.id,game.name, game_rating.rating FROM game_library
INNER JOIN game ON game_library.game_id=game.id
JOIN game_rating ON game_rating.game_id=game_library.game_id AND game_rating.user_id=game_library.user_id
WHERE game_library.user_id={};
""".format(int(user_id))
        cursor.execute(game_sql)
        result = cursor.fetchall()
        return jsonify(result)

    # TODO: Write post and delete function function

    @login_required
    def post(self,**kwargs):
        data = json.loads(request.data)
        game_id = data['game_id']
        user_id = kwargs['userid']
        library_sql = """INSERT INTO game_library(user_id, game_id) VALUES ({0},{1})"""
        library_sql = library_sql.format(int(user_id), int(game_id))
        [conn, cursor] = get_db()
        cursor.execute(library_sql)
        conn.commit()
        return {},201

    @login_required
    def delete(self,game_id,**kwargs):
        user_id = kwargs['userid']
        [conn, cursor] = get_db()
        sql = """DELETE FROM game_library WHERE user_id={0} and game_id={1}""".format(int(user_id), int(game_id))
        cursor.execute(sql)
        conn.commit()
        return {}, 200
