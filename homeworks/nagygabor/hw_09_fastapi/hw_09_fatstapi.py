
 http://127.0.0.1:8000/docs


from contextlib import asynccontextmanager
from uuid import UUID, uuid1

from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Field, Session, SQLModel, create_engine, select

# --------------------------------------------------------------------------- #
# Adatbázis beállítása
# --------------------------------------------------------------------------- #

DATABASE_URL = "sqlite:///webshop.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# --------------------------------------------------------------------------- #
# Modellek
# --------------------------------------------------------------------------- #

class ItemBase(SQLModel):
    item_name: str                       # pl: "morzsaporszívó"
    quantity: int                        # pl: 12 (egész szám -> int)
    price: int                           # pl: 24900 (forint, egész szám -> int)
    category: str | None = None          # opcionális mező, pl: "háztartási gép"



class Item(ItemBase, table=True):
   
    id: UUID = Field(default_factory=uuid1, primary_key=True)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(SQLModel):
    item_name: str | None = None
    quantity: int | None = None
    price: int | None = None
    category: str | None = None


# --------------------------------------------------------------------------- #
# Segédfüggvények
# --------------------------------------------------------------------------- #
def create_db_and_tables() -> None:
    """A modellek alapján létrehozza a táblákat, ha még nem léteznek."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Adatbázis-session függőség (dependency) az endpoint-okhoz."""
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Az app indulásakor létrehozzuk a táblákat.
    create_db_and_tables()
    yield
    # (Itt lehetne leállításkor takarítani, de most nincs rá szükség.)


app = FastAPI(title="Webshop termék-nyilvántartó", lifespan=lifespan)


# --------------------------------------------------------------------------- #
# Endpoint-ok (CRUD)
# --------------------------------------------------------------------------- #
@app.get("/items", response_model=list[Item])
def list_items(session: Session = Depends(get_session)):
    """Minden termék listázása."""
    return session.exec(select(Item)).all()


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: UUID, session: Session = Depends(get_session)):
    """Egy termék lekérése id alapján."""
    item = session.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="A termék nem található.")
    return item


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, session: Session = Depends(get_session)):
    """Új termék hozzáadása. Az id automatikusan generálódik, és a
    válaszban már benne lesz a létrejött termék (id-vel együtt)."""
    db_item = Item(**item.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(
    item_id: UUID,
    item: ItemUpdate,
    session: Session = Depends(get_session),
):
    """Egy termék adatainak frissítése id alapján.
    Csak a megadott mezőket módosítjuk, a többit változatlanul hagyjuk."""
    db_item = session.get(Item, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="A termék nem található.")

    update_data = item.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: UUID, session: Session = Depends(get_session)):
    """Egy termék törlése id alapján."""
    db_item = session.get(Item, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="A termék nem található.")

    session.delete(db_item)
    session.commit()
   
