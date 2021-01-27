from app import db

class Conta(db.Model):
    __tablename__:"conta"
    id = db.Column(db.Integer, primary_key == True)
    senha = = db.Column(db.String)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique == True)
    dataNasc = db.Column(db.DateTime)

    def __init__(self, email, nome, senha, dataNasc):
        self.email = email
        self.nome = nome
        self.senha = senha
        self.dataNasc = dataNasc

    def __repr__(self):
        return "<Usuario: %r , email: %r>" %(self.nome, self.email)


class Perfis(db.Model):
    __tablename__:"perfis"
    id = db.Column(db.Integer, db.ForeignKey('conta.id'))
    nome = db.Column(db.String)
    filmes = db.Column(db.PickleType, db.ForeignKey('filmes.id'))
    #nomeFilme = db.relationship('Filme', foreignKey = filmes)

    def __init__(self, filmes):
        self.filmes = filmes
    
    def __repr__(self):
        return "<perfis %r>" % self.filmes


class Filme(db.Model):
    __tablename__:"filmes"
    id = db.Column(db.Integer, primary_key == True)
    nome = db.Column(db.String)
    genero = db.Column(db.String)
    descricao = db.Column(db.Text)
    
    def __init__(self, id, nome, genero, descricao):
        self.nome = nome
        self.genero = genero
        self.descricao = descricao
    
    def __repr__(self):
        return "<Filme %r>" % self.nome