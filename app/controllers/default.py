from app import app


@app.route("/")
def index():
    return "index"


@app.route("/login")
def logar():
    return "Login"


@app.route("/cadastro")
def cadastrar():
    return "Cadastro"


@app.route("/home")
def home():
    return "Home"


@app.route("/perfis")
def perfis():
    return "perfis"


@app.route("/perfil")
def perfil():
    return "perfil"
