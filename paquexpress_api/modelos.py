from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, DECIMAL, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from bd import Base

class Agente(Base):
    __tablename__ = "Agentes"
    id_agente = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    hash_contrasena = Column(String(255), nullable=False)
    nombre_completo = Column(String(100))
    creado_en = Column(TIMESTAMP, default=datetime.utcnow)
    paquetes = relationship("Paquete", back_populates="agente")

class Paquete(Base):
    __tablename__ = "Paquetes"
    id_paquete = Column(Integer, primary_key=True, index=True)
    id_unico_rastreo = Column(String(50), unique=True, nullable=False)
    direccion_destino = Column(String(255), nullable=False)
    id_agente_asignado = Column(Integer, ForeignKey("Agentes.id_agente"))
    estado = Column(Enum('ASIGNADO', 'EN_RUTA', 'ENTREGADO'), default='ASIGNADO')
    agente = relationship("Agente", back_populates="paquetes")
    entrega = relationship("Entrega", back_populates="paquete", uselist=False)

class Entrega(Base):
    __tablename__ = "Entregas"
    id_entrega = Column(Integer, primary_key=True, index=True)
    id_paquete = Column(Integer, ForeignKey("Paquetes.id_paquete"), unique=True, nullable=False)
    id_agente = Column(Integer, ForeignKey("Agentes.id_agente"))
    latitud = Column(DECIMAL(10, 8), nullable=False)
    longitud = Column(DECIMAL(11, 8), nullable=False)
    ruta_foto_evidencia = Column(String(255), nullable=False)
    fecha_hora = Column(TIMESTAMP, default=datetime.utcnow)
    paquete = relationship("Paquete", back_populates="entrega")