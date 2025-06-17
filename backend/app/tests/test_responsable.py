import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Pour résoudre les imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import SessionLocal
from models import Base, Product, Reapprovisionnement
from responsable import consulter_stock, reapprovisionner

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # Setup in-memory DB
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    SessionLocal.configure(bind=engine)
    Base.metadata.create_all(engine)

    # Ajouter un produit pour les tests
    session = TestingSessionLocal()
    produit = Product(name="ProduitX", category="TestCat", price=20.0, stock=5)
    session.add(produit)
    session.commit()
    session.close()

    yield
    Base.metadata.drop_all(bind=engine)

def test_consulter_stock():
    produits = consulter_stock()
    assert isinstance(produits, list)
    assert len(produits) >= 1
    assert hasattr(produits[0], "name")
    assert hasattr(produits[0], "stock")

'''def test_reapprovisionner_succes():
    produit = consulter_stock()[0]
    stock_initial = produit.stock

    ok = reapprovisionner(produit.id, 10, magasin_id=1, centre_id=1)
    assert ok is True

    session = SessionLocal()
    produit_recharge = session.query(Product).get(produit.id)
    reappros = session.query(Reapprovisionnement).filter_by(produit_id=produit.id).all()
    session.close()

    assert produit_recharge.stock == stock_initial + 10
    assert len(reappros) == 1
    assert reappros[0].quantite == 10
'''
'''def test_reapprovisionner_produit_inexistant():
    ok = reapprovisionner(9999, 10, magasin_id=1, centre_id=1)
    assert ok is True  # Toujours True car même si produit absent, reappro est créé

    session = SessionLocal()
    reappros = session.query(Reapprovisionnement).filter_by(produit_id=9999).all()
    session.close()

    assert len(reappros) == 1
    assert reappros[0].quantite == 10
'''