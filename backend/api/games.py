from flask_restplus import Resource, abort
from flask import request, session, jsonify
from db import get_db
import json
import hashlib
from api.decorators import login_required


class GamesWebAPI(Resource):
    # all = True means that we take all locations, if false only the ones owned by user
    @login_required
    def get(self, **kwargs):
        [conn, cursor] = get_db()
        sql = """SELECT * FROM game"""
        cursor.execute(sql)
        games = cursor.fetchall()
        return jsonify(games)

    @login_required
    def post(self):
        data = json.loads(request.data)
        s = session
        name = data.get('name','')
        [conn, cursor] = get_db()
        sql = """INSERT INTO game (name) VALUES('{0}')""".format(name)
        cursor.execute(sql)
        conn.commit()
        return
