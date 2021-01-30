from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class CadastroForm(Form):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    # dataNasc = DateTimeLocalField('dataNasc',
    #                               format="%Y-%m-%dT%H:%M:%S",
    #                               default=datetime.today(),
    #                               validators=[DataRequired()])
    dataNasc = StringField('dataNasc', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class BuscaForm(Form):
    filme = StringField('filme', validators=[DataRequired()])


class PerfilForm(Form):
    nome = StringField('nome', validators=[DataRequired()])
    contaId = StringField('contaId')
    filmes = StringField('filmes')
