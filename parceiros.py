from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from app.database import SessionLocal
from app.models import Parceiro
from app.auth import hash_password, create_token
from app.stripe_service import criar_checkout

router = APIRouter()

@router.get("/cadastro")
def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post("/cadastro")
def criar_parceiro(
    nome_responsavel: str = Form(...),
    nome_imobiliaria: str = Form(...),
    creci: str = Form(...),
    cpf_cnpj: str = Form(...),
    cidade: str = Form(...),
    whatsapp: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    plano: str = Form(...)
):
    db = SessionLocal()

    parceiro = Parceiro(
        nome_responsavel=nome_responsavel,
        nome_imobiliaria=nome_imobiliaria,
        creci=creci,
        cpf_cnpj=cpf_cnpj,
        cidade=cidade,
        whatsapp=whatsapp,
        email=email,
        senha=hash_password(senha),
        plano=plano
    )

    db.add(parceiro)
    db.commit()
    db.refresh(parceiro)

    checkout = criar_checkout(plano)
    return RedirectResponse(checkout, status_code=303)
