from sale_manager import (
    check_stock,
    initialize_products,
    list_products,
    register_sale,
    return_product,
    search_products,
)


def main():
    initialize_products()

    while True:
        print("\n1. Afficher les produits\n2. Rechercher un produit\n3. Enregistrer une vente\n4. Retour d'un produit\n5. Vérifier le stock\n6. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            produits = list_products()
            for p in produits:
                print(f"{p.id} - {p.name} ({p.category}) : {p.price}$, Stock: {p.stock}")

        elif choix == "2":
            keyword = input("Entrez un mot-clé (nom ou catégorie) : ")
            results = search_products(keyword)
            if results:
                for p in results:
                    print(f"{p.id} - {p.name} ({p.category}) : {p.price}$, Stock: {p.stock}")
            else:
                print("Aucun produit trouvé.")

        elif choix == "3":
            ids = input("IDs des produits séparés par une virgule: ")
            id_list = list(map(int, ids.split(",")))
            total = register_sale(id_list)
            print(f"Vente enregistrée. Total = {total}$")

        elif choix == "4":
            pid = int(input("ID du produit à retourner : "))
            success = return_product(pid)
            print("Produit retourné avec succès." if success else "Échec du retour.")

        elif choix == "5":
            pid = input("Entrez l'ID du produit (ou laissez vide pour tout voir) : ")
            stock_info = check_stock(int(pid)) if pid else check_stock()
            if isinstance(stock_info, list):
                for info in stock_info:
                    print(info)
            else:
                print(stock_info)

        elif choix == "6":
            break

if __name__ == "__main__":
    main()
