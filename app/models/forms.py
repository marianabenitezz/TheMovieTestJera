from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
import requests
import json


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class CadastroForm(Form):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    dataNasc = StringField('dataNasc', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class BuscaForm(Form):
    filme = StringField('filme')


class PerfilForm(Form):
    nome = StringField('nome')
    idUsuario = StringField('idUsuario')
    filmes = StringField('filmes')