from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ModeloIngreso(BaseModel):
    nombre_usuario: str
    contrasena: str

class ModeloRegistro(BaseModel):
    nombre_usuario: str
    contrasena: str
    nombre_completo: str

class PaqueteBase(BaseModel):
    id_paquete: int
    id_unico_rastreo: str
    direccion_destino: str
    estado: str
    class Config:
        from_attributes = True

class RespuestaEntrega(BaseModel):
    id_entrega: int
    id_paquete: int
    ruta_foto_evidencia: str
    fecha_hora: Optional[datetime]
    latitud: float
    longitud: float
    class Config:
        from_attributes = True