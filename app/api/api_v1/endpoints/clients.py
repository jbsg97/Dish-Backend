from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.clients import ClientBase, ClientUpdate, ClientCreate
from app.crud import clients
from typing import List

router = APIRouter()

@router.get("", response_model=List[ClientBase])
def get_clients(db: Session = Depends(deps.get_db)):
    db_client = clients.get_clients(db)
    if not db_client:
        raise HTTPException(status_code=400, detail="No existen clientes.")
    return db_client


@router.get("/{cellphone}", response_model=ClientBase)
def get_clients(cellphone: str, db: Session = Depends(deps.get_db)):
    db_client = clients.get_client(db, cellphone)
    if not db_client:
        raise HTTPException(status_code=400, detail="El cliente no existe.")
    return db_client


@router.post("", response_model=ClientBase, status_code=201)
def create_client(client: ClientCreate, db: Session = Depends(deps.get_db)):
    created_client = clients.create_client(db, client.telefono, client=client)
    if not created_client:
        raise HTTPException(status_code=400, detail="El telefono ya ha sido registrado.")
    return created_client


@router.put("/{cellphone}", response_model=ClientBase)
def update_client(cellphone: str, client: ClientUpdate, db: Session = Depends(deps.get_db)):
    updated_client = clients.update_client(db, cellphone, client)
    if not updated_client:
        raise HTTPException(status_code=400, detail="El cliente no existe.")
    return updated_client


@router.delete("/{cellphone}")
def delete_client(cellphone: str, db: Session = Depends(deps.get_db)):
    deleted_client = clients.delete_client(db, cellphone)
    if not deleted_client:
        raise HTTPException(status_code=400, detail="El cliente no existe.")
    return deleted_client
