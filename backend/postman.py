from flask import json

from api import app
from api.routes import api as ap

app.config['SERVER_NAME'] = 'localhost'

with app.app_context():
    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications
    data = ap.as_postman(urlvars=urlvars, swagger=swagger)
    print(json.dumps(data))
