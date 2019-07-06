from flask_restplus import Resource, abort
from flask import request, session
from db import get_db
from datetime import datetime
import json
import logging
import hashlib
from api.decorators import login_required

class LoginWebAPI(Resource):
    @login_required
    def get(self, userid):
        logging.debug(session.get('userid','missing'))
        return 200

    def post(self):
        data = json.loads(request.data)
        self.username = data.get('username', "")
        self.password = data.get('password', "")
        hashed_password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        [conn, db] = get_db()
        sql = """SELECT id, password,username FROM users WHERE username='{}'""".format(self.username)
        db.execute(sql)
        result = db.fetchall()[0]
        userpassword = result['password']
        if userpassword == hashed_password:
            session['userid'] = result['id']
            s_date = str(datetime.utcnow())
            string = result['username']+s_date
            hashed_session = hashlib.sha224(string.encode('utf-8')).hexdigest()
            sql = """INSERT INTO session(user_id, hashed_session) VALUES ({0},'{1}')"""
            sql = sql.format(result['id'], hashed_session)
            db.execute(sql);
            conn.commit()
            return hashed_session
        else:
            abort(401,"Invalid username or password") # Invalid password

    def delete(self):
        print(session.get('userid','missing'))
        session.pop('userid')
        print(session.get('userid', 'missing'))
