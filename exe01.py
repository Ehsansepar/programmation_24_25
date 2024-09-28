# Ecrire un script qui permet de calculer le volume d'une sphère 4/3 pi R3
# pi vaut 3.141592 (1, 2, 3, 4)

from math import pi

rayon =  float(input("Entrez le rayon de la sphère : "))

volume  = (4/3) * pi * (5 ** 3)
print(round(volume, 2))  # Affiche le volume de la sphère
