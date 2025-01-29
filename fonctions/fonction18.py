# Enregistrer le fichier sous le nom fonction18.py
# Construire une fonction cut_endlist(liste) qui, à partir d'une liste, permet de conserver dans
# une nouvelle liste tous les éléments de l'ancienne liste, sauf le dernier! La fonction retournera
# cette liste! Si la liste de départ est vide, la fonction retournera une liste vide!
# EXEMPLE


def cut_endlist(liste) : 
    if not liste :
        return []
    return liste[:-1]



s1 = ["hello", 40.25, 57, "world", 4, "!"]
print(cut_endlist(s1)) # retournera ["hello", 40.25, 57, "world", 4]