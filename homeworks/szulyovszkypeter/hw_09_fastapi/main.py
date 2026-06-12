from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from routers import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- 1. Startup (Induláskor lefutó rész) ---
    ## App indulásakor: Létrehozzuk a táblákat aszinkron módon
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield  # Itt fut az alkalmazás, amíg le nem állítják
    
    # --- 2. Shutdown (Leálláskor lefutó rész) ---
    # Tisztán lezárjuk a kapcsolatokat és felszabadítjuk a pool-t
    await engine.dispose()
    print("Az adatbázis kapcsolatok sikeresen lezárva. Bye!")



app = FastAPI(
    title="Webshop Termék Nyilvántartó - Teljesen Aszinkron",
    lifespan=lifespan
)

app.include_router(router)