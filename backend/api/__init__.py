from flask import Flask, g
import psycopg2
import json
import logging
app = Flask(__name__)
app.config.from_pyfile("config.py", silent=False)

logging.basicConfig(filename='./log/backend.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    )
logging.info('Started')

def close_db():
    with app.app_context():
        if 'db' in g:
            g.db.close()
            g.db_conn.close()
        else:
            pass


with app.app_context():
    from api.routes import blueprint
    app.register_blueprint(blueprint)
