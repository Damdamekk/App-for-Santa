from sqlalchemy.orm import Session
from .Child import Child

def create_child(db: Session, child_data: dict):
    db_child = Child(**child_data)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child

def get_children(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Child).offset(skip).limit(limit).all()

def get_child(db: Session, child_id: int):
    return db.query(Child).filter(Child.id == child_id).first()

def update_child(db: Session, child_id: int, child_data: dict):
    db_child = db.query(Child).filter(Child.id == child_id).first()
    for key, value in child_data.items():
        setattr(db_child, key, value)
    db.commit()
    db.refresh(db_child)
    return db_child

def delete_child(db: Session, child_id: int):
    db_child = db.query(Child).filter(Child.id == child_id).first()
    db.delete(db_child)
    db.commit()
    return db_child
