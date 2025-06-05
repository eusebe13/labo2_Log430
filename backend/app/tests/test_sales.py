import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from sqlalchemy import create_engine

from app.database import SessionLocal
from app.models import Base  #, Sale
from backend.app.initialiser_test import (
    check_stock,
    initialize_products,
    list_products,
    register_sale,
    return_product,
    search_products,
)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # Setup in-memory database
    engine = create_engine("sqlite:///:memory:")
    #TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    SessionLocal.configure(bind=engine)

    '''# Add initial data
    session = TestingSessionLocal()
    product = Product(name="TestProduct", category="Test", price=10.0, stock=5)
    session.add(product)
    session.commit()
    session.close()'''

    yield

    Base.metadata.drop_all(bind=engine)

def test_list_products():
    products = list_products()
    print(products[0].name)
    assert len(products) == 20
    assert products[0].name == "Produit1"

def test_register_sale():
    initial_stock = list_products()[0].stock
    total = register_sale([1])
    assert total == 10.0
    assert list_products()[0].stock == initial_stock - 1

def test_register_sale_out_of_stock():
    for _ in range(5):
        register_sale([1])
    total = register_sale([1])
    assert total == 0  # No stock left

def test_search_product():
    result = search_products("1")
    assert len(result) >= 1

def test_register_return():
    register_sale([1])
    initial_stock = list_products()[0].stock
    return_product(1)
    assert list_products()[0].stock == initial_stock + 1

def test_get_stock_status():
    status = check_stock()
    print(status)
    assert isinstance(status, list)
    assert any("Produit1: 1 unités" in s for s in status)

def test_add_initial_products():
    # Should not throw
    initialize_products()
    assert len(list_products()) >= 20
