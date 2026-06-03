"""
FastAPI app, ami egy képzeletbeli webshop termék nyílvántartójaként működik az alapvető CRUD endpoint-okkal.

"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import Base, engine
from routers.sanya_webshop import router

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 
    await engine.dispose()

# --------------------------------------------------------------------------------
#
# main:app
#
# --------------------------------------------------------------------------------

app = FastAPI(lifespan=lifespan)
app.include_router(router)

# Az app indítása:
#   - cd a 'hw_09_fastapi' könyvtárba
#   - uvicorn main:app --reload
