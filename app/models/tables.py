from app import db, login_manager
from datetime import datetime


class Conta(db.Model):
    __tablename__: "conta"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    dataNasc = db.Column(db.String)
    senha = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, nome, email, dataNasc, senha):
        self.nome = nome
        self.email = email
        self.dataNasc = dataNasc
        self.senha = senha

    def __repr__(self):
        return "<Usuario: %r , email: %r>" % (self.nome, self.email)


class Filme(db.Model):
    __tablename__: "filmes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    genero = db.Column(db.String)
    descricao = db.Column(db.Text)

    def __init__(self, id, nome, genero, descricao):
        self.nome = nome
        self.genero = genero
        self.descricao = descricao

    def __repr__(self):
        return "<Filme %r>" % self.nome


class Perfis(db.Model):
    __tablename__: "perfis"
    id = db.Column(db.Integer, primary_key=True)
    conta = db.Column(db.Integer, db.ForeignKey('conta.id'))
    nome = db.Column(db.String)
    filmes = db.Column(db.String, db.ForeignKey('filme.id'))

    def __init__(self, conta, nome, filmes):
        self.conta = conta
        self.nome = nome
        self.filmes = filmes

    def __repr__(self):
        return "<perfis %r>" % self.filmes