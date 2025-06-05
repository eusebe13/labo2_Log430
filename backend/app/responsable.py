from database import SessionLocal
from models import Product, Reapprovisionnement

def consulter_stock():
    session = SessionLocal()
    produits = session.query(Product).all()
    session.close()
    return produits

def reapprovisionner(produit_id, quantite, magasin_id, centre_id):
    session = SessionLocal()
    reappro = Reapprovisionnement(
        produit_id=produit_id,
        quantite=quantite,
        magasin_id=magasin_id,
        centre_id=centre_id
    )
    produit = session.query(Product).get(produit_id)
    if produit:
        produit.stock += quantite
    session.add(reappro)
    session.commit()
    session.close()
    return True
