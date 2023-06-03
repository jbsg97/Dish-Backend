from pydantic import BaseModel, Field, validator
from typing import Optional

class ClientName(BaseModel):
    nombre: str
    apellido: str


class ClientNameUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]


class ClientBase(BaseModel):
    telefono: str
    edad: int
    nombre_cliente: ClientName


class ClientCreate(BaseModel):
    nombre_cliente: ClientName
    telefono: str = Field(description="El numero debe ser de 10 digitos.", min_length=10, max_length=10)
    edad: int = Field(ge=18, description="Debes ser mayor de edad para registrarte.")

    @validator("telefono", always=True)
    def check_storage_type(cls, value):
        if not value.isdigit():
            raise ValueError("Ingrese solamente numeros.")
        return value

    class Config:
        orm_mode = True


class ClientUpdate(BaseModel):
    nombre_cliente: Optional[ClientNameUpdate]
    edad: Optional[int] = Field(ge=18, description="La edad debe ser mayor a 18.")
