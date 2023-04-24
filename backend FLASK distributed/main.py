import pickle
from flask import Flask, jsonify, make_response, request, send_file
from dao.user import User
from envs.dev.dev_env import config, get_database_config
from database.db import init_app
from controller_routes.routes.article_routes import article_routes
from controller_routes.routes.genre_routes import genre_routes
from controller_routes.routes.user_routes import user_routes
from flask_cors import CORS
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required
import os
from dotenv import load_dotenv
import datetime
from pkg_resources import require

load_dotenv()

app = Flask(__name__)

# Cors config
app.config['JSON_AS_ASCII'] = False
CORS(app)


# jwt-config/////////////////////////////////////////////////////////////////////
app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')
jwt = JWTManager(app)

def obtener_payload():
    payload = {
        'user':'pepe',
        'rol': 'ADMIN'
    }
    return payload




from dao.user import User
from dao_schema.user_schema import user_schema
from flask_jwt_extended import create_access_token


@app.post("/login")
def login():
    username = request.json['username']
    password = request.json['password']

    # Consulta en la base de datos para encontrar un usuario con el nombre de usuario y la contraseña especificados
    user = User.query.filter_by(user=username, password=password).first()

    if user:
        # Genera y devuelve un token JWT
        token_config = {
            'payload': {'username': user.user, 'email': user.email},
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = create_access_token(token_config)
        return jsonify({"token": token})
    else:
        # Devuelve un error de autenticación
        respuesta = make_response({"error-401": "error de autenticación"})
        respuesta.status_code = 401
        return respuesta


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/dashboard", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    current_user = current_user["payload"]
    return jsonify(current_user)

##//////////////////////////////////////////////////////////////////////


# SUBIR ARCHIVOS /////////////////////////////////////////////////////////////////////

def chunks(lst, n):
    #"""Divide una lista en lotes de tamaño n."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Verificar si la carpeta existe, si no, crearla
        if not os.path.exists('pdfs'):
            os.makedirs('pdfs')

        # Obtener los archivos
        files = request.files.getlist('file')

        #Enviar los archivos por lotes
        batch_size = 10  # Define el tamaño máximo de un lote
        #El número 10 en batch_size representa el tamaño máximo de un lote de archivos que se enviará en una sola petición. 
        #En otras palabras, si el usuario selecciona 30 archivos para subir, estos archivos se dividirán en 3 lotes de 10 archivos cada uno
        batches = list(chunks(files, batch_size))
        total_files = len(files)
        total_batches = len(batches)
        for i, batch in enumerate(batches):
            # Guardar los archivos en la carpeta subidaArchivos\archivos
            for file in batch:
                file.save(os.path.join('pdfs', file.filename))

        # Devolver una respuesta JSON
        message = f'Se subieron {total_files} archivos en {total_batches} lotes'
        return jsonify({'message': message})
    else:
        return jsonify({'message': 'Solicitud no valida'})
    
##//////////////////////////////////////////////////////////////////////

@app.route('/pdf')
def pdf():
    # Abre el archivo PDF desde el sistema de archivos
    with open('pdfs/Osiris-Spelling-Database.pdf', 'rb') as f:
        pdf_bytes = f.read()
    
    pdf_path = 'C:/ALEJANDRO/OneShelf/backend FLASK distributed/pdfs/prueba.pdf'
    return send_file(pdf_path, as_attachment=True)

    # Devuelve el archivo PDF en formato de bytes
    # return send_file(pdf_bytes, attachment_filename='pdfs/archivo.pdf', as_attachment=pickle.FALSE)
##//////////////////////////////////////////////////////////////////////

##//////////////////////////////////////////////////////////////////////
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
app.register_blueprint(user_routes)

# MAIN
if __name__ == '__main__':
    app.config.from_object(config['dev'])
    app.run()

