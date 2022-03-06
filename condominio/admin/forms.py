from wtforms import Form, StringField, PasswordField, validators, ValidationError
from flask_wtf import FlaskForm
from .modules import Sindico

class RegisterSindico(Form):
    nome = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
    usuario = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
    email = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
    tel = StringField('', [validators.length(min=1, max=20), validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired(), validators.EqualTo('confirm', message='As senhas devem ser iguais!')])
    confirm = PasswordField('',[validators.DataRequired()])

    def validate_usuario(self,usuario):
        if Sindico.query.filter_by(usuario=usuario.data).first():
            raise ValidationError('Este usuário já esta cadastrado!')

    def validate_email(self,email):
        if Sindico.query.filter_by(email=email.data).first():
            raise ValidationError('Este e-mail já esta cadastrado!')  


class LoginSindico(Form):
   usuario = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
   password = PasswordField('',[validators.DataRequired()])

   