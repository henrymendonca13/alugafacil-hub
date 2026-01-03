from app.database import db
from app.models import Parceiro
from werkzeug.security import generate_password_hash
from app.main import app

with app.app_context():
    parceiro = Parceiro(
        nome="Imobiliária Teste",
        email="teste@alugafacil.com",
        senha_hash=generate_password_hash("123456"),
        cidade="Rio de Janeiro",
        status="ativo"
    )
    db.session.add(parceiro)
    db.session.commit()

    print("Parceiro criado com sucesso!")
