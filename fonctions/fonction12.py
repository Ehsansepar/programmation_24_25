def liste_paire(liste) : 
    new_lst = []

    for element in range(len(liste)) : 
        if liste[element] % 2 == 0 : 
            new_lst.append(liste[element] / 2)
        elif liste[element] % 2 == 1 :
            new_lst.append(liste[element] * 2)

    return new_lst

serie = [4, 52, 13, 9, 16, 49, 756, 7]
print(liste_paire(serie)) # retournera [2, 104, 6, 18, 8, 98, 378, 14]