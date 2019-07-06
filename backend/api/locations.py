from flask_restplus import Resource, abort
from flask import request, session
from db import get_db
import json
import hashlib
from api.decorators import login_required


class LocationsWebAPI(Resource):
    # all = True means that we take all locations, if false only the ones owned by user
    @login_required
    def get(self, *args, **kwargs):
        userid = kwargs['userid']
        r = request
        s = session
        [conn, cursor] = get_db()
        sql = """SELECT * FROM locations"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @login_required
    def post(self, userid):
        r = request
        headers = type(request.headers)
        headers_dict = dict(request.headers)
        token = headers_dict['Authorization']
        data = json.loads(request.data)
        name = data.get('name', '')
        ispublic = data.get('ispublic','')
        street = data.get('street', '')
        postalcode = data.get('postalcode', '')
        city = data.get('city', '')
        if None in [name, ispublic, street, postalcode,city]:
            abort(400)
        return {},201
