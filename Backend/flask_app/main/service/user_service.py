import uuid
#import datetime

from .. import db
from ..model.User import User

def get_all_users():
    users = User.query.all()
    response_object = {
            'status': 'success',
            'data': [user.toDict() for user in users],
        }
    return response_object, 200

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

def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    response_object = {
           'status': 'success',
           'message': 'Successfully deleted.'
        }
    return response_object, 201

def login_post():
    name = request.json.get("name", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(name=name).first()
    if user:
        if user.check_password(password):
            access_token = create_access_token(identity=name)
            return jsonify(access_token=access_token)
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    else:
        return "User not found"



def save_changes(data):
    db.session.add(data)
    db.session.commit()