from src.models import db, Cliente, Usuario
from src.schemas import ClienteForm, UsuarioForm, LoginForm
from flask_wtf.csrf import generate_csrf
from sqlalchemy.exc import IntegrityError
import src.utils as utils
from flask import request
from datetime import datetime
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta

@utils.csrf.exempt
def crear_cliente():
    body = ClienteForm()

    body.csrf_token.data = generate_csrf()

    if body.validate_on_submit():
        try:
            cliente = Cliente(
                cedula=body.cedula.data,
                nombres=body.nombres.data,
                apellidos=body.apellidos.data,
                email=body.email.data,
                celular=body.celular.data
            )
            
            db.session.add(cliente)
            db.session.commit()
            return {'status': 'success', 'data': {'cliente': cliente.to_dict()}}, 201
        except IntegrityError:
            db.session.rollback()
            return {'status': 'fail', 'message': 'Cliente con cédula duplicada'}, 409

    else:
        return {'status': 'fail', 'errors': body.errors}, 400

@jwt_required()
def obtener_clientes():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('limit', default=10, type=int)

    clientes = Cliente.query.paginate(page=page, per_page=per_page, error_out=False)
    clientes_list = [cliente.to_dict() for cliente in clientes.items]
    
    resultado = {
        'status': 'success',
        'clientes': clientes_list,
        'pages': clientes.pages,
        'limit': clientes.per_page,
        'results': len(clientes_list)
    }

    return resultado

@jwt_required()
def obtener_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)

    if cliente:
        return {"status": "success", 'data': {'cliente': cliente.to_dict()}}
    else:
        return {"status": "fail", 'message': f'Cliente con id {cliente_id} no existe'}, 404

@utils.csrf.exempt
def actualizar_cliente(cliente_id):
    body = ClienteForm()

    body.csrf_token.data = generate_csrf()

    if body.validate_on_submit():
        cliente = Cliente.query.get(cliente_id)

        if cliente:
            if body.nombres.data:
                cliente.nombres = body.nombres.data
            if body.apellidos.data:
                cliente.apellidos = body.apellidos.data
            if body.email.data:
                cliente.email = body.email.data
            if body.celular.data:
                cliente.celular = body.celular.data

            cliente.updated_at = datetime.utcnow()
            db.session.commit()

            return {"status": "success", "data": {"cliente": cliente.to_dict()}}
        else:
            return {"status": "fail", 'message': f'Cliente con id {cliente_id} no existe'}, 404
    else:
        return {'status': 'fail', 'errors': body.errors}, 400

@utils.csrf.exempt
@jwt_required()
def eliminar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)

    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return {"status": "success", "message": f"Cliente con id {cliente_id} eliminado exitosamente"}, 204
    else:
        return {"status": "fail", "message": f"Cliente con id {cliente_id} no existe"}, 404

@utils.csrf.exempt
def crear_usuario():
    body = UsuarioForm()

    body.csrf_token.data = generate_csrf()

    if body.validate_on_submit():
        try:
            usuario = Usuario(
                username=body.username.data,
                nombre_completo=body.nombre_completo.data,
                email=body.email.data,
                password=utils.get_password_hash(body.password.data)
            )
            
            db.session.add(usuario)
            db.session.commit()
            return {'status': 'success', 'data': {'usuario': usuario.to_dict()}}, 201
        except IntegrityError:
            db.session.rollback()
            return {'status': 'fail', 'message': 'Usuario duplicado'}, 409

    else:
        return {'status': 'fail', 'errors': body.errors}, 400
      
@utils.csrf.exempt  
def crear_token():
    body = LoginForm()

    body.csrf_token.data = generate_csrf()

    if body.validate_on_submit():    
        usuario = Usuario.query.filter_by(username=body.username.data).first()    
        if usuario is None:
            return {'status': 'fail', 'message': 'Usuario/Contraseña incorrectos'}, 401
        else:
            if not utils.verify_password(body.password.data, usuario.password):
                return {'status': 'fail', 'message': 'Usuario/Contraseña incorrectos'}, 401

        access_token = create_access_token(identity=usuario.username, expires_delta=timedelta(minutes=1))
        return {"status": "success", "token": access_token}