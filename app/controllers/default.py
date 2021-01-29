from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app, db, login_manager

from app.models.tables import Conta, Filme, Perfis
from app.models.forms import LoginForm, CadastroForm, BuscaForm, PerfilForm
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
            flash("Login inválido. Cadastre-se ou tente novamente!")

    return render_template("login.html", form=form)


@app.route("/perfis", methods=["GET", "POST"])
def perfis():
    if current_user.is_authenticated:
        form = PerfilForm()
        todos = listarPerfis(current_user.id)
        if form.validate_on_submit():
            if len(todos) >= 4:
                flash("Limite máximo de perfis atingido!")
                print("Atingiu o limite")

            else:
                novoPerfil = Perfis(current_user.id, form.nome.data,
                                    form.filmes.data)
                db.session.add(novoPerfil)
                db.session.commit()
                todos = listarPerfis(current_user.id)
                print("SUCESSO!", novoPerfil.nome)
        else:
            print("Erro ao adicionar")

        return render_template("perfis.html", form=form, todos=todos)

    else:
        flash("Faça login para acessar seu perfil!")
        return redirect(url_for("logar"))


def listarPerfis(comparacao):
    todos = []
    for instancia in db.session.query(Perfis).filter_by(contaId=comparacao):
        todos.append(instancia)
    return todos


@app.route("/perfil")
def perfil():
    if current_user.is_authenticated:
        form = BuscaForm()
        filmes = []
        if form.validate_on_submit():
            filmes = api.buscarFilme(form.filme.data)
        else:
            print("Erro ao buscar")
        return render_template("perfil.html", form=form, filmes=filmes)
    else:
        flash("Faça login para acessar seu perfil!")
        return redirect(url_for("logar"))


@app.route("/logout")
def deslogar():
    logout_user()
    flash("Deslogado")
    return redirect(url_for("index"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    form = CadastroForm()
    if form.validate_on_submit():
        e = Conta.query.filter_by(email=form.email.data).first()
        if e:
            flash("Já existe uma conta neste e-mail. Utilize outro!")
        else:
            conta = Conta(form.nome.data, form.email.data, form.dataNasc.data,
                          form.senha.data)
            db.session.add(conta)
            db.session.commit()
            flash("Cadastrado com sucesso!")
            return redirect(url_for("logar"))
    else:
        flash("Dados inválidos!")
        print("Erro ao preencher dados")

    return render_template("cadastro.html", form=form)


@app.route("/home")
def home():
    return render_template("home.html")
