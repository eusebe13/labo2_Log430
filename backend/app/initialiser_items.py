from database import SessionLocal
from models import Product, Utilisateur, Magasin, RoleEnum, RapportTendance, Reapprovisionnement


def init_products():
    session = SessionLocal()
    existing = session.query(Product).count()
    if existing == 0:
        for i in range(20):
            product = Product(
                name=f"Produit{i+1}",
                category="CatégorieA" if i % 2 == 0 else "CatégorieB",
                price=10.0 + i,
                stock=(i + 1) * 2
            )
            session.add(product)
        session.commit()
    session.close()

def init_users():

    session = SessionLocal()

    # Vérifie si des utilisateurs existent déjà
    if session.query(Utilisateur).count() == 0:
        # Création d'un magasin par défaut si aucun magasin n'existe
        magasin = session.query(Magasin).first()
        if not magasin:
            magasin = Magasin(nom="Magasin Central", region="Région A")
            session.add(magasin)
            session.commit()

        # Création des utilisateurs avec des rôles différents
        employe = Utilisateur(
            nom="employe1",
            mot_de_passe="1234",
            role=RoleEnum.employe,
            magasin_id=magasin.id
        )
        gestionnaire = Utilisateur(
            nom="gestionnaire1",
            mot_de_passe="admin",
            role=RoleEnum.gestionnaire,
            magasin_id=magasin.id
        )
        responsable = Utilisateur(
            nom="responsable1",
            mot_de_passe="root",
            role=RoleEnum.responsable,
            magasin_id=magasin.id,
            is_maison_mere=True  # ou False selon ta logique
        )

        # Ajout à la session
        session.add_all([employe, gestionnaire, responsable])
        session.commit()
        print("Utilisateurs initiaux créés.")
    else:
        print("Utilisateurs déjà présents.")
    
    session.close()

def init_magasins():
    session = SessionLocal()

    # Vérifie si des magasins existent déjà
    if session.query(Magasin).count() == 0:
        magasins = [
            Magasin(nom="Magasin Central", region="Région A"),
            Magasin(nom="Magasin Nord", region="Région B"),
            Magasin(nom="Magasin Sud", region="Région C")
        ]
        session.add_all(magasins)
        session.commit()
        print("Magasins initiaux créés.")
    else:
        print("Magasins déjà présents.")

    session.close()
