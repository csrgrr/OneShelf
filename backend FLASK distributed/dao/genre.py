from database.db import db


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(250), nullable=True)
    color = db.Column(db.String(250), nullable=True)

    def __init__(self, genre, color):
        self.genre = genre
        self.color = color

