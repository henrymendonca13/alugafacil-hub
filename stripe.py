def criar_checkout(plano):
    price_map = {
        "parceiro": STRIPE_PRICE_PARCEIRO,
        "elite": STRIPE_PRICE_ELITE,
        "premium": STRIPE_PRICE_PREMIUM
    }

    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{"price": price_map[plano], "quantity": 1}],
        success_url=f"{BASE_URL}/painel",
        cancel_url=f"{BASE_URL}/cadastro"
    )
    return session.url
