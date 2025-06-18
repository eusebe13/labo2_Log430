import os
import sys

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from employe import acheter_product, consulter_product, verifier_stock
from initialiser_items import init_products
from models import Base, Magasin, Product, Vente

engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

    # Créer un magasin obligatoire (id = 1)
    session = TestingSessionLocal()
    magasin = Magasin(id=1, nom="MagasinTest", region="Test")
    session.add(magasin)
    session.commit()
    session.close()

    # Ajouter des produits
    init_products()
    yield
    Base.metadata.drop_all(bind=engine)

'''def test_consulter_product():
    produits = consulter_product()
    assert len(produits) == 20
    assert all(hasattr(p, "name") and hasattr(p, "stock") for p in produits)

def test_acheter_product_single():
    db = TestingSessionLocal()
    produit = db.query(Product).first()
    stock_initial = produit.stock
    prix = produit.price
    db.close()

    total = acheter_product([produit.id], magasin_id=1)
    assert total == prix

    db = TestingSessionLocal()
    produit_apres = db.query(Product).get(produit.id)
    ventes = db.query(Vente).all()
    db.close()

    assert produit_apres.stock == stock_initial - 1
    assert len(ventes) == 1
    assert ventes[0].prix_total == prix
    assert ventes[0].quantite == 1
    assert ventes[0].produit_id == produit.id
    assert ventes[0].magasin_id == 1

def test_verifier_stock_tous():
    stock = verifier_stock()
    assert isinstance(stock, list)
    assert len(stock) == 20
    assert all("unités" in ligne for ligne in stock)

def test_verifier_stock_un_produit():
    produit = consulter_product()[0]
    result = verifier_stock(produit.id)
    assert isinstance(result, str)
    assert str(produit.stock) in result
    assert produit.name in result

def test_verifier_stock_introuvable():
    result = verifier_stock(99999)
    assert result == "Introuvable"
'''
