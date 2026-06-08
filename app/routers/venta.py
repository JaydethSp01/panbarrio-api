from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Venta(BaseModel):
    id: int
    productoId: int
    cantidad: int

ventas_db = []

@router.get("/venta", response_model=List[Venta])
def get_ventas():
    return ventas_db

@router.post("/venta", response_model=Venta)
def add_venta(venta: Venta):
    venta.id = len(ventas_db) + 1
    ventas_db.append(venta)
    return venta
