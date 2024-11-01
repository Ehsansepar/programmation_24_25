taches = []

def ajouter_tache() : 
    print(" --- option : Ajouter la tâche --- ")
    nom = input("Entrer le nom de tâche : ")
    description = input("Entrez la discription de la tâche : ")
    statut = "en attente"
    taches.append([nom, description, statut])
    print("\n ---*--- Votre tâche a enregistrer avec succés ---*---")

def afficher_taches() : 
    if not taches : 
        print(" --- Aucune tâche enregistrée --- ")

    else :
        # for tache in taches : 
        #     nom = tache[0]
        #     description = tache[1]
        #     statut = tache[2]
        print("     --- Affichage des tâches ---    ")
        for i, tache in enumerate(taches, 1):
            nom, description, statut = tache
            print(f"{i} - Nom : {nom}\n    Description : {description}\n    Statut : {statut}\n -----------------------")


def supprimer_tache() : 
    if not taches :
        print(" --- Aucune tâche enregistrée --- ")
        return
    
    afficher_taches()

    while True : 
        index = int(input("Entrez le numéro de la tâche à supprimer : "))

        try : 
            if index < 0 :
                print("Le numéro est invalide. Entrez un nombre positif : ")
            elif index > len(taches) :
                print("Numéro de tâche est invalid. Entrez un nombre dans la liste : ")
            else :
                taches.pop(index-1)
                print("Votre tâche a supprimé avec succés")
                break
        except ValueError : 
            print("Entrez un nombre valide.")

def marquer_tache_terminee() : 
    if not taches : 
        print(" --- Aucune tâche enregistrée --- ")
        return
    
    afficher_taches()

    while True : 
        try : 
            nombre_tache = int(input("Entrez le numéro de la tâche à marqué comme terminée : "))

            if nombre_tache < 0 :
                print("Entrez un nombre positif. ")
            elif nombre_tache > len(taches) : 
                print("le nombre est invalide. Entrez un nombre dans la liste. ")
            else : 
                taches[nombre_tache - 1][2] = "terminée"
                print(f"Votre tâche '{taches[nombre_tache - 1][0]}' marquée comme terminée. ")
                break
        except ValueError :
            print("Entrez un nombre valide. ")



def menu_principal():
    while True:
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

# Lancer le programme
menu_principal()