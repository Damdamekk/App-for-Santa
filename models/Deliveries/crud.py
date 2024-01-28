
from sqlalchemy.orm import Session
from .Delivery import Delivery

def create_delivery(db: Session, delivery_data: dict):
    db_delivery = Delivery(**delivery_data)
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def get_deliveries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Delivery).offset(skip).limit(limit).all()

def get_delivery(db: Session, delivery_id: int):
    return db.query(Delivery).filter(Delivery.id == delivery_id).first()

def update_delivery(db: Session, delivery_id: int, delivery_data: dict):
    db_delivery = db.query(Delivery).filter(Delivery.id == delivery_id).first()
    for key, value in delivery_data.items():
        setattr(db_delivery, key, value)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def delete_delivery(db: Session, delivery_id: int):
    db_delivery = db.query(Delivery).filter(Delivery.id == delivery_id).first()
    db.delete(db_delivery)
    db.commit()
    return db_delivery
