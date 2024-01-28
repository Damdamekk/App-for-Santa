from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey('children.id'))
    elf_id = Column(Integer, ForeignKey('elves.id'))
    toy_id = Column(Integer, ForeignKey('toys.id'))
    delivery_date = Column(Date)

    child = relationship("Child", back_populates="deliveries")
    elf = relationship("Elf", back_populates="deliveries")
    toy = relationship("Toy", back_populates="deliveries")
