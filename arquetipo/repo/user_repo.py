from dao.user import User
from database.db import db


# Listar usuarios
def find_all_repo():
    users = User.query.all()
    return users


# Buscar usuario por id
def find_one_repo(id):
    return User.query.get(id)


# Buscar usuario por username
def find_by_username_repo(username):
    data = User.query.filter(User.username == username).all()
    results = []
    for i in data:
        info = {
            'id': i.id,
            'username': i.username,
            'email': i.email,
            'password': i.password
        }
        results.append(info)
    return results


# Guardar usuarios
def save_repo(user):
    db.session.add(user)
    db.session.commit()
    return user


# Modificar usuarios
def update_repo(id, user):
    user_by_id = User.query.get(id)
    user_by_id.id = id
    user_by_id.username = user.username
    user_by_id.email = user.email
    user_by_id.password = user.password
    db.session.commit()
    return user

# Eliminar usuarios
def delete_repo(id):
    user_by_query = User.query.get(id)
    db.session.delete(user_by_query)
    db.session.commit()