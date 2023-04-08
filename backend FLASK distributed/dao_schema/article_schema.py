from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from dao_schema.genre_schema import GenreSchema

ma = Marshmallow()

class ArticleSchema(Schema):
    id = fields.Integer()
    authors = fields.String()
    year = fields.Integer()
    title = fields.String()
    journal = fields.String()
    issue = fields.Integer()
    place = fields.String()
    doi = fields.String()
    genreId = fields.Integer()
    genre = fields.Nested(GenreSchema, only=["id", "genre", "color"])
    pdf = fields.String()

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
