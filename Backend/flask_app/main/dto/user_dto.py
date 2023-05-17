from flask_restx import Namespace, fields, cors

class UserDto:
    apiUser = Namespace('user', description='user related operations', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    apiRegistration = Namespace('registration', description='registration', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    apiDeletion = Namespace('deletion', description='deletion', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    apiLogin = Namespace('registration', description='login', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])

    user_register = apiRegistration.model('user_register',{
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'name': fields.String(required=False, description='user first name'),
        'surname': fields.String(required=False, description='user last name')
        # 'public_id': fields.Ïnteger(description='user Identifier'
    })

    user_login = apiRegistration.model('user_login',{
        'name': fields.String(required=True, description='user first name'),
        'password': fields.String(required=True, description='user password')
    })