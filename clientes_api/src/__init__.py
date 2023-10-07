from flask import Flask
from dotenv import load_dotenv
from src.models import db, migrate
from src.controllers import *
import os
import src.utils as utils
from flask_jwt_extended import JWTManager

def handle_error(error):
    respuesta = {
        'status': 'error',
        'message': str(error)
    }
    return respuesta, 500

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    load_dotenv()    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    migrate.init_app(app, db)
    utils.csrf.init_app(app)
    jwt = JWTManager(app)

    @app.get('/api/health')
    def healthcheck():
        return {"status": "UP"}
    
    app.route('/api/clientes', strict_slashes=False, methods=['POST'])(crear_cliente)
    app.route('/api/clientes', strict_slashes=False, methods=['GET'])(obtener_clientes)
    app.route('/api/clientes/<string:cliente_id>', methods=['GET'])(obtener_cliente)
    app.route('/api/clientes/<string:cliente_id>', methods=['DELETE'])(eliminar_cliente)
    app.route('/api/clientes/<string:cliente_id>', methods=['PUT'])(actualizar_cliente)
    
    app.route('/api/usuarios', strict_slashes=False, methods=['POST'])(crear_usuario)
    
    app.route('/api/login', strict_slashes=False, methods=['POST'])(crear_token)

    app.register_error_handler(Exception, handle_error)

    @app.errorhandler(404)
    def handle_not_found_error(e):
        respuesta = {
            'status': 'fail',
            'message': 'Ruta no encontrada'
        }
        return respuesta, 404

    return app