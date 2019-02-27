# services/users/project/api/users.py
# Here, we created a new instance of the Blueprint class and bound the ping_pong() view function to it.


from flask import Blueprint, jsonify


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
