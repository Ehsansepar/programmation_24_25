# Enregistrer le fichier sous le nom fonction20.py
# Construire une fonction cut_n_list(liste, nbre) qui, à partir d'une liste et d'un entier, permettra
# de retourner une liste composer des mêmes éléments que la liste de départ tout en omettant
# l'élément d'index donné au départ. Si l'index n'est pas légal, la fonction retournera la liste de
# départ. Si la liste de départ est vide, la fonction retournera une liste vide!


# Solution 1 (avec slicing)
def cut_n_list_v1(liste, nbre) : 
    if not liste:  # Vérifie si la liste est vide
        return []  
    if nbre < 0 or nbre >= len(liste):  
        return liste  
    return liste[:nbre] + liste[nbre+1:]  

# Solution 2 (avec pop)
def cut_n_list(liste, nbre) : 
    if not liste:  
        return []
    if nbre < 0 or nbre >= len(liste):  
        return liste
    
    nouvelle_liste = liste.copy()  
    nouvelle_liste.pop(nbre)
    return nouvelle_liste





# EXEMPLE
# s1 = ["hello", 40.25, 57, "world", 4, "!"]
# cut_n_list(s1, 3) # retournera ["hello", 40.25, 57, 4, "!"]