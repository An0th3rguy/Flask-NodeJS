from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import get_all_users, get_user

api = UserDto.apiUser


@api.route('/')
class UserList(Resource):
    @api.response(200, 'Success')
    @api.doc('get list of users')

    def get(self):
        return get_all_users()

@api.route('/<int:id>')
class User(Resource):
    @api.response(200, 'Success')
    @api.doc('get user')

    def get(self, id):
        return get_user(id=id)