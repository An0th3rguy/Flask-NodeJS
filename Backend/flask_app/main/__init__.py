from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from .config import config_by_name

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    return app

#    with app.app_context():
#        db.drop_all()

#    with app.app_context():
#        db.create_all()