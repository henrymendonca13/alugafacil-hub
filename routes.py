from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Property
from app import db

main = Blueprint('main', __name__)

CIDADES = [
    "Magé",
    "Guapimirim",
    "Teresópolis",
    "Petrópolis",
    "Nova Friburgo"
]

EVENTOS = [
    "Aluga Day",
    "Black Aluga",
    "Aluga Week",
    "Summer Aluga",
    "Winter Aluga"
]

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            nome=request.form["nome"],
            email=request.form["email"],
            creci=request.form["creci"],
            documento=request.form["documento"],
            senha=generate_password_hash(request.form["senha"])
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))

    return render_template("register.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and check_password_hash(user.senha, request.form["senha"]):
            login_user(user)
            return redirect(url_for("main.dashboard"))

    return render_template("login.html")

@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", properties=current_user.properties)

@main.route("/add-property", methods=["GET", "POST"])
@login_required
def add_property():
    if request.method == "POST":
        eventos = ",".join(request.form.getlist("eventos"))

        prop = Property(
            titulo=request.form["titulo"],
            cidade=request.form["cidade"],
            tipo=request.form["tipo"],
            quartos=request.form["quartos"],
            suites=request.form["suites"],
            garagem=request.form["garagem"],
            metragem=request.form["metragem"],
            condominio=request.form["condominio"],
            iptu=request.form["iptu"],
            eventos=eventos,
            owner=current_user
        )
        db.session.add(prop)
        db.session.commit()
        return redirect(url_for("main.dashboard"))

    return render_template(
        "add_property.html",
        cidades=CIDADES,
        eventos=EVENTOS
    )

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
