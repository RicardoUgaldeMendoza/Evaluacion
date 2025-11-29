import os
import shutil
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from bd import obtener_bd
from modelos import Paquete, Entrega
from esquemas import PaqueteBase, RespuestaEntrega

router = APIRouter(tags=["Entrega"])

CARPETA_SUBIDAS = "uploads"
os.makedirs(CARPETA_SUBIDAS, exist_ok=True)

@router.get("/paquetes/{id_agente}", response_model=list[PaqueteBase])
def obtener_paquetes_asignados(id_agente: int, bd: Session = Depends(obtener_bd)):
    paquetes = (
        bd.query(Paquete)
        .filter(Paquete.id_agente_asignado == id_agente)
        .filter(Paquete.estado.in_(['ASIGNADO', 'EN_RUTA']))
        .all()
    )
    return paquetes

@router.post("/registrar_entrega/", response_model=RespuestaEntrega)
async def registrar_entrega(
    id_agente: int = Form(...),
    id_paquete: int = Form(...),
    latitud: float = Form(...),
    longitud: float = Form(...),
    archivo: UploadFile = File(...),
    bd: Session = Depends(obtener_bd)
):
    paquete = bd.query(Paquete).filter(Paquete.id_paquete == id_paquete).first()
    if not paquete:
        raise HTTPException(status_code=404, detail="Paquete no encontrado")
    if paquete.estado == 'ENTREGADO':
        raise HTTPException(status_code=400, detail="El paquete ya fue entregado")

    ruta = ""
    try:
        extension_archivo = os.path.splitext(archivo.filename)[1]
        nuevo_nombre_archivo = f"evidencia_{id_paquete}_{id_agente}_{int(os.times()[4])}{extension_archivo}"
        ruta = os.path.join(CARPETA_SUBIDAS, nuevo_nombre_archivo)

        with open(ruta, "wb") as buffer:
            shutil.copyfileobj(archivo.file, buffer)

        nueva_entrega = Entrega(
            id_paquete=id_paquete,
            id_agente=id_agente,
            latitud=latitud,
            longitud=longitud,
            ruta_foto_evidencia=ruta,
        )
        bd.add(nueva_entrega)
        paquete.estado = 'ENTREGADO'
        bd.commit()
        bd.refresh(nueva_entrega)
        return nueva_entrega

    except Exception as e:
        bd.rollback()
        if os.path.exists(ruta):
            os.remove(ruta)
        raise HTTPException(status_code=500, detail=f"Error al registrar: {str(e)}")