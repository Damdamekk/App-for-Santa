from sqlalchemy.orm import Session
from .Elf import Elf

def create_elf(db: Session, elf_data: dict):
    db_elf = Elf(**elf_data)
    db.add(db_elf)
    db.commit()
    db.refresh(db_elf)
    return db_elf

def get_elves(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Elf).offset(skip).limit(limit).all()

def get_elf(db: Session, elf_id: int):
    return db.query(Elf).filter(Elf.id == elf_id).first()

def update_elf(db: Session, elf_id: int, elf_data: dict):
    db_elf = db.query(Elf).filter(Elf.id == elf_id).first()
    for key, value in elf_data.items():
        setattr(db_elf, key, value)
    db.commit()
    db.refresh(db_elf)
    return db_elf

def delete_elf(db: Session, elf_id: int):
    db_elf = db.query(Elf).filter(Elf.id == elf_id).first()
    db.delete(db_elf)
    db.commit()
    return db_elf
