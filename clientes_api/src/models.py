from datetime import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    cedula = db.Column(db.String(10), unique=True)
    nombres = db.Column(db.String(40))
    apellidos = db.Column(db.String(40))
    email = db.Column(db.String(100))
    celular = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'cedula': self.cedula,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'email': self.email,
            'celular': self.celular,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }    
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(15), unique=True)
    nombre_completo = db.Column(db.String(70))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'nombre_completo': self.nombre_completo,            
            'email': self.email,            
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }
