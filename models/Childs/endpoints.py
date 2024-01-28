from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import create_child,get_child,get_children,delete_child,update_child
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/children/")
def create_child(child_data: dict, db: Session = Depends(get_db)):
    return create_child(db, child_data)

@router.get("/children/")
def read_children(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_children(db, skip=skip, limit=limit)

@router.get("/children/{child_id}")
def read_child(child_id: int, db: Session = Depends(get_db)):
    return get_child(db, child_id)

@router.put("/children/{child_id}")
def update_child(child_id: int, child_data: dict, db: Session = Depends(get_db)):
    return update_child(db, child_id, child_data)

@router.delete("/children/{child_id}")
def delete_child(child_id: int, db: Session = Depends(get_db)):
    return delete_child(db, child_id)
