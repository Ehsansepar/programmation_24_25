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
    print("\n ---*--- Votre tâche a été enregistrée avec succès ---*---\n\n")
    input("Appuyez sur Entrée pour revenir au menu...")

def afficher_taches():
    clear_screen()
    if not taches:
        print(" --- Aucune tâche enregistrée --- ")
    else:
        print("     --- Affichage des tâches ---    ")
        for i, tache in enumerate(taches, 1):
            nom, description, statut = tache
            print(f"{i} - Nom : {nom}\n    Description : {description}\n    Statut : {statut}\n -----------------------\n\n")
    input("Appuyez sur Entrée pour revenir au menu...")

def afficher_taches_main():
    # clear_screen()
    if not taches:
        print(" --- Aucune tâche enregistrée --- ")
    else:
        print("     --- Affichage des tâches ---    ")
        for i, tache in enumerate(taches, 1):
            nom, description, statut = tache
            print(f"{i} - Nom : {nom}\n    Description : {description}\n    Statut : {statut}\n -----------------------\n\n")
    # input("Appuyez sur Entrée pour revenir au menu...")

def supprimer_tache():
    clear_screen()
    if not taches:
        print(" --- Aucune tâche enregistrée --- \n\n")
        input("Appuyez sur Entrée pour revenir au menu...")
        return

    afficher_taches_main()

    while True:
        try:
            index = int(input("Entrez le numéro de la tâche à supprimer : "))
            if 0 < index <= len(taches):
                taches.pop(index - 1)
                print("Votre tâche a été supprimée avec succès.\n\n")
                break
            else:
                print("Numéro de tâche invalide. Veuillez entrer un nombre dans la liste.")
        except ValueError:
            print("Entrez un nombre valide.")
    input("Appuyez sur Entrée pour revenir au menu...")

def marquer_tache_terminee():
    clear_screen()
    if not taches:
        print(" --- Aucune tâche enregistrée --- \n\n")
        input("Appuyez sur Entrée pour revenir au menu...")
        return
    
    afficher_taches_main()

    while True:
        try:
            nombre_tache = int(input("Entrez le numéro de la tâche à marquer comme terminée : "))
            if 0 < nombre_tache <= len(taches):
                taches[nombre_tache - 1][2] = "terminée"
                print(f"Votre tâche '{taches[nombre_tache - 1][0]}' a été marquée comme terminée.\n\n")
                break
            else:
                print("Numéro de tâche invalide. Veuillez entrer un nombre dans la liste.")
        except ValueError:
            print("Entrez un nombre valide.")
    input("Appuyez sur Entrée pour revenir au menu...")

def menu_principal():
    while True:
        clear_screen()
        print("\n--- Gestionnaire de Tâches ---")
        print("1 - Ajouter une nouvelle tâche")
        print("2 - Afficher toutes les tâches")
        print("3 - Marquer une tâche comme terminée")
        print("4 - Supprimer une tâche")
        print("5 - Quitter")

        choix = input("Choisissez une option (1-5) : ")

        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            marquer_tache_terminee()
        elif choix == "4":
            supprimer_tache()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
            time.sleep(2)  # Pause pour afficher le message avant de rafraîchir l'écran

# Lancer le programme
menu_principal()
