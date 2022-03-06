from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, validators, Form
from .modules import Morador


class RegisterMorador(Form):
    nome = StringField('', [ validators.length(min=4, max=45), validators.DataRequired()])
    usuario = StringField('', [ validators.length(min=4, max=45), validators.DataRequired()])
    email = StringField('', [ validators.length(min=4, max=45), validators.DataRequired()])
    tel = StringField('', [ validators.length(min=4, max=20), validators.DataRequired()])
    bloco = StringField('', [  validators.DataRequired()])
    apto = StringField('', [ validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired(), validators.EqualTo('confirm', message='As senhas devem ser iguais!')])
    confirm = PasswordField('',[ validators.DataRequired()])

    def validate_user(self,usuario):
        if Morador.query.filter_by(usuario=usuario.data).first():
            raise ValidationError('Este usuário já esta em uso')


    def validate_email(self,email):
        if Morador.query.filter_by(email=email.data).first():
            raise ValidationError('Este e-mail já esta em uso')        


class LoginMorador(FlaskForm):
    email = StringField('', [ validators.length(min=4, max=45), validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired()])