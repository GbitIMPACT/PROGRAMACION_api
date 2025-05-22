from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Trabajador(Base):
    __tablename__ = "trabajadores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    # Puedes agregar más campos si lo deseas

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    cantidad = Column(Integer)
    precio = Column(Integer)
    unidad_medida = Column(String(50))
    trabajador_id = Column(Integer, ForeignKey("trabajadores.id"))
    trabajador = relationship("Trabajador")