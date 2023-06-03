from sqlalchemy.orm import Session

from app.models.clients import ClientModel
from app.schemas.clients import ClientBase

def data_format(db_client):
    data = {
        "nombre_cliente": {
            "nombre": db_client.nombre,
            "apellido": db_client.apellido
        },
        "telefono": db_client.telefono,
        "edad": db_client.edad
    }
    return data

def validate_client(db: Session, cellphone: str):
    db_client = db.query(ClientModel).filter(ClientModel.telefono == cellphone).first()
    if db_client:
        return db_client
    return None

def get_clients(db: Session):
    total_clients = []
    db_clients = db.query(ClientModel).all()
    for client in db_clients:
        total_clients.append(data_format(client))
    return total_clients

def get_client(db: Session, cellphone: str):
    db_client = validate_client(db, cellphone)
    if not db_client:
        return None
    data = data_format(db_client)
    return data

def create_client(db: Session,  cellphone: str, client: ClientBase):
    db_client = validate_client(db, cellphone)
    if db_client:
        return None
    
    db_client = ClientModel(
        nombre=client.nombre_cliente.nombre,
        apellido=client.nombre_cliente.apellido,
        telefono=client.telefono,
        edad=client.edad
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    data = data_format(db_client)
    return data

def update_client(db: Session, cellphone: str, client: ClientBase):
    db_client = validate_client(db, cellphone)

    if not db_client:
        return None
    client_data = client.dict()
    if client_data['nombre_cliente'] != None:
        client_data.update(**client_data['nombre_cliente'])
    del client_data['nombre_cliente']

    for var, value in client_data.items():
        setattr(db_client, var, value) if value or str(value) == 'False' else None

    db.commit()
    db.refresh(db_client)
    data = data_format(db_client)
    return data

def delete_client(db: Session, cellphone: str):
    db_client = validate_client(db, cellphone)
    if not db_client:
        return None
    db.delete(db_client)
    db.commit()
    return {"message": "El cliente ha sido eliminado"}
