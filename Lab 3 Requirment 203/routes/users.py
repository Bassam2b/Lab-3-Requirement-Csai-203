from flask import Blueprint, jsonify, request

users_bp = Blueprint('users_bp', __name__)

users = [
   
]


@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user': user})

@users_bp.route('/', methods=['POST'])
def create_user():
    new_user = {
        'id': users[-1]['id'] + 1 if users else 1,
        'name': request.json.get('name', ''),
        'email': request.json.get('email', ''),
        'age': request.json.get('age', 0)
    }
    users.append(new_user)
    return jsonify({'user': new_user}), 201

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    user['age'] = request.json.get('age', user['age'])
    return jsonify({'user': user})


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    users.remove(user)
    return jsonify({'result': True})
