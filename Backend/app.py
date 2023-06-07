# from datetime import datetime
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_json import FlaskJSON, json_response
# from flask_cors import CORS
# from flask_bcrypt import Bcrypt

# from flask import jsonify
# from flask import request

# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager

# from flask_restx import Resource,Api

# app = Flask(__name__)
# FlaskJSON(app)
# CORS(app)
# bcrypt = Bcrypt(app)
# api = Api(app)

# app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
# jwt = JWTManager(app)

# connectionstring = 'postgresql+psycopg2://postgres:postgres@db:5433'

# app.config['SQLALCHEMY_DATABASE_URI'] = connectionstring
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     surname = db.Column(db.String(128))
#     email = db.Column(db.String(128), unique=True)
#     password_hash = db.Column(db.String(128))

#     @property
#     def password(self):
#         raise AttributeError('password: write-only field')

#     @password.setter
#     def password(self, password):
#         self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.password_hash, password)

#     def toDict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'surname': self.surname,
#             'email': self.email
#         }

# '''
# with app.app_context():
#     db.drop_all()
#     db.create_all()
# '''

# @api.route('/')
# class Home(Resource):
#     def get(self):
#         now = datetime.utcnow()
#         return json_response(time=now)

# @app.route('/users', methods=['GET'])
# @jwt_required()
# def get_users():
#     users = User.query.all()
#     data = {'data': [user.toDict() for user in users]}
#     return data

# @app.route('/user/create/<string:name>/<string:password>', methods=['GET', 'POST'])
# def create_user(name, password):
#     user = User(name=name, password=password)
#     db.session.add(user)
#     db.session.commit()
#     return "User added"

# @app.route('/login/<string:name>/<string:password>', methods=['GET'])
# def login(name, password):
#     user = User.query.filter_by(name=name).first()
#     if user:
#         if user.check_password(password):
#             return "Success"
#         else:
#             return "Incorrect username or password"
#     else:
#         return "User not found"


# @app.route('/user/create', methods=['POST'])
# def create_user_post():
#     name = request.json.get("name", None)
#     password = request.json.get("password", None)
#     user = User(name=name, password=password)
#     db.session.add(user)
#     db.session.commit()
#     return "User added"

# @app.route('/login', methods=['POST'])
# def login_post():
#     name = request.json.get("name", None)
#     password = request.json.get("password", None)
#     user = User.query.filter_by(name=name).first()
#     if user:
#         if user.check_password(password):
#             access_token = create_access_token(identity=name)
#             return jsonify(access_token=access_token)
#         else:
#             return jsonify({"msg": "Bad username or password"}), 401
#     else:
#         return "User not found"


import os

from flask_migrate import Migrate

from flask_app import blueprint
from flask_app.main import create_app, db
#from flask_app.main.model import User

from flask_cors import CORS

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
migrate = Migrate(app, db)

# Nastavení povolení všech Cross-Origin přístupů
CORS(app, resources={r"/*": {"origins": "*"}}) # Stále to hází na frontendu chybu CORS

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)