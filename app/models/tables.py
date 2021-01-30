from app import db, login_manager
import datetime


class Conta(db.Model):  #conta de usuários
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


class Perfis(db.Model):
    __tablename__: "perfis"
    id = db.Column(db.Integer, primary_key=True)
    contaId = db.Column(db.Integer)
    nome = db.Column(db.String)
    filmes = db.Column(db.PickleType)  #representam os filmes para assistir

    def __init__(self, contaId, nome, filmes):
        self.contaId = contaId
        self.nome = nome
        self.filmes = filmes

    def __repr__(self):
        return "<ContaID %r, Nome %r, Filmes %r>" % (self.contaId, self.nome,
                                                     self.filmes)


class Filme(db.Model):
    __tablename__: "filmes"
    id = db.Column(db.Integer, primary_key=True)
    contaId = db.Column(db.Integer)
    perfilId = db.Column(db.Integer)
    filmeId = db.Column(db.Integer)
    filmeNome = db.Column(db.String)
    media = db.Column(db.String)

    def __init__(self, contaId, perfilId, filmeId, filmeNome, media):
        self.contaId = contaId
        self.perfilId = perfilId
        self.filmeId = filmeId
        self.filmeNome = filmeNome
        self.media = media

    def __repr__(self):
        return "<ContaID: %r, PerfilID: %r, FilmeID: %r,  FilmeNome: %r, Media: %r>" % (
            self.contaId, self.perfilId, self.filmeId, self.filmeNome,
            self.media)
