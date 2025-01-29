# Enregistrer le fichier sous le nom fonction19.py
# Construire un fonction cut_beglist(liste). Même chose que précédemment, sauf qu'il s'agit du
# premier élément de la liste! Si la liste de départ est vide, la fonction retournera une liste vide!
# EXEMPLE
# s1 = ["hello", 40.25, 57, "world", 4, "!"]
# cut_beglist(s1) # retournera [40.25, 57, "world", 4, "!"]


def cut_beglist(liste) :
    if not liste :
        return []
    return liste[1:]



s1 = ["hello", 40.25, 57, "world", 4, "!"]
print(cut_beglist(s1)) # retournera [40.25, 57, "world", 4, "!"]