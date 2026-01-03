@routes.route("/dashboard/imovel/novo", methods=["GET", "POST"])
def cadastrar_imovel():
    if "parceiro_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        eventos = ",".join(request.form.getlist("eventos"))

        imovel = Imovel(
            parceiro_id=session["parceiro_id"],
            titulo=request.form["titulo"],
            tipo=request.form["tipo"],
            quartos=request.form["quartos"],
            suites=request.form["suites"],
            vagas=request.form["vagas"],
            metros=request.form["metros"],
            aluguel=request.form["aluguel"],
            condominio=request.form["condominio"],
            iptu=request.form["iptu"],
            eventos=eventos
        )
        db.session.add(imovel)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("cadastrar_imovel.html", eventos=EVENTOS)
