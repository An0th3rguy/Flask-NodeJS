from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import login_post


api = UserDto.apiLogin
_user_login = UserDto.user_login


@api.route('/login')
class Login(Resource):
    @api.response(202, 'User login.')
    @api.doc('login user')
    @api.expect(_user_login, validate=True)

    def post(self):
        #user token
        return login_post()