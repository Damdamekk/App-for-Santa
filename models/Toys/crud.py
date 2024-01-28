from sqlalchemy.orm import Session
from .Toy import Toy

def create_toy(db: Session, toy_data: dict):
    db_toy = Toy(**toy_data)
    db.add(db_toy)
    db.commit()
    db.refresh(db_toy)
    return db_toy

def get_toys(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Toy).offset(skip).limit(limit).all()

def get_toy(db: Session, toy_id: int):
    return db.query(Toy).filter(Toy.id == toy_id).first()

def update_toy(db: Session, toy_id: int, toy_data: dict):
    db_toy = db.query(Toy).filter(Toy.id == toy_id).first()
    for key, value in toy_data.items():
        setattr(db_toy, key, value)
    db.commit()
    db.refresh(db_toy)
    return db_toy

def delete_toy(db: Session, toy_id: int):
    db_toy = db.query(Toy).filter(Toy.id == toy_id).first()
    db.delete(db_toy)
    db.commit()
    return db_toy
