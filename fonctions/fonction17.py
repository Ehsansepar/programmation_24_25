# Construire une fonction diff_list(liste1, liste2) qui, à partir de deux listes, permet de calculer
# une nouvelle liste qui est le résultat de la différence, élément par élément, des deux listes
# précédentes. Ces deux listes doivent posséder le mêmes nombres d'éléments !

def diff_list(liste1, liste2) : 
    new_lst = []

    if len(liste1) != len(liste2):
        return "Les listes doivent avoir le même nombre d'éléments!"

    # for i in range(len(liste1)) : 
    #     for j in range(len(liste2)) :
    #         new_lst.append(liste1[i] - liste2[j])

    for i in range(len(liste1)) :
        new_lst.append(liste1[i] - liste2[i])
    
    return new_lst





s1 = [4, 5, 8, 89, 2, 14]
s2 = [2, 3, 8, 65, 45, 6]

print(diff_list(s1, s2)) # retournera [2, 2, 0, 24, -43, 8]