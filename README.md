ANtes de tudo é necessário possuir o banco de dados postgreSQL e Python 3.4.2(ou superior) instalados em seu ambiente. 
A versão do postgreSQL utilizada neste projeto é a 8.4.22.
Com o postgreSQL instalado, utilize o comando

$ sudo su - postgres

Crie um banco de dados da seguinte forma:

$ createdb mainbd

Se tal banco de dados já existir, utilize

$ dropdb mydb

e tente criá-lo novamente.
Outra opção é utilizar um banco de dados de sua escolha e alterar o arquivo settings.py do projeto para ser coerente com suas configurações preferidas de banco.

Após o download do código fonte ($ git clone https://github.com/Biazus/teleconsultoria.git), é necessário resolver as dependências do projeto.
Como sugestão, utilize <b>virtualenv</b> para isolar seu ambiente de trabalho:

$ virtualenv -p python3.4 ENV
$ source ./ENV/bin/activate

Para instalar dependências do projeto utilizando pip, é necessário executar o comando abaixo:

$ pip install -r requirements.txt

Caso prefira, as dependências podem ser instaladas manualmente utilizando-se 

$ apt-get install {{nome-e-versao-da-dependencia}}

Apoś, rode o código utilizando os comandos a seguir:

$ python manage.py migrate
$ python manage.py runserver

Acesse: 

http://127.0.0.1:8000/core/

