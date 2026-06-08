from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

productos_db = []

@router.get("/producto", response_model=List[Producto])
def get_productos():
    return productos_db

@router.post("/producto", response_model=Producto)
def add_producto(producto: Producto):
    producto.id = len(productos_db) + 1
    productos_db.append(producto)
    return producto
