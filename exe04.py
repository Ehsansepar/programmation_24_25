# Ecrire un script qui permet d'afficher 55 nombres tirés au hasard et compris entre 0 et 100
# (1, 6, 9, 4)

from random import  randint
nombre = []

for i in range(55) :
    value = randint(0, 100)  # Affiche 55 nombres compris entre
    nombre.append(value)

print(nombre)  # Affiche la liste des nombres