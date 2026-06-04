# Homework 9: FastAPI Webshop Product API

A simple FastAPI application for managing products in an imaginary webshop.
The application uses async SQLAlchemy with SQLite and the aiosqlite driver.

Hungarian documentation is available in [README.hu.md](README.hu.md).

## Running the app

```bash
cd homeworks/budaikrisztian/hw_09_fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API documentation is available while the app is running:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

```text
GET     /api/v1/products/
GET     /api/v1/products/{product_id}
POST    /api/v1/products/
PUT     /api/v1/products/{product_id}
DELETE  /api/v1/products/{product_id}
```

The `PUT` endpoint updates the provided product fields.

## Example product creation request

```json
{
  "item_name": "morzsaporszivo",
  "quantity": 12,
  "price": 24900,
  "category": "haztartasi gep"
}
```

The `id` field does not need to be provided. The application generates it
automatically and includes it in the response.

## Tests and checks

```bash
cd ../../..
.venv/bin/ruff check homeworks/budaikrisztian/hw_09_fastapi
.venv/bin/mypy homeworks/budaikrisztian/hw_09_fastapi
.venv/bin/python -m pytest homeworks/budaikrisztian/hw_09_fastapi/tests -q
```
