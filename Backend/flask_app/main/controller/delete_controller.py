from flask import request
from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import delete_user

api = UserDto.apiDeletion
# _user_get = UserDto.user_get
_user_delete = UserDto.user_delete

@api.route('/delete')
class Delete(Resource):
    @api.response(201, 'User successfully deleted.')
    @api.doc('delete user')
    @api.expect(_user_delete, validate=True)

    def post(self):
        """Delete User """
        id = request.json
        return delete_user(id=id)