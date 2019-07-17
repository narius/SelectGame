from flask_restplus import Resource, abort
from flask import request, session, jsonify
from db import get_db
import json
import hashlib
from api.decorators import login_required
from api.enumerations import EVENT_INVITE_STATUS
import logging


class EventInviteWebAPI(Resource):

    @login_required
    def get(self, **kwargs):
        userid = kwargs['userid']
        [conn, cursor] = get_db()
        sql = """SELECT event.id event_id, event.name event_name, event.eventdate FROM users
INNER JOIN event_participant ON event_participant.user_id=users.id AND event_participant.status='event.status.sent'
INNER JOIN event ON event.id=event_participant.event_id
WHERE users.id={}""".format(userid)
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify(result)


    @login_required
    def patch(self, **kwargs):
        userid = kwargs['userid']
        [conn, cursor] = get_db()
        logging.debug(request.data)
        r = request
        data = json.loads(request.data)
        event_id = data.get('event_id', '')
        result = {}
        sql = """SELECT * FROM users
WHERE id not in (SELECT user_id FROM event_participant WHERE event_id={0})
AND id not in (SELECT event.owner FROM event WHERE id={0})
AND id not in (SELECT event.creator FROM event WHERE id={0});""".format(event_id)
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify(result)

    @login_required
    def post(self, **kwargs):
        [conn, cursor] = get_db()
        userid = kwargs['userid']
        data = json.loads(request.data)
        receiver = data.get('receiver','')
        event_id = data.get('event_id','')
        if receiver == '' or event_id == '':
            abort(400)
        sql = """INSERT INTO event_participant (event_id, user_id, status, invited_by)
        VALUES({0}, {1}, '{2}', {3})"""
        sql = sql.format(event_id,receiver,EVENT_INVITE_STATUS.SENT,userid)
        cursor.execute(sql)
        conn.commit()
        return

    # Used to change status of invite
    @login_required
    def put(self,**kwargs):
        [conn, cursor] = get_db()
        userid = kwargs['userid']
        data = json.loads(request.data)
        event_id = data.get('event_id','')
        status = data.get('status', '')
        if event_id=='' or status=='':
            abort(400)
        sql = """UPDATE event_participant SET status='{0}' 
                 WHERE user_id={1} AND event_id={2}""".format(status,userid,event_id)
        cursor.execute(sql)
        conn.commit()
        return
