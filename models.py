from flask_login import UserMixin
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    creci = db.Column(db.String(50), nullable=False)
    documento = db.Column(db.String(50), nullable=False)

    properties = db.relationship('Property', backref='owner', lazy=True)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120))
    cidade = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    quartos = db.Column(db.Integer)
    suites = db.Column(db.Integer)
    garagem = db.Column(db.Integer)
    metragem = db.Column(db.Integer)
    condominio = db.Column(db.Float)
    iptu = db.Column(db.Float)
    status = db.Column(db.String(20), default='disponivel')

    eventos = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
