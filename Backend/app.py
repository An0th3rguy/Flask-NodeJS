from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_json import FlaskJSON, json_response
from flask_cors import CORS

app = Flask(__name__)
FlaskJSON(app)
CORS(app)

connectionstring = 'postgresql+psycopg2://postgres:postgres@db:5432'

app.config['SQLALCHEMY_DATABASE_URI'] = connectionstring
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    now = datetime.utcnow()
    return json_response(time=now)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
