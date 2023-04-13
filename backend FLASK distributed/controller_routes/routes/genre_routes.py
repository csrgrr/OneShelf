from flask import Blueprint, jsonify, request
from controller_routes.controller.genre_controller import get_genres, save_genre, update_genre, delete_genre
from dao.genre import Genre
from dao_schema.genre_schema import genre_schema
from database.db import db
from flask_cors import CORS

genre_routes = Blueprint('genre_routes', __name__)
CORS(genre_routes)


# Ruta para guardar un nuevo género
@genre_routes.route('/save-genre', methods=['POST'])
def save_genre():
    genre = request.json['genre']
    color = request.json['color']
    genreClass = Genre(genre, color)
    db.session.add(genreClass)
    db.session.commit()
    return genre_schema.dump(genre)

# Ruta para obtener todos los géneros
@genre_routes.route('/genres')
def genres():
    genres = get_genres()
    return jsonify(genres)
#genre by id
@genre_routes.get("/genres/<int:genre_id>")
def get_genre_by_id(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        return genre_schema.dump(genre)
    else:
        return jsonify({'message': 'Genre not found.'}), 404

# Ruta para update un género
@genre_routes.put("/update-genre/<int:id>")
def update_genre(id):
    genre = Genre.query.get(id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    genre.genre = request.json['genre']
    genre.color = request.json['color']
    db.session.commit()
    return genre_schema.dump(genre)



# Ruta para actualizar un género existente
@genre_routes.route('/update-genre/<int:genre_id>', methods=['PUT'])
def update_existing_genre(genre_id):
    updated_genre = update_genre(genre_id, request)
    return jsonify(updated_genre)

# Ruta para eliminar un género existente
@genre_routes.delete("/delete-genre/<int:id>")
def delete_genre(id):
    genre = Genre.query.get(id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    db.session.delete(genre)
    db.session.commit()
    return jsonify({'message': 'Genre successfully deleted'}), 200
