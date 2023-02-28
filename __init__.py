from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

#configuracao de string de acesso ao banco de dados
# a estrutura deve ser: app.config['SQLALCHEMY_DATABASE_URI'] = '(banco de dados utilizado:mysql, postgrees,oracle)://(usuario):(senha)@(host do banco de dados)/(banco)'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/teste'
app.config['SECRET_KEY'] = 'rob@task'
app.config['SQLACHEMY_TRACK_MODIFICARIONS']=False

login_manager = LoginManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
