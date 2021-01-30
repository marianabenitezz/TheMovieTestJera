from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app, db, login_manager

from app.models.tables import Conta, Filme, Perfis
from app.models.forms import LoginForm, CadastroForm, BuscaFilmeForm, PerfilForm, AssistirForm
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


@app.route("/perfil/<string:idPerfil>/<string:nomePerfil>",
           methods=['GET', 'POST'])
def perfil(idPerfil, nomePerfil):
    if current_user.is_authenticated:
        buscaFilmeForm = BuscaFilmeForm()
        assistirForm = AssistirForm()
        filmes = []
        paraAssistir = listarFilmesParaAssistir(current_user.id, idPerfil)
        sugestoes = api.buscarFilmesMaisPopulares()

        if buscaFilmeForm.validate_on_submit():
            filmes = api.buscarFilme(buscaFilmeForm.filme.data)

        if paraAssistir != []:
            sugestoes = api.buscarFilmeSimilar(str(paraAssistir[-1].filmeId))

        return render_template("perfil.html",
                               buscaFilmeForm=buscaFilmeForm,
                               filmes=filmes,
                               nomePerfil=nomePerfil,
                               idUser=current_user.id,
                               idPerfil=idPerfil,
                               paraAssistir=paraAssistir,
                               sugestoes=sugestoes)
    else:
        flash("Faça login para acessar seu perfil!")
        return redirect(url_for("logar"))


def listarFilmesParaAssistir(idConta, idPerfil):
    todos = []
    filmesDoPerfil = db.session.query(Filme).filter_by(contaId=idConta,
                                                       perfilId=idPerfil)
    if filmesDoPerfil:
        for instancia in filmesDoPerfil:
            todos.append(instancia)

    return todos


@app.route(
    "/adicionarParaAssistir/<contaId>/<perfilId>/<filmeId>/<filmeNome>/<media>/<nomePerfil>",
    methods=["GET", "POST"])
def adicionarParaAssistir(contaId, perfilId, filmeId, filmeNome, media,
                          nomePerfil):

    listaParaAssistir = listarFilmesParaAssistir(contaId, perfilId)

    lista = []
    for i in range(len(listaParaAssistir)):
        lista.append(listaParaAssistir[i].filmeId)

    if filmeId not in lista:
        filme = Filme(contaId, perfilId, filmeId, filmeNome, media)
        db.session.add(filme)
        db.session.commit()
    else:
        flash("Este filme já está na WatchList")

    return redirect(url_for('perfil', idPerfil=perfilId,
                            nomePerfil=nomePerfil))


@app.route("/logout")
def deslogar():
    logout_user()
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
        print("Não preencheu os dados")

    return render_template("cadastro.html", form=form)


@app.route("/home")
def home():
    return render_template("home.html")
