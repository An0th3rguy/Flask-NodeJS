from flask_restx import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import delete_user

api = UserDto.apiDeletion


@api.route('/delete/<int:id>')
class Delete(Resource):
    @api.response(201, 'User successfully deleted.')
    @api.doc('delete user')

    def delete(self, id):
        """Delete User """
        return delete_user(id=id)