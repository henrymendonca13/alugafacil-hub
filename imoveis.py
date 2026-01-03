from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.database import SessionLocal
from app.models import Imovel

router = APIRouter()

@router.post("/imovel/novo")
def novo_imovel(
    tipo: str = Form(...),
    quartos: int = Form(...),
    suites: int = Form(...),
    garagem: int = Form(...),
    area: float = Form(...),
    aluguel: float = Form(...),
    eventos: list = Form([])
):
    db = SessionLocal()

    imovel = Imovel(
        tipo=tipo,
        quartos=quartos,
        suites=suites,
        garagem=garagem,
        area=area,
        aluguel=aluguel,
        eventos=",".join(eventos)
    )

    db.add(imovel)
    db.commit()

    return RedirectResponse("/painel", status_code=303)
