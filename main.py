from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import producto, venta, caja, usuario
import os

app = FastAPI()

origins = os.environ.get("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(producto.router)
app.include_router(venta.router)
app.include_router(caja.router)
app.include_router(usuario.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}