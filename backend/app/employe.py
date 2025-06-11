from app.database import SessionLocal
from app.models import Product, Vente

def consulter_product():
    session = SessionLocal()
    product = session.query(Product).all()
    session.close()
    return product

def acheter_product(ids_product):
    session = SessionLocal()
    total = 0
    for pid in ids_product:
        produit = session.query(Product).get(pid)
        if produit and produit.stock > 0:
            produit.stock -= 1
            total += produit.price
    vente = Vente(total=total)
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
        product = session.query(Product).all()
        session.close()
        return [f"{p.name}: {p.stock} unités" for p in product]