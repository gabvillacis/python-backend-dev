from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Optional

class ClienteForm(FlaskForm):
    cedula = StringField('cedula', validators=[DataRequired(), Length(min=10, max=10, message="El campo cédula debe tener 10 caracteres")])
    nombres = StringField('nombres', validators=[DataRequired(message="El campo nombres es obligatorio")])
    apellidos = StringField('apellidos', validators=[DataRequired(message="El campo apellidos es obligatorio")])
    email = StringField('email', validators=[DataRequired(message="El campo email es obligatorio")])
    celular = StringField('celular', validators=[Optional()])
    
class UsuarioForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=15, message="El campo username debe tener máx 15 caracteres")])
    nombre_completo = StringField('nombre_completo', validators=[DataRequired(message="El campo nombre_completo es obligatorio")])    
    email = StringField('email', validators=[DataRequired(message="El campo email es obligatorio")])
    password = StringField('password', validators=[DataRequired(message="El campo password es obligatorio")])
    
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=15, message="El campo username debe tener máx 15 caracteres")])    
    password = StringField('password', validators=[DataRequired(message="El campo password es obligatorio")])