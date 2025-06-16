import os
import sys

# Ajouter le chemin du dossier parent pour les imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import engine
from app.models import Base
from app.initialiser_items import init_products, init_users, init_magasins, init_test

def init_db():
    print("Création des tables...")
    Base.metadata.create_all(bind=engine)

    print("Insertion des données initiales...")
    init_products()
    init_users()
    init_magasins()
    # init_test()
    print("Initialisation terminée.")

if __name__ == "__main__":
    init_db()
