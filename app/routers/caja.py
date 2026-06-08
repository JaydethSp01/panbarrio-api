from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Caja(BaseModel):
    id: int
    monto: float

cajas_db = []

@router.get("/caja", response_model=List[Caja])
def get_cajas():
    return cajas_db

@router.post("/caja", response_model=Caja)
def add_caja(caja: Caja):
    caja.id = len(cajas_db) + 1
    cajas_db.append(caja)
    return caja
