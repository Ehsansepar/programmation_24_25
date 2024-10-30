# Ce programme est un gestionnaire simple de bibliothèque. Il permet à l’utilisateur de faire plusieurs actions sur une liste de livres prédéfinis. Chaque livre est représenté par une liste contenant son titre, auteur, genre, disponibilité et nombre d'emprunts. Toutes les données des livres sont stockées dans une liste nommée bibliotheque.

# Le programme propose un menu principal avec les options suivantes :

# Afficher tous les livres : Cette option affiche la liste complète des livres avec leurs détails.
# Ajouter un livre : L’utilisateur peut ajouter un nouveau livre à la bibliothèque en saisissant les informations nécessaires. Le livre est ensuite ajouté à la liste bibliotheque.
# Chercher des livres par genre : Permet de filtrer les livres par genre. L’utilisateur peut choisir entre trois genres : Fiction, Science-fiction, et Non-fiction. Selon le choix de l’utilisateur, le programme affiche tous les livres appartenant à ce genre.
# Afficher le livre le plus emprunté : Cette option identifie et affiche le livre ayant le plus grand nombre d'emprunts. Le programme parcourt chaque livre et compare le nombre d'emprunts pour déterminer le livre le plus populaire.
# Quitter le programme : Permet à l’utilisateur de fermer le gestionnaire.
# Le programme utilise une structure en boucle pour afficher le menu et réagir au choix de l'utilisateur. Chaque option est reliée à une fonction spécifique (afficher_tous_les_livres, ajouter_livre, afficher_livre_par_genre, afficher_livre_plus_emprunte) qui exécute l'action correspondante. Si l’utilisateur entre une option invalide, un message d’erreur s'affiche, et le menu est relancé pour que l’utilisateur puisse essayer à nouveau.

# En exécutant le code, l’utilisateur interagit avec le menu en entrant un chiffre pour choisir une option. Cela permet d’organiser les fonctionnalités de manière simple et accessible, facilitant ainsi la gestion de la bibliothèque.


#                       ---------------- Created By Separ Ehsan --------------------


# Liste de livres : [Titre, Auteur, Genre, Disponibilité, Nombre d'emprunts]
bibliotheque = [
    ["L'Alchimiste", "Paulo Coelho", "Fiction", "Disponible", 8],
    ["1984", "George Orwell", "Science-fiction", "Indisponible", 12],
    ["Sapiens", "Yuval Noah Harari", "Non-fiction", "Disponible", 5]
]

def show_library() :
    for livre in bibliotheque :
        titre = livre[0]
        auteur = livre[1]
        genre = livre[2]
        disponibilite = livre[3]
        emprunts = livre[4]
        print(f"Titre: {titre}, Auteur: {auteur}, Genre: {genre}, Disponibilité: {disponibilite}, Emprunts: {emprunts}")

def livre_plus_emprunts() : 
    livre_plus_emprunts = ""
    max_emprunt = 0

    for livre in bibliotheque : 
        if livre[4] > max_emprunt :
            max_emprunt = livre[4]
            livre_plus_emprunts = livre[0]
    print(f"Le livre plus emprunté est {livre_plus_emprunts} avec {max_emprunt} emprunts. ")


def afficher_livre_par_genre():
    print("--- Afficher les livres par genre ---")
    print("1 - Fiction")
    print("2 - Science-fiction")
    print("3 - Non-fiction")

    choix = int(input("Choisissez le genre de livre (1-3) : "))

    if choix == 1:
        genre_recherche = "Fiction"
    elif choix == 2:
        genre_recherche = "Science-fiction"
    elif choix == 3:
        genre_recherche = "Non-fiction"
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")
        return  # Sortie de la fonction si le choix est invalide

    print(f"\n--- Livres du genre {genre_recherche} ---")
    for livre in bibliotheque:
        if livre[2].lower() == genre_recherche.lower():
            titre = livre[0]
            auteur = livre[1]
            disponibilite = livre[3]
            emprunts = livre[4]
            print(f"Titre: {titre}, Auteur: {auteur}, Disponibilité: {disponibilite}, Emprunts: {emprunts}")

def ajouter_livre():
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    print(f"Pour Les Genre vous pouvez utliser ses genres : ")
    print("Fiction, Science-Fiction, Non-Fiction : ")
    genre = input("Entrez le genre du livre : ")
    disponibilite = input("Entrez la disponibilité (Disponible/Indisponible) : ")
    emprunts = int(input("Entrez le nombre d'emprunts : "))
    bibliotheque.append([titre, auteur, genre, disponibilite, emprunts])
    print(f"Le livre '{titre}' a été ajouté à la bibliothèque.")

def les_livre_dispo() : 
    for livre in bibliotheque : 
        if "Disponible".lower() == livre[3].lower() : 
            titre = livre[0]
            auteur = livre[1]
            disponibilite = livre[3]
            emprunts = livre[4]
    print("Les livres Disponible maintenant : ")
    print(f" --- Titre: {titre}, Auteur: {auteur}, Disponibilité: {disponibilite}, Emprunts: {emprunts}")


# def afficher_livre_par_gerne() : 
#     print(f"--- Afficher Les livre par rapport de Leur Genre : ")
#     print("--- 1 - Fiction ---")
#     print("--- 2 - Science_Fiction ---")
#     print("--- 3 - Non-fiction ---")

#     choix = int(input("Choisissez votre genre de Livre : "))
    

#     if choix == 1 : 
#         for livre in bibliotheque : 
#             if "fiction".lower() == livre[2].lower() : 
#                 titre = livre[0]
#                 auteur = livre[1]
#                 genre = livre[2]
#                 disponibilite = livre[3]
#                 emprunts = livre[4]
#                 print(f"Titre: {titre}, Auteur: {auteur}, Disponibilité: {disponibilite}, Emprunts: {emprunts}")
            
#             elif "fiction".lower() == livre[2].lower() : 
#                 titre = livre[0]
#                 auteur = livre[1]
#                 genre = livre[2]
#                 disponibilite = livre[3]
#                 emprunts = livre[4]
#                 print(f"Titre: {titre}, Auteur: {auteur}, Disponibilité: {disponibilite}, Emprunts: {emprunts}")

# show_library()
# livre_plus_emprunts()


def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Voir tous les livres")
        print("2 - Voir Le livre plus emprunt")
        print("3 - Ajouter un livre")
        print("4 - Chercher des livres par genre")
        print("5 - Voir des Livres Disponible")
        print("6 - Quitter")
        
        choix = int(input("Choisissez une option (1-4) : "))

        if choix == 1:
            show_library()
        elif choix == 2 :
            livre_plus_emprunts()
        elif choix == 3:
            ajouter_livre()
        elif choix == 4:
            afficher_livre_par_genre()
        elif choix == 5 : 
            les_livre_dispo()
        elif choix == 6:
            print("Merci d'avoir utilisé le gestionnaire de bibliothèque. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Lancement du programme
menu_principal()

# Created by Separ Ehsan 2024