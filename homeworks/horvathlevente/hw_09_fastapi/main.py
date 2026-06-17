from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid1, UUID

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import create_engine

# -----------------------
# Adatbázis beállítások
# -----------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./items.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------
# SQLAlchemy modell
# -----------------------

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)


# -----------------------
# Pydantic modellek
# -----------------------

class ItemBase(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item_name": "morzsaporszívó",
                    "quantity": 12,
                    "price": 24900,
                    "category": "háztartási gép"
                }
            ]
        }
    }


class ItemCreate(ItemBase):
    # id-t nem ad meg a user
    pass


class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None


class Item(ItemBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }


# -----------------------
# FastAPI app
# -----------------------

app = FastAPI(title="Webshop terméknyilvántartó – hw_09_fastapi")


# 1) Minden termék listázása
@app.get("/items", response_model=List[Item])
def list_items(db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    return [
        Item(
            id=UUID(item.id),
            item_name=item.item_name,
            quantity=item.quantity,
            price=item.price,
            category=item.category,
        )
        for item in items
    ]


# 2) 1 termék listázása id alapján
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: UUID, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == str(item_id)).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(
        id=UUID(item.id),
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        category=item.category,
    )


# 3) 1 termék hozzáadása (id generálódik, de a response-ban benne van)
@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_id = str(uuid1())
    db_item = ItemDB(
        id=new_id,
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        category=item.category,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return Item(
        id=UUID(db_item.id),
        item_name=db_item.item_name,
        quantity=db_item.quantity,
        price=db_item.price,
        category=db_item.category,
    )


# 4) 1 termék adatainak frissítése id alapján
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: UUID, item_update: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == str(item_id)).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_update.item_name is not None:
        db_item.item_name = item_update.item_name
    if item_update.quantity is not None:
        db_item.quantity = item_update.quantity
    if item_update.price is not None:
        db_item.price = item_update.price
    if item_update.category is not None:
        db_item.category = item_update.category

    db.commit()
    db.refresh(db_item)

    return Item(
        id=UUID(db_item.id),
        item_name=db_item.item_name,
        quantity=db_item.quantity,
        price=db_item.price,
        category=db_item.category,
    )


# 5) 1 termék törlése id alapján
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: UUID, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == str(item_id)).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return


# Egyszerű root endpoint
@app.get("/")
def root():
    return {"message": "hw_09_fastapi – webshop terméknyilvántartó"}
