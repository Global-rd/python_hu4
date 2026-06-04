"""
Homework 9: Webshop product API tests.
Author: Budai Krisztian
"""

from collections.abc import AsyncGenerator

import httpx
import pytest
from app.api.deps import get_db
from app.api.v1.endpoints.products import get_product
from app.db.base import Base
from app.main import app
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate
from fastapi import HTTPException
from fastapi.routing import APIRoute
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool

# Shared database URL for isolated async repository tests.
TEST_DATABASE_URL = "sqlite+aiosqlite://"

# Shared product data for create and read tests.
PRODUCT_NAME = "morzsaporszivo"
PRODUCT_QUANTITY = 12
PRODUCT_PRICE = 24900
PRODUCT_CATEGORY = "haztartasi gep"

# Shared product data for update and delete tests.
UPDATED_QUANTITY = 7
UPDATED_CATEGORY = "elektronika"

# Shared missing identifier for not-found tests.
MISSING_PRODUCT_ID = "missing-product-id"

engine = create_async_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest.fixture
async def reset_database() -> None:
    """Reset the in-memory database before each async test."""
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


@pytest.fixture
def product_create_data() -> ProductCreate:
    """Create reusable product input data."""
    return ProductCreate(
        item_name=PRODUCT_NAME,
        quantity=PRODUCT_QUANTITY,
        price=PRODUCT_PRICE,
        category=PRODUCT_CATEGORY,
    )


@pytest.fixture
async def api_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    """Create an async HTTP client with a test database dependency."""

    async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
        async with TestingSessionLocal() as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db
    transport = httpx.ASGITransport(app=app)

    try:
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            yield client
    finally:
        app.dependency_overrides.clear()


class TestProductRoutes:
    """Tests for FastAPI product route registration."""

    def test_registers_product_routes(self) -> None:
        """The app should expose all product CRUD routes."""
        # Arrange
        expected_routes: set[tuple[str, str]] = {
            ("/api/v1/products/", "GET"),
            ("/api/v1/products/", "POST"),
            ("/api/v1/products/{product_id}", "GET"),
            ("/api/v1/products/{product_id}", "PUT"),
            ("/api/v1/products/{product_id}", "DELETE"),
        }

        # Act
        actual_routes: set[tuple[str, str]] = set()

        for route in app.routes:
            if not isinstance(route, APIRoute):
                continue

            for method in route.methods:
                actual_routes.add((route.path, method))

        # Assert
        assert expected_routes.issubset(actual_routes), (
            "Checks that all product CRUD routes are registered."
        )


class TestProductRepositoryCreateAndRead:
    """Tests for creating and reading products."""

    @pytest.mark.anyio
    async def test_creates_and_gets_product_by_id(
        self,
        reset_database: None,
        product_create_data: ProductCreate,
    ) -> None:
        """Created products should receive an id and be readable by id."""
        # Arrange
        async with TestingSessionLocal() as db:
            repository = ProductRepository(db)

            # Act
            product = await repository.create(product_create_data)
            saved_product = await repository.get_by_id(product.id)

            # Assert
            assert product.id, "Checks that id is generated."
            assert saved_product == product, "Checks id based product lookup."


class TestProductRepositoryUpdateAndDelete:
    """Tests for listing, updating and deleting products."""

    @pytest.mark.anyio
    async def test_lists_updates_and_deletes_product(
        self,
        reset_database: None,
    ) -> None:
        """Products should support list, update and delete operations."""
        # Arrange
        async with TestingSessionLocal() as db:
            repository = ProductRepository(db)
            product = await repository.create(
                ProductCreate(
                    item_name="telefon",
                    quantity=4,
                    price=199000,
                )
            )

            # Act
            products = await repository.get_all()
            updated_product = await repository.update(
                product.id,
                ProductUpdate(
                    quantity=UPDATED_QUANTITY,
                    category=UPDATED_CATEGORY,
                ),
            )
            deleted = await repository.delete(product.id)
            deleted_product = await repository.get_by_id(product.id)

            # Assert
            assert products == [product], "Checks product listing."
            assert updated_product is not None, "Checks update result exists."
            assert updated_product.quantity == UPDATED_QUANTITY, (
                "Checks updated quantity."
            )
            assert updated_product.category == UPDATED_CATEGORY, (
                "Checks updated category."
            )
            assert deleted is True, "Checks delete success flag."
            assert deleted_product is None, "Checks product is removed."


