from database import SessionLocal
from models import RapportTendance, Product

def generer_rapport(region=None):
    session = SessionLocal()
    if region:
        rapports = session.query(RapportTendance).filter_by(region=region).all()
    else:
        rapports = session.query(RapportTendance).all()
    session.close()
    return rapports

def mettre_a_jour_produit(produit_id, champs):
    session = SessionLocal()
    produit = session.query(Product).get(produit_id)
    if not produit:
        session.close()
        return False
    for cle, val in champs.items():
        setattr(produit, cle, val)
    session.commit()
    session.close()
    return True
