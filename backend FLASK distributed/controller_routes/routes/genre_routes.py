from flask import Blueprint, jsonify, request
from controller_routes.controller.genre_controller import get_genres, save_genre, update_genre, delete_genre

genre_routes = Blueprint('genre_routes', __name__)

# Ruta para obtener todos los géneros
@genre_routes.route('/genres')
def genres():
    genres = get_genres()
    return jsonify(genres)

# Ruta para guardar un nuevo género
@genre_routes.route('/genres', methods=['POST'])
def add_genre():
    genre = save_genre(request)
    return jsonify(genre)

# Ruta para actualizar un género existente
@genre_routes.route('/update-genre/<int:genre_id>', methods=['PUT'])
def update_existing_genre(genre_id):
    updated_genre = update_genre(genre_id, request)
    return jsonify(updated_genre)

# Ruta para eliminar un género existente
@genre_routes.route('/delete-genre/<int:genre_id>', methods=['DELETE'])
def delete_existing_genre(genre_id):
    result = delete_genre(genre_id)
    return jsonify(result)
