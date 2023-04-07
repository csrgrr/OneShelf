from database.db import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authors = db.Column(db.String(250), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(1000), nullable=True)
    journal = db.Column(db.String(250), nullable=True)
    issue = db.Column(db.Integer, nullable=True)
    place = db.Column(db.String(250), nullable=True)
    doi = db.Column(db.String(1000), nullable=True)
    genreId = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre', backref='articles')
    pdf = db.Column(db.String(1000), nullable=True)

    def __init__(self, authors, year, title, journal, issue, place, doi, genre_id, pdf):
        self.authors = authors
        self.year = year
        self.title = title
        self.journal = journal
        self.issue = issue
        self.place = place
        self.doi = doi
        self.genreId = genre_id
        self.pdf = pdf
