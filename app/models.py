from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int

class Venta(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    total: float

class Caja(BaseModel):
    id: int
    saldo_inicial: float
    saldo_actual: float

class Usuario(BaseModel):
    id: int
    nombre: str
    rol: str