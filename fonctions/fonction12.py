def liste_paire(liste) :
    new_lst_pair = [] 
    for i in range(len(liste)) : 
        if i % 2 == 1 :
            new_lst_pair.append(liste[i] * 2)
        elif i % 2 == 0 :
            new_lst_pair.append(liste[i] // 2)
    return new_lst_pair

serie = [4, 52, 13, 9, 16, 49, 756, 7]
print(liste_paire(serie)) # retournera [2, 104, 6, 18, 8, 98, 378, 14]