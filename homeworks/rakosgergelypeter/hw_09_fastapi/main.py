from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
from routers.items import router as item_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield 

    await engine.dispose()
    
app = FastAPI(lifespan=lifespan)
app.include_router(item_router)

@app.get("/")
def root():
    return {"message": "FastAPI is working"}