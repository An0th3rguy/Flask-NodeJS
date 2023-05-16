from flask import request
from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import save_new_user

api = UserDto.api
# _user_get = UserDto.user_get
_user_register = UserDto.user_register


@api.route('/')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user_register, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)