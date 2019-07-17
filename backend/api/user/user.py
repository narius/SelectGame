from flask_restplus import Resource
from db import get_db
import json


class UsersWebAPI(Resource):
    def get(self, userid=None):
        if userid is not None:
            userid = int(userid)
        users = self.get_users(userid)
        return json.loads(users)

    def get_users(self ,userid=None):
        sql = """SELECT * FROM users"""
        if userid is not None:
            sql = sql + """WHERE id={0}""".format(userid)
        db = get_db()
        db.execute(sql)
        users = db.fetchall()
        return users
