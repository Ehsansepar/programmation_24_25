import os
import time

taches = []

def clear_screen():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')

def ajouter_tache():
    clear_screen()
    print(" --- Option : Ajouter une tâche --- ")
    nom = input("Entrez le nom de la tâche : ")
    description = input("Entrez la description de la tâche : ")
    statut = "en attente"
    taches.append([nom, description, statut])

    # Sauvegarde dans un fichier
    with open('./txt_files/test.txt', 'a') as fichier:
        fichier.write(f"{nom}|{description}|{statut}\n")

    print("\n ---*--- Votre tâche a été enregistrée avec succès ---*---\n\n")
    input("Appuyez sur Entrée pour revenir au menu...")


def charger_taches():
    """Charge les tâches depuis un fichier texte."""
    try:
        with open('./txt_files/test.txt', 'r') as fichier:
            for ligne in fichier:
                nom, description, statut = ligne.strip().split('|')
                taches.append([nom, description, statut])
    except FileNotFoundError:
        # Si le fichier n'existe pas, aucune action n'est nécessaire
        pass

# def afficher_taches():
#     """Affiche les tâches directement à partir d'un fichier texte."""
#     clear_screen()
#     try:
#         fichier = open('./txt_files/test.txt', 'r')
#         # with open('./txt_files/test.txt', 'r') as fichier:
#         lignes = fichier.readlines()
#         if not lignes:
#             print(" --- Aucune tâche enregistrée --- ")
#         else:
#             print("     --- Affichage des tâches ---    ")
#             for i, ligne in enumerate(lignes, 1):
#                 nom, description, statut = ligne.strip().split('|')
#                 print(f"{i} - Nom : {nom}\n    Description : {description}\n    Statut : {statut}\n -----------------------\n")
#     except FileNotFoundError:
#         print(" --- Aucune tâche enregistrée --- ")
#     input("Appuyez sur Entrée pour revenir au menu...")

def afficher_taches():
    """Affiche les tâches directement depuis le fichier."""
    clear_screen()
    try:
        with open('./txt_files/test.txt', 'r') as fichier:
            lignes = fichier.readlines()
            if not lignes:
                print(" --- Aucune tâche enregistrée --- ")
            else:
                print("     --- Affichage des tâches ---    ")
                for ligne in lignes:
                    print(ligne.strip())
    except FileNotFoundError:
        print(" --- Aucune tâche enregistrée --- ")
    input("Appuyez sur Entrée pour revenir au menu...")



while True :
    print(" ajouter \n affichezr \n charger")
    choix = int(input("Choisissez une option : "))
    if choix == 1 :
        ajouter_tache()
    elif choix == 2 :
        afficher_taches()
    elif  choix == 3 :
        charger_taches()
