# Projet : Gestionnaire de Stock d'un Petit Magasin
# Objectif
# Créer un programme pour gérer les stocks d’un magasin. Le programme va permettre de :

#1 Stocker des informations sur plusieurs articles (nom, quantité en stock, et prix unitaire).
#2 Afficher le stock de chaque article et son prix total en fonction de la quantité.
#3 Afficher l’article le plus cher et celui avec le plus de stock.
#4 Afficher la valeur totale de tous les articles en stock.



stock = [
    ["Pommes", 50, 1.5],
    ["Bananes", 30, 2.0],
    ["Oranges", 40, 1.8]
]


def aficher_stock() :
    article_plus_chere = ""
    prix_max = 0 
    article_plus_stocke = ""
    quantite_max = 0

    for article  in stock:
        nom =  article[0]
        quantite = article[1]
        prix_unitaire = article[2]
        prix_total = quantite * prix_unitaire
        print(f"Article : {nom}, Quantité : {quantite}, Prix unitaire : { prix_unitaire}, Prix total : {prix_total}")
        # Afficher l'article le plus cher et celui avec le plus de stock    
    
        if prix_unitaire > prix_max :
            prix_max = prix_unitaire
            article_plus_chere = nom 

        if quantite > quantite_max :
            quantite_max = quantite
            article_plus_stocke = nom
    print(f"Article le plus cher : {article_plus_chere}")
    print(f"Article avec le plus de stock : {article_plus_stocke}")
    # print(f"Article avec le plus de stock : {article_plus_stocke}")

def ajouter_article() :
    nom = input("Entrer le nom de l'article : ")
    quantite = int(input("Entrer la quantité de l'article : "))
    prix_unitaire = float(input("Entrer le prix unitaire de l'article : "))
    stock.append([nom, quantite, prix_unitaire])

while True :
    print("\n--- Menu ---")
    print("1. Afficher le stock")
    print("2. Ajouter un nouvel article")
    print("3. Quitter")

    choix =  int(input("Choisissez une option : "))

    if  choix == 1 :
        aficher_stock()
    elif  choix == 2 : 
        ajouter_article()
    elif choix == 3 :
        print("Au revoir")
        break
    else : 
        print("Option non valide, veuillez choisir une option entre 1 et 3")




