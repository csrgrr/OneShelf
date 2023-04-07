from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from dao_schema.article_schema import ArticleSchema

ma = Marshmallow()

class GenreSchema(Schema):
    id = fields.Integer()
    genre = fields.String()
    color = fields.String()
    articles = fields.Nested(ArticleSchema, many=True)
    article_genre = fields.Integer()

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
