from flask_restplus import Resource
from flask import request,jsonify
from api.enumerations import FEATURE_FLAGS
from db import get_db
import json
import hashlib


class RegistrationWebAPI(Resource):
    def get(self):
        pass

    def post(self):
        data = json.loads(request.data)
        self.registration_code = data.get('registration_code', "")
        self.username = data.get('username', "")
        self.firstname = data.get('firstname', "")
        self.surname = data.get('surname', "")
        self.email = data.get('email', "")
        self.password = data.get('password', "")
        if FEATURE_FLAGS.NEED_REGISTRATION_CODE and not self.check_registration_code():
            return 401 # invalid registration code
        if len(self.username)<3:
            return 402 #Too short username
        self.create_user()
        return 200

    # Returns True if the code is valid else False.
    def check_registration_code(self):
        sql = """SELECT id from registration_codes WHERE code='{}' and valid=true;""".format(self.registration_code)
        [conn,db] = get_db()
        db.execute(sql)
        codes = db.fetchall()
        return len(codes)>0

    def create_user(self):
        hashed_password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        sql = """INSERT INTO users(username, password, email, firstname, surname) VALUES('{0}','{1}','{2}','{3}','{4}') RETURNING id;"""
        sql = sql.format(self.username, hashed_password, self.email, self.firstname, self.surname)
        print(sql)
        [conn, db] = get_db()
        db.execute(sql)
        conn.commit()
        result = db.fetchall()
        print(result)
