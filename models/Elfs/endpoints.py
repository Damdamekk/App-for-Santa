from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import update_elf, create_elf, get_elf,get_elves,delete_elf
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/elves/")
def create_elf(elf_data: dict, db: Session = Depends(get_db)):
    return create_elf(db, elf_data)

@router.get("/elves/")
def read_elves(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_elves(db, skip=skip, limit=limit)

@router.get("/elves/{elf_id}")
def read_elf(elf_id: int, db: Session = Depends(get_db)):
    return get_elf(db, elf_id)

@router.put("/elves/{elf_id}")
def update_elf(elf_id: int, elf_data: dict, db: Session = Depends(get_db)):
    return update_elf(db, elf_id, elf_data)

@router.delete("/elves/{elf_id}")
def delete_elf(elf_id: int, db: Session = Depends(get_db)):
    return delete_elf(db, elf_id)
