from flask_restx import Api
from flask import Blueprint

from .main.contoroller.user_contoroller import api as user_ns
from .main.contoroller.authorization_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')