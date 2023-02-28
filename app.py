from flask import render_template,request,redirect,url_for,jsonify
from flask_migrate import Migrate
from app import app,db
from app.models import User, user_share_schema, users_share_schema
from flask_login import login_user,logout_user,current_user
import datetime
import jwt
import json
from app.autenticate import jwt_required

Migrate(app,db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )
#rota de registro em flask

@app.route('/')
def teste():
    logout_user()
    return render_template('index.html')

@app.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    return redirect(url_for("login"))


@app.route('/register',methods=['GET','POST'])
def register():
    #TODO - verifica a autenticação e registra o usuario ao banco de dados
    if request.method == 'POST':
        name = request.form['nome']
        email = request.form['email']
        pwd = request.form['pass']
        if name and email and pwd:
            user = User(name,email,pwd)
            db.session.add(user)
            db.session.commit()
    return render_template('register.html')


@app.route('/login')
def login():
    #TODO - realiza a verificação do metodo, autentica o usuario e o loga
#if request.method == 'POST':
#email = request.form['email']
#pwd = request.form['pass']

#user = User.query.filter_by(email=email).first()

#if not user or not user.verify_password(pwd):
    #return redirect(url_for('login'))

#login_user(user)
        logout_user()
        return render_template("index.html")
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/auth/register',methods=['POST'])
def registro():
        dados = request.get_data().decode()
        dados = json.loads(dados)
        nome = dados['username']
        email = dados['email']
        password = dados['password']
        user = User(nome,email,password)

        db.session.add(user)
        db.session.commit()

        result = user_share_schema.dump(user.query.filter_by(email = email).first())

        
        return jsonify(result)

@app.route('/auth/login',methods=['POST'])
def authlogin():
        dados = request.get_data().decode()
        dados = json.loads(dados)
        email = dados['email']
        password = dados['password']

        user = User.query.filter_by(email=email).first_or_404()

        if not user.verify_password(password):
            logout_user()
            return jsonify({
                "error":"credenciais incorretas"
            }), 403
        
        payload = {
            "id" : user.id,
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 10)

        }
        token = jwt.encode(payload, app.config['SECRET_KEY'],algorithm="HS256")

        if user.verify_password(password):
            login_user(user)
        
        return jsonify({'token':token})

@app.route('/auth/protected')
@jwt_required
def protected(current_user):
    result = users_share_schema.dump(
        User.query.all()
    )
    return jsonify(result)

app.run(debug=True)
