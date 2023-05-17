#from flask import request
from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import get_all_users

api = UserDto.apiUser
# _user_get = UserDto.user_get
#_user_register = UserDto.user_register


@api.route('/')
class UserList(Resource):
    @api.response(200, 'Success')
    @api.doc('get list of users')

    def get(self):      #Gets list of users
        return get_all_users()
#        return {'response':'Success'}