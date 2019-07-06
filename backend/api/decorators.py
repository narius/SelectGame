from functools import wraps
from flask import session, request
from flask_restplus import abort
from db import get_db

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #userid = session.get('userid', None)
        #if userid is None:
        #    abort(401, "Not loggedin") # Not logged in
        r = request
        headers_dict = dict(request.headers)
        token = headers_dict.get('Authorization','')
        if token == '':
            abort(401)
        [conn, cursor] = get_db()
        sql = """SELECT user_id FROM session WHERE hashed_session='{}'""".format(token)
        cursor.execute(sql)
        row = cursor.fetchone()
        if row == None:
            abort(401)
        userid = row['user_id']
        kwargs['userid'] = userid
        return f(*args, **kwargs)
    return decorated_function
