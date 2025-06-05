from database import SessionLocal
from models import RapportTendance

def afficher_rapports():
    session = SessionLocal()
    rapports = session.query(RapportTendance).all()
    session.close()
    return rapports