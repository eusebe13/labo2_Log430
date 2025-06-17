import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Pour que les imports fonctionnent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import SessionLocal
from models import Base, Product, RapportTendance
from gestionnaire import afficher_rapports, generer_rapport, mettre_a_jour_produit

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # Crée une BDD SQLite en mémoire
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    SessionLocal.configure(bind=engine)
    Base.metadata.create_all(engine)

    # Ajout de données de test
    session = TestingSessionLocal()

    produit = Product(name="ProduitTest", category="CatégorieX", price=15.0, stock=10)
    session.add(produit)
    session.commit()  # Nécessaire pour que produit.id soit défini

    rapport1 = RapportTendance(region="Est", total_ventes=1000.0)
    rapport2 = RapportTendance(region="Ouest", total_ventes=2000.0)

    rapport1.produits.append(produit)
    rapport2.produits.append(produit)

    session.add_all([rapport1, rapport2])
    session.commit()
    session.close()

    yield
    Base.metadata.drop_all(bind=engine)

def test_afficher_rapports():
    rapports = afficher_rapports()
    assert len(rapports) == 2
    regions = [r.region for r in rapports]
    assert "Est" in regions
    assert "Ouest" in regions

def test_generer_rapport_tout():
    rapports = generer_rapport()
    assert len(rapports) == 2
    assert all(hasattr(r, "total_ventes") for r in rapports)

def test_generer_rapport_filtre_region():
    rapports = generer_rapport("Est")
    assert len(rapports) == 1
    assert rapports[0].region == "Est"

def test_generer_rapport_region_inexistante():
    rapports = generer_rapport("Nord")
    assert rapports == []

def test_mettre_a_jour_produit_succes():
    session = SessionLocal()
    produit = session.query(Product).first()
    session.close()

    success = mettre_a_jour_produit(produit.id, {"price": 20.0})
    assert success

    session = SessionLocal()
    produit_modifie = session.query(Product).get(produit.id)
    session.close()

    assert produit_modifie.price == 20.0

def test_mettre_a_jour_produit_introuvable():
    success = mettre_a_jour_produit(9999, {"price": 20.0})
    assert not success
