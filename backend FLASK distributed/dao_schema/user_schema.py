from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

ma = Marshmallow()

class UserSchema(Schema):
    user = fields.String()
    email = fields.Email()
    password = fields.String()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
