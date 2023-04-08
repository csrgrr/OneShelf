from flask import request, jsonify
from dao.article import Article
from dao_schema.article_schema import articles_schema, article_schema
from database.db import db


# Listar todos los artículos
def get_articles():
    articles = Article.query.all()
    return articles_schema.dump(articles)


# Buscar un artículo por id
def get_article_by_id(article_id):
    article = Article.query.get(article_id)
    if article:
        return article_schema.dump(article)
    else:
        return jsonify({'message': 'Article not found.'}), 404


# Crear un nuevo artículo
def create_article():
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


# Actualizar un artículo existente
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


# Eliminar un artículo existente
def delete_article(article_id):
    article = Article.query.get(article_id)
    if article:
        db.session.delete(article)
        db.session.commit()
        return jsonify({'message': 'Article successfully deleted.'})
    else:
        return jsonify({'message': 'Article not found.'}), 404
