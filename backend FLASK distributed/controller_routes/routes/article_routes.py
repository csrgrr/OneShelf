from flask import Blueprint, jsonify, request
from controller_routes.controller.article_controller import get_articles, create_article, update_article, delete_article

article_routes = Blueprint('article_routes', __name__)


# Ruta para obtener todos los artículos
@article_routes.route('/articles')
def articles():
    articles = get_articles()
    return jsonify(articles)


# Ruta para guardar un nuevo artículo
@article_routes.route('/save-article', methods=['POST'])
def add_article():
    article = create_article(request)
    return jsonify(article)


# Ruta para actualizar un artículo existente
@article_routes.route('/article-update/<int:article_id>', methods=['PUT'])
def update_existing_article(article_id):
    updated_article = update_article(article_id, request)
    return jsonify(updated_article)


# Ruta para eliminar un artículo existente
@article_routes.route('/delete-article/<int:article_id>', methods=['DELETE'])
def delete_existing_article(article_id):
    result = delete_article(article_id)
    return jsonify(result)
