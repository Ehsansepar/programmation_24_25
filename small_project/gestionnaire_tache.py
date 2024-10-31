taches = []

def ajouter_tache() : 
    print(" --- option : Ajouter la tâche --- ")
    nom = input("Entrer le nom de tâche : ")
    description = input("Entrez la discription de la tâche : ")
    statut = "en attente"
    taches.append([nom, description, statut])

def afficher_taches() : 
    if not taches : 
        print(" --- Aucune tâche enregistrée --- ")

    else :
        # for tache in taches : 
        #     nom = tache[0]
        #     description = tache[1]
        #     statut = tache[2]
        for i, tache in enumerate(taches, 1):
            nom, description, statut = tache
        print("     --- Affichage des tâches ---    ")
        print(f"{i} - Nom : {nom}\n    Description : {description}\n    Statut : {statut}")



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