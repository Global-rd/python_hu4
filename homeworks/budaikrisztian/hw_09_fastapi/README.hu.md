# 9. házi feladat: FastAPI webshop termék API

Egyszerű FastAPI alkalmazás egy képzeletbeli webshop terméknyilvántartásához.
Az alkalmazás async SQLAlchemy kapcsolatot használ SQLite és aiosqlite
driverrel.

Az angol dokumentáció itt érhető el: [README.md](README.md).

## Az alkalmazás futtatása

```bash
cd homeworks/budaikrisztian/hw_09_fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Az API dokumentáció futás közben itt érhető el:

```text
http://127.0.0.1:8000/docs
```

## Endpointok

```text
GET     /api/v1/products/
GET     /api/v1/products/{product_id}
POST    /api/v1/products/
PUT     /api/v1/products/{product_id}
DELETE  /api/v1/products/{product_id}
```

A `PUT` endpoint a megadott termékmezőket frissíti.

## Példa termék létrehozása

```json
{
  "item_name": "morzsaporszívó",
  "quantity": 12,
  "price": 24900,
  "category": "háztartási gép"
}
```

Az `id` mezőt nem kell megadni. Az alkalmazás automatikusan generálja, és a
válaszban visszaadja.

## Tesztek és ellenőrzések

```bash
cd ../../..
.venv/bin/ruff check homeworks/budaikrisztian/hw_09_fastapi
.venv/bin/mypy homeworks/budaikrisztian/hw_09_fastapi
.venv/bin/python -m pytest homeworks/budaikrisztian/hw_09_fastapi/tests -q
```
