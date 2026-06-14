from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

# Fontos: sqlite+aiosqlite-ot használunk a sima sqlite helyett
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# AsyncSession-t használó sessionmaker konfigurálása
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

# Aszinkron Dependency Injection függvény
async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()