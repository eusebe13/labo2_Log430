# main.py
from employe import consulter_product, acheter_product, verifier_stock
from gestionnaire import generer_rapport, mettre_a_jour_produit
from responsable import consulter_stock, reapprovisionner
from interfaceweb import afficher_rapports
from initialiser_test import initialize_products

def main():
    initialize_products()  # Initialiser les produits pour les tests
    while True:
        print("""
1. Afficher les produits
2. Acheter un produit
3. Vérifier le stock
4. Générer rapport (gestionnaire)
5. Mettre à jour un produit (gestionnaire)
6. Reapprovisionner un produit (responsable)
7. Voir les rapports (interface web)
8. Quitter
""")
        choix = input("Votre choix : ")

        if choix == "1":
            produits = consulter_product()
            for p in produits:
                print(f"{p.id} - {p.name} ({p.category}) : {p.price}$, Stock: {p.stock}")

        elif choix == "2":
            ids = input("IDs des produits séparés par une virgule : ")
            id_list = list(map(int, ids.split(",")))
            total = acheter_product(id_list)
            print(f"Vente enregistrée. Total = {total}$")

        elif choix == "3":
            pid = input("Entrez l'ID du produit (ou laissez vide pour tout voir) : ")
            stock_info = verifier_stock(int(pid)) if pid else verifier_stock()
            if isinstance(stock_info, list):
                for info in stock_info:
                    print(info)
            else:
                print(stock_info)

        elif choix == "4":
            region = input("Entrez une région (ou vide pour tout) : ")
            rapports = generer_rapport(region if region else None)
            for r in rapports:
                print(f"Rapport région: {r.region}, période: {r.periode}, total: {r.totalVentes}")

        elif choix == "5":
            pid = int(input("ID du produit à modifier : "))
            champ = input("Champ à modifier (ex: price) : ")
            val = input("Nouvelle valeur : ")
            try:
                val = float(val) if champ in ["price"] else val
            except:
                pass
            succes = mettre_a_jour_produit(pid, {champ: val})
            print("Produit mis à jour." if succes else "Échec de la mise à jour.")

        elif choix == "6":
            pid = int(input("ID du produit : "))
            quantite = int(input("Quantité : "))
            magasin_id = int(input("ID du magasin : "))
            centre_id = int(input("ID du centre logistique : "))
            reapprovisionner(pid, quantite, magasin_id, centre_id)
            print("Produit réapprovisionné.")

        elif choix == "7":
            rapports = afficher_rapports()
            for r in rapports:
                print(f"Région: {r.region}, Période: {r.periode}, Ventes: {r.totalVentes}$")

        elif choix == "8":
            break

if __name__ == "__main__":
    main()
