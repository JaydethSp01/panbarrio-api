from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

usuarios_db = []

@router.get("/usuario", response_model=List[Usuario])
def get_usuarios():
    return usuarios_db

@router.post("/usuario", response_model=Usuario)
def add_usuario(usuario: Usuario):
    usuario.id = len(usuarios_db) + 1
    usuarios_db.append(usuario)
    return usuario
