from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import autenticacion, entrega
from bd import Base, motor

Base.metadata.create_all(bind=motor)

app = FastAPI(title="API Paquexpress")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/subidas", StaticFiles(directory="uploads"), name="subidas")
app.include_router(autenticacion.router, prefix="/auth")
app.include_router(entrega.router)

@app.get("/")
def leer_raiz():
    return {"mensaje": "API Paquexpress Operativa"}