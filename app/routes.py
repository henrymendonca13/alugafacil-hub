from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Parceiro, Imovel
from .database import db

routes = Blueprint("routes", __name__)

@routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        parceiro = Parceiro.query.filter_by(email=email).first()
        if parceiro and check_password_hash(parceiro.senha_hash, senha):
            session["parceiro_id"] = parceiro.id
            return redirect("/dashboard")

        return render_template("login.html", erro="Login inválido")

    return render_template("login.html")


@routes.route("/logout")
def logout():
    session.clear()
    return redirect("/")
