from flask import Flask
from envs.dev.dev_env import config, get_database_config
from database.db import init_app
from controller_routes.routes.article_routes import article_routes
from controller_routes.routes.genre_routes import genre_routes
from flask_cors import CORS

app = Flask(__name__)

# Cors config
app.config['JSON_AS_ASCII'] = False
CORS(app)

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
