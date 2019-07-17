from flask import current_app, g
import psycopg2
import psycopg2.extras


def get_db():
    with current_app.app_context():
        if 'db' not in g:
            g.db_conn = psycopg2.connect(current_app.config['DATABASE_URI'])
            g.db = g.db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return g.db_conn,g.db
