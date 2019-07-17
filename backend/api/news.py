from flask_restplus import Resource, abort
from flask import request, session, jsonify
from db import get_db
import json
import hashlib
from api.decorators import login_required


class NewsWebAPI(Resource):
    # all = True means that we take all locations, if false only the ones owned by user
    @login_required
    def get(self, **kwargs):
        userid = userid = kwargs['userid']
        [conn, cursor] = get_db()
        news_sql = """SELECT * FROM news"""
        cursor.execute(news_sql)
        news = cursor.fetchall()
        return jsonify(news)

    @login_required
    def post(self,**kwargs):
        userid = userid = kwargs['userid']
        data = json.loads(request.data)
        header = data['header']
        text = data['text']
        [conn, cursor] = get_db()
        rating = data['rate']
        sql = """
        INSERT INTO news(writer_id,header, text) VALUES({0},{1},{2})"""
        sql = sql.format(userid,header,text)
        cursor.execute(sql);
        conn.commit()
        return
