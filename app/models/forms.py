from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, DateField


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class CadastroForm(Form):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('Email Address',
                       [validators.DataRequired(),
                        validators.Email()])
    dataNasc = DateField('dataNasc', format='%Y-%m-%d')
    senha = PasswordField('senha', [
        validators.DataRequired(),
        validators.Length(min=6,
                          message="Senhas devem ter no mínimo 6 caracteres"),
        validators.EqualTo('confirmacao', message="Senhas não correspondem"),
    ])
    confirmacao = PasswordField('confirmacao')


class BuscaFilmeForm(Form):
    filme = StringField('filme', validators=[DataRequired()])


class AssistirForm(Form):
    contaId = StringField('contaId', validators=[DataRequired()])
    perfilId = StringField('perfilId', validators=[DataRequired()])
    filmeId = StringField('filmeId', validators=[DataRequired()])
    filmeNome = StringField('filmeNome', validators=[DataRequired()])
    media = StringField('media', validators=[DataRequired()])


class PerfilForm(Form):
    nome = StringField('nome', validators=[DataRequired()])
    contaId = StringField('contaId')
    filmes = StringField('filmes')
