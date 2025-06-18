from app.database import SessionLocal
from app.models import Product, Reapprovisionnement


def consulter_stock():
    session = SessionLocal()
    try:
        produits = session.query(Product).all()
        return produits
    finally:
        session.close()

def reapprovisionner(produit_id, quantite, magasin_id):
    """
    Ajoute une quantité au stock du produit et crée une entrée de réapprovisionnement.
    """
    session = SessionLocal()
    try:
        produit = session.query(Product).get(produit_id)
        if not produit:
            return False  # produit introuvable

        produit.stock += quantite

        reappro = Reapprovisionnement(
            produit_id=produit_id,
            quantite=quantite,
            magasin_id=magasin_id,
            statut="en cours"  # ou autre statut par défaut
        )
        session.add(reappro)
        session.commit()
        return True
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
