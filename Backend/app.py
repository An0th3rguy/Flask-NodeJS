from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_json import FlaskJSON, json_response
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
FlaskJSON(app)
CORS(app)
bcrypt = Bcrypt(app)

connectionstring = 'postgresql+psycopg2://postgres:postgres@db:5433'

app.config['SQLALCHEMY_DATABASE_URI'] = connectionstring
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password
        }

'''
with app.app_context():
    db.drop_all()
    db.create_all()
'''

@app.route('/')
def home():
    now = datetime.utcnow()
    return json_response(time=now)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    data = {'data': [user.toDict() for user in users]}
    return data

'''
@app.route('/user/<string:name>', methods=['GET'])
def get_user(name):
    user = User.query.filter_by(name=name).first()
    return json_response(id=user.id, name=user.name)
'''

@app.route('/user/create/<string:name>/<string:password>', methods=['GET', 'POST'])
def create_user(name, password):
    password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(name=name, password=password)
    db.session.add(user)
    db.session.commit()
    result = User.query.filter_by(name=name).first()
    return result.name

@app.route('/login/<string:name>/<string:password>', methods=['GET'])
def login(name, password):
    user = User.query.filter_by(name=name).first()
    if bcrypt.check_password_hash(user.password, password):
        return "success"
    else:
        return "fail"