from flask import Blueprint, jsonify, request
from dao.user import User
from dao_schema.user_schema import user_schema, users_schema
from database.db import db

user_routes = Blueprint('user_routes', __name__)

# Ruta para obtener todos los usuarios
@user_routes.route('/users')
def users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

# Ruta para obtener un usuario por username
@user_routes.route('/users/<string:username>')
def user_by_username(username):
    user = User.query.filter_by(user = username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user_schema.dump(user))

# Ruta para crear un nuevo usuario
@user_routes.route('/add-user', methods=['POST'])
def add_user():
    user = request.json['user']
    email = request.json['email']
    password = request.json['password']

    userClass = User(user, email, password)
    db.session.add(userClass)
    db.session.commit()

    return user_schema.dump(userClass)

# Ruta para actualizar un usuario existente
@user_routes.route('/update-user/<string:username>', methods=['PUT'])
def update_user(username):
    userClass = User.query.filter_by(user=username).first()
    if not userClass:
        return jsonify({'message': 'User not found'}), 404
    userClass.user = request.json['user']
    userClass.email = request.json['email']
    userClass.password = request.json['password']
    db.session.commit()
    return user_schema.dump(userClass)

# Ruta para eliminar un usuario existente
@user_routes.route('/delete-user/<string:username>', methods=['DELETE'])
def delete_user(username):
    userClass = User.query.filter_by(user=username).first()
    if not userClass:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(userClass)
    db.session.commit()

    return user_schema.dump(userClass)