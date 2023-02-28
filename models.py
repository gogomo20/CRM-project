from app import db,login_manager,ma
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id = user_id).first()



class User(db.Model,UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True,unique=True)
    nome = db.Column(db.String(84),nullable=False)
    email = db.Column(db.String(84),nullable=False,unique=True)
    senha = db.Column(db.String(128),nullable = False)
    classe = db.Column(db.String(1),nullable = False,server_default = 'F')
    def __init__(self,nome,email,password,classe = "F") -> None:
        self.nome = nome
        self.email  = email
        self.senha = generate_password_hash(password)
        self.classe = classe
    def verify_password(self,pwd):
        return check_password_hash(self.senha,pwd)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','nome','email')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many= True)