class TestProductApi:
    """Tests for product API calls through the ASGI app."""

    @pytest.mark.anyio
    async def test_creates_updates_gets_and_deletes_product_over_http(
        self,
        reset_database: None,
        product_create_data: ProductCreate,
        api_client: httpx.AsyncClient,
    ) -> None:
        """Product CRUD should work through HTTP requests."""
        # Arrange
        product_payload = product_create_data.model_dump()

        # Act
        create_response = await api_client.post(
            "/api/v1/products/",
            json=product_payload,
        )
        product_id = create_response.json()["id"]

        update_response = await api_client.put(
            f"/api/v1/products/{product_id}",
            json={"quantity": UPDATED_QUANTITY},
        )
        get_response = await api_client.get(
            f"/api/v1/products/{product_id}",
        )
        delete_response = await api_client.delete(
            f"/api/v1/products/{product_id}",
        )
        missing_response = await api_client.get(
            f"/api/v1/products/{product_id}",
        )

        # Assert
        assert create_response.status_code == 201, (
            "Checks product creation status."
        )
        assert update_response.status_code == 200, (
            "Checks product update status."
        )
        assert update_response.json()["quantity"] == UPDATED_QUANTITY, (
            "Checks updated quantity."
        )
        assert get_response.status_code == 200, "Checks product get status."
        assert get_response.json()["quantity"] == UPDATED_QUANTITY, (
            "Checks GET returns the updated quantity."
        )
        assert delete_response.status_code == 204, (
            "Checks product delete status."
        )
        assert missing_response.status_code == 404, (
            "Checks product is missing after delete."
        )

    @pytest.mark.anyio
    async def test_returns_404_for_missing_product_over_http(
        self,
        reset_database: None,
        api_client: httpx.AsyncClient,
    ) -> None:
        """ID based API operations should return 404 for unknown products."""
        # Arrange
        update_payload = {"quantity": UPDATED_QUANTITY}

        # Act
        get_response = await api_client.get(
            f"/api/v1/products/{MISSING_PRODUCT_ID}",
        )
        update_response = await api_client.put(
            f"/api/v1/products/{MISSING_PRODUCT_ID}",
            json=update_payload,
        )
        delete_response = await api_client.delete(
            f"/api/v1/products/{MISSING_PRODUCT_ID}",
        )

        # Assert
        assert get_response.status_code == 404, (
            "Checks missing product get status."
        )
        assert update_response.status_code == 404, (
            "Checks missing product update status."
        )
        assert delete_response.status_code == 404, (
            "Checks missing product delete status."
        )

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param(
                {
                    "item_name": "",
                    "quantity": PRODUCT_QUANTITY,
                    "price": PRODUCT_PRICE,
                },
                id="empty-name",
            ),
            pytest.param(
                {
                    "item_name": PRODUCT_NAME,
                    "quantity": -1,
                    "price": PRODUCT_PRICE,
                },
                id="negative-quantity",
            ),
            pytest.param(
                {
                    "item_name": PRODUCT_NAME,
                    "quantity": PRODUCT_QUANTITY,
                    "price": 0,
                },
                id="zero-price",
            ),
        ],
    )
    async def test_rejects_invalid_product_create_payloads(
        self,
        reset_database: None,
        api_client: httpx.AsyncClient,
        payload: dict[str, object],
    ) -> None:
        """Invalid create payloads should be rejected by validation."""
        # Arrange comes from the parametrized payload input.

        # Act
        response = await api_client.post("/api/v1/products/", json=payload)

        # Assert
        assert response.status_code == 422, (
            "Checks invalid create payload status."
        )


class TestMissingProducts:
    """Tests for missing product handling."""

    @pytest.mark.anyio
    async def test_repository_returns_none_or_false_for_missing_product(
        self,
        reset_database: None,
    ) -> None:
        """Repository operations should handle unknown ids gracefully."""
        # Arrange
        async with TestingSessionLocal() as db:
            repository = ProductRepository(db)

            # Act
            found_product = await repository.get_by_id(MISSING_PRODUCT_ID)
            updated_product = await repository.update(
                MISSING_PRODUCT_ID,
                ProductUpdate(price=42),
            )
            deleted = await repository.delete(MISSING_PRODUCT_ID)

            # Assert
            assert found_product is None, "Checks missing lookup result."
            assert updated_product is None, "Checks missing update result."
            assert deleted is False, "Checks missing delete result."

    @pytest.mark.anyio
    async def test_endpoint_returns_404_for_missing_product(
        self,
        reset_database: None,
    ) -> None:
        """The get product endpoint should raise 404 for unknown ids."""
        # Arrange
        async with TestingSessionLocal() as db:
            repository = ProductRepository(db)

            # Act + Assert
            with pytest.raises(HTTPException) as exc_info:
                await get_product(MISSING_PRODUCT_ID, repository)

        # Assert
        assert exc_info.value.status_code == 404, (
            "Checks missing product HTTP status."
        )
