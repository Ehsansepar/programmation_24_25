# 📝 Projet 1 – Bloc-notes simple (niveau facile)

# Objectif : Gérer une liste de notes avec un menu.
# Ajouter une note
# Modifier une note par son numéro
# Voir toutes les notes
# Supprimer une note par son numéro
# Sauvegarder dans un fichier texte (optionnel)

# Tu utilises :
# Boucles (while)
# Listes
# Fonctions

# Variables
notes = [] 
menu = """
1. Ajouter une note
2. Modifier une note
3. Voir toutes les notes
4. Supprimer une note
5. Quitter
"""

# Fonctions

def affichier_menu():
    print(menu)

def afficher_notes(notes):
    if not notes:
        print("Aucune note à afficher.")
    else:
        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note}")
def ajouter_note(notes):
    note = input("Entrez la note à ajouter : ")
    notes.append(note)
    print("Note ajoutée.")



affichier_menu()
while True:
    option = choisir_option()
    if option == 1:
        ajouter_note(notes)
    elif option == 2:
        modifier_note(notes)
    elif option == 3:
        afficher_notes(notes)
    elif option == 4:
        supprimer_note(notes)
    elif option == 5:
        sauvegarder_notes(notes, 'notes.txt')
        print("Au revoir !")
        break
    affichier_menu()