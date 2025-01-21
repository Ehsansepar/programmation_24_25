def listeConvertToInt(liste) :
    listeInt = []
    for mot in liste :
        listeInt.append(len(mot))

def sommeListe(liste) :
    # dsqfj
    somme = 0 
    for i in range(len(liste)) : 
        somme += liste[i]
    return somme

# # Exercice 14 
def cmp_som_liste(s1, s2) :

    sumS1 = sommeListe(s1)
    sumS2 = sommeListe(s2)

    if sumS1 > sumS2 : 
        return 1
    elif sumS1 < sumS2 : 
        return -1
    else :
        return 0

    s1 = [2, 6, 8, 9, 4, 63] # => 92
    s2 = [5, 6, 74, 3, 1, 0] # => 89
    s3 = [7, 6, 9, 59, 6, 8] # => 95
    print(cmp_som_liste(s1, s2)) # retournera 1 car 92 – 89 = 3
    print(cmp_som_liste(s1, s3)) # retournera -1 car 92 – 95 = -3


# Exercice 15
def cmp_liste(s1, s2) : 
    return cmp_som_liste(listeConvertToInt(s1), listeConvertToInt(s2))
    

s1 = ['chat', 'chien', 'condor', 'serpent'] # => [4, 5, 6, 7] =>22
s2 = ['rat', 'souris', 'cochon', 'dragon'] # => [3, 6, 6, 6] => 21
print(cmp_liste(s1, s2)) # retournera 1 car 22 – 21 = 1