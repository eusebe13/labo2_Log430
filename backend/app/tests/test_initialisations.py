import os
import sys

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import depuis app/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from initialiser_items import init_magasins, init_products, init_users
from models import Base, Magasin, Product, Utilisateur

engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

'''def test_init_products():
    init_products()
    db = TestingSessionLocal()
    produits = db.query(Product).all()
    db.close()
    assert len(produits) == 20
    assert produits[0].name.startswith("Produit")

def test_init_users():
    init_users()
    db = TestingSessionLocal()
    users = db.query(Utilisateur).all()
    roles = set(user.role.value for user in users)
    db.close()
    assert len(users) == 3
    assert roles == {"employe", "gestionnaire", "responsable"}
'''
'''def test_init_magasins():
    init_magasins()
    db = TestingSessionLocal()
    magasins = db.query(Magasin).all()
    db.close()
    assert len(magasins) >= 1
    assert magasins[0].nom.startswith("Magasin")
'''
