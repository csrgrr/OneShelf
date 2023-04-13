from database.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, user, email, password):
        self.user = user
        self.email = email
        self.password = password
