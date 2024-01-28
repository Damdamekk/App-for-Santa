from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import create_toy, update_toy, delete_toy, get_toy, get_toys
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/toys/")
def create_toy(toy_data: dict, db: Session = Depends(get_db)):
    return create_toy(db, toy_data)

@router.get("/toys/")
def read_toys(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_toys(db, skip=skip, limit=limit)

@router.get("/toys/{toy_id}")
def read_toy(toy_id: int, db: Session = Depends(get_db)):
    return get_toy(db, toy_id)

@router.put("/toys/{toy_id}")
def update_toy(toy_id: int, toy_data: dict, db: Session = Depends(get_db)):
    return update_toy(db, toy_id, toy_data)

@router.delete("/toys/{toy_id}")
def delete_toy(toy_id: int, db: Session = Depends(get_db)):
    return delete_toy(db, toy_id)
