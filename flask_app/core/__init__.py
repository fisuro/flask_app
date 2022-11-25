from flask import Flask
from core.database import db_session
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

import core.views

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()