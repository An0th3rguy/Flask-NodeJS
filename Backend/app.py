from flask import Flask
from datetime import datetime
from flask_json import FlaskJSON, json_response

app = Flask(__name__)
FlaskJSON(app)

@app.route('/')
def hello_world():
    now = datetime.utcnow()
    return json_response(time=now)