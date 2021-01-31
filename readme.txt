*No terminal do seu computador*

1) Atualizar ou Instalar o Python 3.9.1
2) Instalar o pip  
	obs* Se precisar atualizar o pip:
		- achar o caminho do 'python.exe' 
		$ python.exe -m pip install --upgrade pip

3) Criar o ambiente virtual:
	$ pip install virtualenv (caso o pip não funcione, tente instalar o pip3)
	$ virtualenv venv
	
4) Achar o arquivo 'activate' 
	4.1- Se estiver no Windows: 
		$ cd /venv/scripts/
		$ activate

	4.2- Se estiver no Linux:
		$ source /venv/bin/activate

5) Voltar para a pasta do projeto (/TheMovieTestJera/)
		$ cd..
		$ cd..

6) Instalando as dependências:
	$ pip install -r requirements.txt 

7) Gerando o Banco de dados:
	$ python run.py db init
	$ python run.py db migrate
	$ python run.py db upgrade

8) Executando a aplicação:
	$ python run.py runserver

9) Abrir no navegador:
	localhost:'numero da porta'/