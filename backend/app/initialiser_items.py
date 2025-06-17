from database import SessionLocal
from menu import menu_employe, menu_gestionnaire, menu_responsable
from models import Magasin, Product, RoleEnum, Utilisateur


def init_products():
    session = SessionLocal()
    try:
        if session.query(Product).count() == 0:
            for i in range(20):
                produit = Product(
                    name=f"Produit{i + 1}",
                    category="CatégorieA" if i % 2 == 0 else "CatégorieB",
                    price=10.0 + i,
                    stock=(i + 1) * 2
                )
                session.add(produit)
            session.commit()
            print("Produits initiaux créés.")
        else:
            print("Produits déjà présents.")
    finally:
        session.close()


def init_users():
    session = SessionLocal()
    try:
        if session.query(Utilisateur).count() == 0:
            magasin = session.query(Magasin).first()
            if not magasin:
                magasin = Magasin(nom="Magasin Central", region="Région A")
                session.add(magasin)
                session.commit()

            users = [
                Utilisateur(
                    nom="employe1",
                    mot_de_passe="1234",
                    role=RoleEnum.employe,
                    magasin_id=magasin.id
                ),
                Utilisateur(
                    nom="gestionnaire1",
                    mot_de_passe="admin",
                    role=RoleEnum.gestionnaire,
                    magasin_id=magasin.id
                ),
                Utilisateur(
                    nom="responsable1",
                    mot_de_passe="root",
                    role=RoleEnum.responsable,
                    magasin_id=magasin.id,
                    is_maison_mere=True
                )
            ]
            session.add_all(users)
            session.commit()
            print("Utilisateurs initiaux créés.")
        else:
            print("Utilisateurs déjà présents.")
    finally:
        session.close()


def init_magasins():
    session = SessionLocal()
    try:
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
    finally:
        session.close()


def init_test():
    print("=== Connexion ===")
    nom = input("Nom d'utilisateur : ")
    mdp = input("Mot de passe : ")

    session = SessionLocal()
    try:
        utilisateur = session.query(Utilisateur).filter_by(nom=nom, mot_de_passe=mdp).first()
        if utilisateur:
            print(f"Bienvenue {utilisateur.nom} ({utilisateur.role.value})")
            if utilisateur.role == RoleEnum.employe:
                menu_employe()
            elif utilisateur.role == RoleEnum.gestionnaire:
                menu_gestionnaire()
            elif utilisateur.role == RoleEnum.responsable:
                menu_responsable()
            else:
                print("Rôle non reconnu.")
        else:
            print("Nom ou mot de passe incorrect.")
    finally:
        session.close()
