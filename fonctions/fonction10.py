def demi_liste(liste, nb) :

    if nb != 0 and nb != 1 :
        return -1

    n_liste = []
    i  = nb 

    while i < len(liste) : 
        n_liste.append(liste[i])
        i+= 2

    return n_liste


l = ['chat', 'chien', 'loup', 'crocodile', 'souris', 'araignée']