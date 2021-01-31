No CMD do Windows:

1) ** Instalar o Python **
2) ** Instalar o pip **

3) ** Criar o ambiente virtual: **
	$ pip install virtualenv
	$ virtualenv 'nome_da_virtualenv'
	2.1)** achar o arquivo 'activate' (/TheMovieTestJera/venv/scripts/)**
		$ cd venv/scripts/  
		$ activate

4) Voltar para a pasta do projeto (/TheMovieTestJera/)
		$ cd..
		$ cd..

5) ** Instalando as dependências: **
	$ pip install -r requirements.txt 

6) ** Gerando o Banco de dados: **
	$ python run.py db init
	$ python run.py db migrate
	$ python run.py db upgrade

7) ** executando aplicação **
	$ python run.py runserver
