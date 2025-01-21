def grands_mots(liste, nbre) : 
    new_lst = []
    for i in range(len(liste)) :
        if len(liste[i]) > nbre :
            new_lst.append(liste[i])

    if new_lst == [] : 
        return None
    return new_lst


l = ['crotale', 'python', 'boa', 'couleuvre', 'cobra']
print(grands_mots(l, 5)) # retournera ['crotale', 'python', 'couleuvre']
grands_mots(l, 9) # retournera -1.