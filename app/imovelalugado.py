@routes.route("/dashboard/imovel/<int:id>/alugado")
def marcar_alugado(id):
    if "parceiro_id" not in session:
        return redirect("/login")

    imovel = Imovel.query.get_or_404(id)
    if imovel.parceiro_id == session["parceiro_id"]:
        imovel.status = "alugado"
        db.session.commit()

    return redirect("/dashboard")
