import uuid
#import datetime

from .. import db
from ..model.User import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            # id=str(uuid.uuid4()),
            name = data['name'],
            surname = data['surname'],
            email=data['email'],
            password=data['password']

        )

        save_changes(new_user)
        response_object = {
           'status': 'success',
           'message': 'Successfully registered.'
        }
        return response_object, 201
        # return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()