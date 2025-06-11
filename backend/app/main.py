# main.py
from app.database import SessionLocal
from app.initialiser_items import init_products, init_users, init_magasins
from app.models import Utilisateur, RoleEnum
from app.menu import menu_employe, menu_gestionnaire, menu_responsable
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="POS API",
    description="Système de point de vente avec FastAPI",
    version="1.0.0"
)

app.include_router(router)

def main():
    init_products()
    init_users()
    init_magasins()

    print("=== Connexion ===")
    nom = input("Nom d'utilisateur : ")
    mdp = input("Mot de passe : ")

    session = SessionLocal()
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
    session.close()

if __name__ == "__main__":
    main()
