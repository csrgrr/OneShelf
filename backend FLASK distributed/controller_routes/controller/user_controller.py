from flask import request, jsonify
from dao.user import User
from dao_schema.user_schema import users_schema, user_schema
from database.db import db

# Listar todos los usuarios
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)


# Buscar un usuario por id
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return user_schema.dump(user)
    else:
        return jsonify({'message': 'User not found.'}), 404


# Crear un nuevo usuario
def create_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user = User(name, email, password)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)


# Actualizar un usuario existente
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        name = request.json.get('name', user.name)
        email = request.json.get('email', user.email)
        password = request.json.get('password', user.password)

        user.name = name
        user.email = email
        user.password = password

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
