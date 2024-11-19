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
    # taches.append([nom, description, statut])

    # Sauvegarde dans un fichier
    fichier = open('./txt_files/test.txt', 'a')
    fichier.write(f"{nom}|{description}|{statut}\n")

    print("\n ---*--- Votre tâche a été enregistrée avec succès ---*---\n\n")
    input("Appuyez sur Entrée pour revenir au menu...")

def afficher_taches():
    """Affiche les tâches directement depuis le fichier."""
    clear_screen()
    try:
        fichier = open('./txt_files/test.txt', 'r')  # Open the file
        lignes = fichier.readlines()  # Read all lines
        if not lignes:
            print(" --- Aucune tâche enregistrée --- ")
        else:
            print("     --- Affichage des tâches ---    ")
            for ligne in lignes:  # Iterate through each line
                try:
                    nom, description, statut = ligne.strip().split('|')
                    print(f"Nom : {nom}\nDescription : {description}\nStatut : {statut}\n")
                except ValueError:
                    print(f" --- Ligne mal formatée : {ligne.strip()} --- ")
    except FileNotFoundError:
        print(" --- Aucune tâche enregistrée --- ")
    finally:
        fichier.close()  # Ensure the file is closed no matter what
    input("Appuyez sur Entrée pour revenir au menu...")



while True :
    print(" ajouter \n affichezr \n charger")
    choix = int(input("Choisissez une option : "))
    if choix == 1 :
        ajouter_tache()
    elif choix == 2 :
        afficher_taches()

