from fastapi import APIRouter, Depends, Form, status
from typing import Optional  # új update miatt
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import schemas, services

router = APIRouter(
    prefix="/items",
    tags=["Termékek"]
)

@router.get("", response_model=list[schemas.ItemResponse], status_code=status.HTTP_200_OK)
async def get_all_items(db: AsyncSession = Depends(get_db)):
    return await services.fetch_all_items(db)

@router.get("/{item_id}", response_model=schemas.ItemResponse)
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)):
    return await services.fetch_item_by_id(db, item_id)

@router.post("", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    return await services.add_new_item(db, item)

# meghagyom a régi update végpontot, hogy látszódjon a különbség a formos és a sima json update között, de most már a json és a formos van használatban
# --- 1. VERZIÓ: AZ EREDETI (JSON alapú) PUT ---
# Elérési út: PUT /items/{item_id}/json <-- Kapott egy /json utótagot!
# Ez a standard, ahol egy JSON objektumot küldünk a Request Body-ban

@router.put("/{item_id}/Json", response_model=schemas.ItemResponse)
async def update_item_json(
    item_id: str, 
    item_update: schemas.ItemUpdate, 
    db: AsyncSession = Depends(get_db)
):
    return await services.modify_item(db, item_id, item_update)


# --- 2. VERZIÓ: A FORM-ALAPÚ PUT (A Swagger-barát "trükkös" verzió)
# Elérési út: PUT /items/{item_id}/form   <-- Kapott egy /form utótagot!
# Itt külön beviteli mezők (rubrikák) jelennek meg a Swaggerben
@router.put("/{item_id}/form", response_model=schemas.ItemResponse)
async def update_item(
    item_id: str,
    # A Pydantic objektum helyett egyenként kérjük be a mezőket opcionális Form-ként
    item_name: Optional[str] = Form(None, description="Új név (hagyd üresen, ha nem változik)"),
    quantity: Optional[int] = Form(None, ge=0, description="Új mennyiség"),
    price: Optional[float] = Form(None, gt=0, description="Új ár"),
    category: Optional[str] = Form(None, description="Új kategória (hagyd üresen, ha nem változik)"),
    db: AsyncSession = Depends(get_db)
):
    # Becsomagoljuk a beérkezett form adatokat a meglévő Pydantic sémánkba
    item_update = schemas.ItemUpdate(
        item_name=item_name,
        quantity=quantity,
        price=price,
        category=category
    )
    
    # Meghívjuk a service-t, ami elmenti és a válszban visszadobja a már frisített teljes adatot
    updated_item = await services.modify_item(db, item_id, item_update)
    return updated_item



@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, db: AsyncSession = Depends(get_db)):
    await services.remove_item(db, item_id)
    return None