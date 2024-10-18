# 2. Soit une matrice exematr.py, je vous demande de calculer la somme de la 2ème colonne ainsi
# que de la 3ème ligne. (pas de boucles imbriquées une seule boucle est nécessaire)

liste=[ 
    # 0  1  2
    [11,24,3], # 0
    [47,52,66],# 1
    [71,89,91],# 2
    [10,73,47] ]# 3

somme_col2=0
somme_ligne3=0

# for i in range(len(liste)) : 
#     for j in range(len(liste)) :
#         somme_col2 +=  liste[i][1]
#         if   i == 2 :
#             somme_ligne3 += liste[i][j]

i = 0
while i < len(liste):
    somme_col2 += liste[i][1]
    if i == 2 :
        somme_ligne3 += sum(liste[i])
    i += 1
print("somme de la 2ème colonne : ",somme_col2)
print("somme de la 3ème ligne : ",somme_ligne3)

