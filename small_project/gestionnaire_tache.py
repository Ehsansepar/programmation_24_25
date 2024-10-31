taches = []

def ajoute_tache() : 
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



ajoute_tache()
afficher_taches()