from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@127.0.0.1/shelf"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


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


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(250), nullable=True)
    color = db.Column(db.String(250), nullable=True)

    def __init__(self, genre, color):
        self.genre = genre,
        self.color = color


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
    article_genre = fields.Integer()
    pdf = fields.String()

class GenreSchema(Schema):
    id = fields.Integer()
    genre = fields.String()
    color = fields.String()
    articles = fields.Nested(ArticleSchema, many=True)
    article_genre = fields.Integer()



genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# SHOW
@app.get("/genres")
def get_genres():
    genres = Genre.query.all()
    return genres_schema.dump(genres)

@app.get("/articles")
def get_articles():
    articles = Article.query.all()
    return articles_schema.dump(articles)

# SAVE
@app.post("/save-genre")
def save_genre():
    genre_name = request.json['genre']
    color = request.json['color']
    genre = Genre(genre_name, color)
    db.session.add(genre)
    db.session.commit()
    return genre_schema.dump(genre)


@app.post("/save-article")
def save_article():
    authors = request.json['authors']
    year = request.json['year']
    title = request.json['title']
    journal = request.json['journal']
    issue = request.json['issue']
    place = request.json['place']
    doi = request.json['doi']
    genreId = request.json['genreId']
    pdf = request.json['pdf']

    article = Article(authors, year, title, journal, issue, place, doi, genreId, pdf)
    db.session.add(article)
    db.session.commit()
    return article_schema.dump(article)


# UPDATE
@app.put("/update-genre/<int:id>")
def update_genre(id):
    genre = Genre.query.get(id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    genre.genre = request.json['genre']
    genre.color = request.json['color']
    db.session.commit()
    return genre_schema.dump(genre)

@app.put("/update-article/<int:article_id>")
def update_article(article_id):
    article = Article.query.get(article_id)
    if article:
        authors = request.json.get('authors', article.authors)
        year = request.json.get('year', article.year)
        title = request.json.get('title', article.title)
        journal = request.json.get('journal', article.journal)
        issue = request.json.get('issue', article.issue)
        place = request.json.get('place', article.place)
        doi = request.json.get('doi', article.doi)
        genreId = request.json.get('genreId', article.genreId)
        pdf = request.json.get('pdf', article.pdf)

        article.authors = authors
        article.year = year
        article.title = title
        article.journal = journal
        article.issue = issue
        article.place = place
        article.doi = doi
        article.genreId = genreId
        article.pdf = pdf

        db.session.commit()
        return article_schema.dump(article)
    else:
        return jsonify({'message': 'Article not found.'}), 404


# DELETE
@app.delete("/delete-article/<int:article_id>")
def delete_article(article_id):
    article = Article.query.get(article_id)
    if article:
        db.session.delete(article)
        db.session.commit()
        return jsonify({'message': 'Article successfully deleted.'})
    else:
        return jsonify({'message': 'Article not found.'}), 404

@app.delete("/delete-genre/<int:id>")
def delete_genre(id):
    genre = Genre.query.get(id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    db.session.delete(genre)
    db.session.commit()
    return jsonify({'message': 'Genre successfully deleted'}), 200





if __name__ == '__main__':
    app.run(debug=True)
