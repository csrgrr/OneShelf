from flask import request, jsonify
from dao.user import User
from dao_schema.user_schema import users_schema, user_schema
from database.db import db


# Listar todos los usuarios
def get_users():
    users = User.query.all()
    return users_schema.dump(users)


# Buscar un usuario por id
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user_schema.dump(user)
    else:
        return jsonify({'message': 'User not found.'}), 404


# Crear un nuevo usuario
def create_user():
    user = User(
        user=request.json['user'],
        email=request.json['email'],
        password=request.json['password']
    )
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)


# Actualizar un usuario existente
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.user = request.json.get('user', user.user)
        user.email = request.json.get('email', user.email)
        user.password = request.json.get('password', user.password)

        db.session.commit()
        return user_schema.dump(user)
    else:
        return jsonify({'message': 'User not found.'}), 404


# Eliminar un usuario existente
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User successfully deleted.'})
    else:
        return jsonify({'message': 'User not found.'}), 404
