from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib
from bd import obtener_bd
from modelos import Agente
from esquemas import ModeloIngreso, ModeloRegistro

router = APIRouter(tags=["Autenticacion"])

def hash_md5(contrasena: str) -> str:
    return hashlib.md5(contrasena.encode()).hexdigest()

@router.post("/registrar/")
def registrar(datos: ModeloRegistro, bd: Session = Depends(obtener_bd)):
    hash_c = hash_md5(datos.contrasena)
    agente = Agente(nombre_usuario=datos.nombre_usuario, hash_contrasena=hash_c, nombre_completo=datos.nombre_completo)
    bd.add(agente)
    bd.commit()
    bd.refresh(agente)
    return {"msg": "Agente registrado", "id_agente": agente.id_agente}

@router.post("/ingresar/")
def ingresar(datos: ModeloIngreso, bd: Session = Depends(obtener_bd)):
    agente = bd.query(Agente).filter(Agente.nombre_usuario == datos.nombre_usuario).first()
    if not agente or agente.hash_contrasena != hash_md5(datos.contrasena):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    return {"msg": "Ingreso exitoso", "id_agente": agente.id_agente}