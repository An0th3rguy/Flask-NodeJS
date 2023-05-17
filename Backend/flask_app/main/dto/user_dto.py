from flask_restx import Namespace, fields, cors
#from datetime import datetime

# vlastní autorizační namespace

class UserDto:
    apiUser = Namespace('user', description='user related operations', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    apiRegistration = Namespace('autorization', description='autorization', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])

    user_register = apiRegistration.model('user_register',{
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