from flask_restx import Namespace, fields, cors
from datetime import datetime


class UserDto:
    api = Namespace('user', description='user related operations', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    user_register = api.model('user_register',{
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'name': fields.String(required=False, description='user first name'),
        'surname': fields.String(required=False, description='user last name')
        # 'public_id': fields.Ïnteger(description='user Identifier')
    })
    # user_get = api.model('user_register',{
    #     'email': fields.String(required=True, description='user email address'),
    #     'name': fields.String(required=False, description='user first name'),
    #     'surname': fields.String(required=False, description='user last name')
    #     # 'public_id': fields.Ïnteger(description='user Identifier')
    # })