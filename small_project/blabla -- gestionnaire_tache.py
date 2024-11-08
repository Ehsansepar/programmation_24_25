import os
import time
from colorama import Fore, Style, init # pip install colorama

# Initialize colorama for cross-platform support
init(autoreset=True)

taches = []

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def ajouter_tache():
    clear_screen()

    print(Fore.CYAN + " --- Option : Ajouter une tâche --- ")
    nom = input(Fore.CYAN + "Entrez le nom de la tâche : ")
    description = input(Fore.CYAN + "Entrez la description de la tâche : ")
    statut = "en attente"
    taches.append([nom, description, statut])
    print(Fore.GREEN + "\n ---*--- Votre tâche a été enregistrée avec succès ---*---\n\n")
    input(Fore.YELLOW + "Appuyez sur Entrée pour revenir au menu...")

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
    if not taches:
        print(" --- Aucune tâche enregistrée --- ")
    else:
        print("     --- Affichage des tâches ---    ")
        for i, tache in enumerate(taches, 1):
            nom, description, statut = tache
            print(f"{i} - Nom : {nom}\n    Description : {description}\n    Statut : {statut}\n -----------------------\n\n")


def supprimer_tache():
    clear_screen()
    if not taches:
        print(" --- Aucune tâche enregistrée --- \n\n")
        input("Appuyez sur Entrée pour revenir au menu...")
        return

    afficher_taches()

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

def afficher_menu():
    clear_screen()
    print(Fore.YELLOW + "\n\n   *** Gestionnaire de Tâches ***\n")
    
    # Display the menu options styled as "buttons"
    print(Fore.CYAN + "****************************", end="  ")
    print(Fore.GREEN + "****************************", end="  ")
    print(Fore.BLUE + "****************************", end="  ")
    print(Fore.MAGENTA + "****************************", end="  ")
    print(Fore.RED + "****************************")

    print(Fore.CYAN + "* 1 - Ajouter une tâche   *", end="  ")
    print(Fore.GREEN + "* 2 - Afficher les tâches *", end="  ")
    print(Fore.BLUE + "* 3 - Marquer terminée    *", end="  ")
    print(Fore.MAGENTA + "* 4 - Supprimer tâche     *", end="  ")
    print(Fore.RED + "* 5 - Quitter             *")

    print(Fore.CYAN + "****************************", end="  ")
    print(Fore.GREEN + "****************************", end="  ")
    print(Fore.BLUE + "****************************", end="  ")
    print(Fore.MAGENTA + "****************************", end="  ")
    print(Fore.RED + "****************************")

    # Prompt for user input
    choix = input(Fore.YELLOW + "\n\nChoisissez une option (1-5) : ")
    return choix

def menu_principal():
    while True:
        choix = afficher_menu()
        
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            marquer_tache_terminee()
        elif choix == "4":
            supprimer_tache()
        elif choix == "5":
            print(Fore.GREEN + "Au revoir !")
            break
        else:
            print(Fore.RED + "Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
            time.sleep(2)

# Lancer le programme
menu_principal()
