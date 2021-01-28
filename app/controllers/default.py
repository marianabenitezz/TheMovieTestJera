from flask import render_template
from app import app, db

from app.models.tables import Conta

from app.models.forms import LoginForm
from app.models.forms import CadastroForm


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def logar():
    form = LoginForm()
    if form.validate_on_submit():
        conta = Conta.query.filter_by(email=form.email.data).first()
        if (conta.senha == form.senha.data):
            return "Encontrou %r e senha %r" % (conta.email, conta.senha)
    else:
        print(form.errors)

    return render_template("login.html", form=form)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    form = CadastroForm()
    if form.validate_on_submit():
        conta = Conta(form.nome.data, form.email.data, form.dataNasc.data,
                      form.senha.data)
        db.session.add(conta)
        db.session.commit()

    else:
        print(form.errors)

    return render_template("cadastro.html", form=form)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/perfis")
def perfis():
    return render_template("perfis.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")