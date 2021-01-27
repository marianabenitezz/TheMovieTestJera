from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def logar():
    return render_template("login.html")


@app.route("/cadastro")
def cadastrar():
    return render_template("cadastro.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/perfis")
def perfis():
    return render_template("perfis.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


# @app.route("/teste", methods=['GET])
# def teste():
#     return "teste"
