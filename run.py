from flask_app import flask_app
from db import db

db.init_app(flask_app)

@flask_app.before_first_request
def create_tables():
    db.create_all()
