# Soit 1 liste de nombres
# nb=[15,89,5,99,23,78,12,33,68,16]
# Trouver la moyenne
# Indiquer combien il y a de cotes supérieures à 30. (Sauvez sous liste1.py)

nb=[15,89,5,99,23,78,12,33,68,16]
compteur = 0

moyen = (sum(nb) / len(nb))
print(f"La  moyenne est {moyen}")

for superieurs in nb :
    if superieurs > 30 :
        compteur += 1

print(f"Nombre de côté supérieur  à 30 : {round(compteur, 2)}")  # affiche 5

