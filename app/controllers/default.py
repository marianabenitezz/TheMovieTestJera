from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login_manager

from app.models.tables import Conta, Filme
from app.models.forms import LoginForm, CadastroForm, BuscaForm
from app.controllers import api

import sys


@login_manager.user_loader
def load_user(id):
    return Conta.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def logar():
    form = LoginForm()
    if form.validate_on_submit():
        conta = Conta.query.filter_by(email=form.email.data).first()
        if conta and conta.senha == form.senha.data:
            login_user(conta)
            return redirect(url_for("perfis"))
            flash("Logado")
        else:
            flash("Login inválido")

    return render_template("login.html", form=form)


@app.route("/perfis", methods=["GET", "POST"])
def perfis():
    form = BuscaForm()
    if form.validate_on_submit():
        filmes = api.buscarFilme(form.filme.data)
        print(filmes[0]['release_date'])
    else:
        print("------------------------ERRO------------------------")

    return render_template("perfis.html", form=form)


@app.route("/logout")
def deslogar():
    logout_user()
    flash("Deslogado")
    return redirect(url_for("index"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    form = CadastroForm()
    if form.validate_on_submit():
        conta = Conta(form.nome.data, form.email.data, form.dataNasc.data,
                      form.senha.data)
        db.session.add(conta)
        db.session.commit()
    else:
        print("ERROOOO")

    return render_template("cadastro.html", form=form)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")
