# 1. Soit une matrice exematr.py, je vous demande de faire la somme de la matrice

liste=[ 
    [11,24,3],
    [47,52,66],
    [71,89,91],
    [10,73,47] ]

somme=0

for i in range(len(liste)) : 
    for x in range(len(liste[i])) : 
        somme += liste[i][x]
print(somme)

# 