from pickle import FALSE
from flask import Flask, jsonify, make_response, request
from envs.dev.dev_env import config, get_database_config
from database.db import init_app
from controller_routes.routes.article_routes import article_routes
from controller_routes.routes.genre_routes import genre_routes
from flask_cors import CORS
from flask_jwt_extended import create_access_token, JWTManager, jwt_required
import os
from dotenv import load_dotenv
import datetime
from pkg_resources import require

load_dotenv()

app = Flask(__name__)

# Cors config
app.config['JSON_AS_ASCII'] = False
CORS(app)


# jwt-config
app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')
jwt = JWTManager(app)

def obtener_payload():
    payload = {
        'user':'pepe',
        'rol': 'ADMIN'
    }
    return payload


@app.post("/token")
def crear_token():
    token_config = {
        'paload': obtener_payload(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = create_access_token(token_config)
    return jsonify({"token": token})

@app.post("/login")
def login():
    username = request.json['username']
    password = request.json['password']

    if username == 'pepe' and password == '12345':
        return crear_token()
    else:
        respuesta = make_response({"error-401": "error de autenticación"})
        respuesta.status_code = 401
        return respuesta

@app.get("/dashboard")
@jwt_required()
def dashboard():
    users = {
        'username': 'pepe',
        'email': 'pepe@es.es'
    }
    return jsonify(users)
 




# Database config
user = get_database_config().get('MYSQL_USER')
host = get_database_config().get('MYSQL_HOST')
password = get_database_config().get('MYSQL_PASSWORD')
database = get_database_config().get('DATABASE_NAME')
sql_track_modifications = get_database_config().get('SQLALCHEMY_TRACK_MODIFICATIONS')

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://'+user+'@'+host+'/'+database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = sql_track_modifications

init_app(app)

# Blueprints
app.register_blueprint(article_routes)
app.register_blueprint(genre_routes)

# MAIN
if __name__ == '__main__':
    app.config.from_object(config['dev'])
    app.run()
