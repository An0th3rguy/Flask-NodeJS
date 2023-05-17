from flask import request
from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import save_new_user

api = UserDto.apiRegistration
_user_register = UserDto.user_register


@api.route('/registration')
class Registration(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user_register, validate=True)

    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)