from fastapi import FastAPI
from models.Childs.endpoints import router as child_router
from models.Elfs.endpoints import router as elf_router
from models.Toys.endpoints import router as toy_router
from models.Deliveries.endpoints import router as delivery_router


app = FastAPI()


app.include_router(child_router, prefix="/api")
app.include_router(elf_router, prefix="/api")
app.include_router(toy_router, prefix="/api")
app.include_router(delivery_router, prefix="/api")
