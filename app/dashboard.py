@routes.route("/dashboard")
def dashboard():
    if "parceiro_id" not in session:
        return redirect("/login")

    parceiro = Parceiro.query.get(session["parceiro_id"])
    imoveis = Imovel.query.filter_by(parceiro_id=parceiro.id).all()

    return render_template(
        "dashboard.html",
        parceiro=parceiro,
        imoveis=imoveis
    )
