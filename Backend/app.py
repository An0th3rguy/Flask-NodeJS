from flask import Flask
from datetime import datetime
from flask_json import FlaskJSON, json_response
from flask_cors import CORS

app = Flask(__name__)
FlaskJSON(app)
CORS(app)

@app.route('/')
def hello_world():
    now = datetime.utcnow()
    return json_response(time=now)