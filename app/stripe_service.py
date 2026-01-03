import stripe

stripe.api_key = "SUA_SECRET_KEY"

PLANOS = {
    "parceiro": "price_297",
    "elite": "price_397",
    "premium": "price_597"
}

def criar_checkout(customer_email, plano):
    session = stripe.checkout.Session.create(
        payment_method_types=["card", "pix"],
        mode="subscription",
        customer_email=customer_email,
        line_items=[{"price": PLANOS[plano], "quantity": 1}],
        success_url="https://alugafacilhub.com/sucesso",
        cancel_url="https://alugafacilhub.com/cancelado"
    )
    return session.url
