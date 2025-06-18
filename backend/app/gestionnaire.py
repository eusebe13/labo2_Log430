from app.database import SessionLocal
from app.models import Product, RapportTendance


def afficher_rapports():
    """
    Retourne tous les rapports de tendance.
    """
    session = SessionLocal()
    try:
        return session.query(RapportTendance).all()
    finally:
        session.close()


def generer_rapport(region=None):
    """
    Retourne les rapports filtrés par région si précisée, sinon tous les rapports.
    """
    session = SessionLocal()
    try:
        query = session.query(RapportTendance)
        if region:
            query = query.filter(RapportTendance.region == region)
        return query.all()
    finally:
        session.close()


def mettre_a_jour_produit(produit_id, champs: dict):
    """
    Met à jour les champs spécifiés d’un produit.
    :param produit_id: ID du produit à mettre à jour
    :param champs: Dictionnaire des champs à modifier (ex: {"stock": 10, "price": 15.5})
    :return: True si la mise à jour a réussi, False sinon
    """
    session = SessionLocal()
    try:
        produit = session.get(Product, produit_id)
        if not produit:
            return False
        for cle, valeur in champs.items():
            if hasattr(produit, cle):
                setattr(produit, cle, valeur)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
