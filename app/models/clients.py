from sqlalchemy import Column, String, SmallInteger

from app.database.database import Base

class ClientModel(Base):
    __tablename__ = "clientes"

    telefono = Column(String(length=10), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    edad = Column(SmallInteger)
