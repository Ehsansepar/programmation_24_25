def occurrence(chaine, car) : 
    compteur = 0
    for i in range(len(chaine)) : 
        if chaine[i] == car :
            compteur += 1
    return compteur
