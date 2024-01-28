from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import update_delivery, get_deliveries,get_delivery,delete_delivery,create_delivery
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/deliveries/")
def create_delivery(delivery_data: dict, db: Session = Depends(get_db)):
    return create_delivery(db, delivery_data)

@router.get("/deliveries/")
def read_deliveries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_deliveries(db, skip=skip, limit=limit)

@router.get("/deliveries/{delivery_id}")
def read_delivery(delivery_id: int, db: Session = Depends(get_db)):
    return get_delivery(db, delivery_id)

@router.put("/deliveries/{delivery_id}")
def update_delivery(delivery_id: int, delivery_data: dict, db: Session = Depends(get_db)):
    return update_delivery(db, delivery_id, delivery_data)

@router.delete("/deliveries/{delivery_id}")
def delete_delivery(delivery_id: int, db: Session = Depends(get_db)):
    return delete_delivery(db, delivery_id)
