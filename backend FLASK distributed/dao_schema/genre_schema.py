from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

ma = Marshmallow()

class GenreSchema(Schema):
    id = fields.Integer()
    genre = fields.String()
    color = fields.String()

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
