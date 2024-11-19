# 1) Soit 1 liste de nombres
# Afficher les cotes supérieures à 30 et comptabiliser les (Sauvez sous liste1.py)

# nb=[15,89,5,99,23,78,12,33,68,16]

# nouvelle_liste = []
# compteur = 0

# for i in nb :
#     if i > 30 :
#         nouvelle_liste.append(i)
#         compteur += 1

# print(nouvelle_liste)
# print(compteur)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 3) Soit 1 liste de nombres
nb=[25,89,65,99,13,78,12,33,68,17]
# Trouver et afficher le maximum de la liste

maximum = 0

for i in range(len(nb)) :
    if nb[i] > maximum :
        maximum = nb[i]
print(maximum)