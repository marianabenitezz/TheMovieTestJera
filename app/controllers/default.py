from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def logar():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.senha.data)
    else:
        print(form.errors)

    return render_template("login.html",
                            form=form)


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
