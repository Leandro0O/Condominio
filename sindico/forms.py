from wtforms import Form, StringField, PasswordField, validators, ValidationError

class CadastroSindico(Form):
    nome = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
    usuario = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
    email = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
    tel = StringField('', [validators.length(min=1, max=20), validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired(), validators.EqualTo('confirm', message='As senhas devem ser iguais!')])
    confirm = PasswordField('')

class LoginSindico(Form):
   usuario = StringField('', [validators.length(min=1, max=45), validators.DataRequired()])
   password = PasswordField('', validators.DataRequired)

   