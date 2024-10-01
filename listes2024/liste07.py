#  Soit 1 liste de nombres
# nb=[25,89,65,99,13,78,12,33,68,17]
# afficher l'indice du plus grand nombre, la réponse ici est 3

nb=[25,89,65,99,13,78,12,33,68,17]

maximum = max(nb)

index_max =  nb.index(maximum)
print (index_max)  # affiche 3

print(maximum)