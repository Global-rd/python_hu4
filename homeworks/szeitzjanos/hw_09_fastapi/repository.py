import uuid
from typing import List, Optional
from models import ProductModel
from schemas import ProductCreate, ProductUpdate
from database import get_connection


class ProductRepository:

    def list_all(self) -> List[ProductModel]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, item_name, quantity, price, category FROM products")
        rows = cursor.fetchall()
        conn.close()

        return [ProductModel(*row) for row in rows]

    def get_by_id(self, product_id: str) -> Optional[ProductModel]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, item_name, quantity, price, category FROM products WHERE id = ?",
            (product_id,)
        )
        row = cursor.fetchone()
        conn.close()

        return ProductModel(*row) if row else None

    def create(self, data: ProductCreate) -> ProductModel:
        new_id = str(uuid.uuid1())
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO products (id, item_name, quantity, price, category)
            VALUES (?, ?, ?, ?, ?)
        """, (new_id, data.item_name, data.quantity, data.price, data.category))

        conn.commit()
        conn.close()

        return ProductModel(new_id, data.item_name, data.quantity, data.price, data.category)

    def update(self, product_id: str, data: ProductUpdate) -> Optional[ProductModel]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE products
            SET item_name = ?, quantity = ?, price = ?, category = ?
            WHERE id = ?
        """, (data.item_name, data.quantity, data.price, data.category, product_id))

        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()

        return self.get_by_id(product_id) if updated else None

    def delete(self, product_id: str) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()

        return deleted
