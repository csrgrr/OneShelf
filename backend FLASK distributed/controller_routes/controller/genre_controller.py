from flask import request, jsonify
from dao.genre import Genre
from dao_schema.genre_schema import genres_schema, genre_schema
from database.db import db


def get_genres():
    genres = Genre.query.all()
    return genres_schema.dump(genres)


def save_genre():
    name = request.json['genre']
    color = request.json['color']

    genre = Genre(name, color)
    db.session.add(genre)
    db.session.commit()
    return genre_schema.dump(genre)


def update_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        name = request.json.get('name', genre.name)

        genre.name = name

        db.session.commit()
        return genre_schema.dump(genre)
    else:
        return jsonify({'message': 'Genre not found.'}), 404


def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        db.session.delete(genre)
        db.session.commit()
        return jsonify({'message': 'Genre successfully deleted.'})
    else:
        return jsonify({'message': 'Genre not found.'}), 404
