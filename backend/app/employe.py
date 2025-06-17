from database import SessionLocal
from models import Product, Vente, Magasin

def consulter_product():
    session = SessionLocal()
    produits = session.query(Product).all()
    session.close()
    return produits

def acheter_product(ids_product, magasin_id=1):
    session = SessionLocal()
    total = 0
    for pid in ids_product:
        produit = session.query(Product).get(pid)
        if produit and produit.stock > 0:
            produit.stock -= 1
            total += produit.price
            vente = Vente(
                produit_id=produit.id,
                magasin_id=magasin_id,
                quantite=1,
                prix_total=produit.price
            )
            session.add(vente)
    session.commit()
    session.close()
    return total

def verifier_stock(produit_id=None):
    session = SessionLocal()
    if produit_id:
        produit = session.query(Product).get(produit_id)
        session.close()
        return f"{produit.name}: {produit.stock} unités" if produit else "Introuvable"
    else:
        produits = session.query(Product).all()
        session.close()
        return [f"{p.name}: {p.stock} unités" for p in produits]
