from fastapi import FastAPI

from db.database import engine, Base
from routers.item_router import router as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Webshop Termék Nyilvántartó")

app.include_router(item_router)