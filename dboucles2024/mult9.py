# 1. Etablir un programme qui permet de tirer 25 nombres au hasard compris entre 1 et 100.
# D'afficher uniquement les multiples de 9 et de les comptabiliser (comptabiliser = combien il y en a) (mult9.py). (1, 6, 9, 5, 4, 7, 4)

from random import *

nombres = []  # les nombres générés
multip_9 = []  # les multiples de 9

for i in range(25):
    nombre = randint(1, 100)  # Génère un nombre entre 1 et 100
    nombres.append(nombre)

    # Vérifier si le nombre est un multiple de 9
    if nombre % 9 == 0:
        multip_9.append(nombre)

print(f"Nombre généré : {nombres}")
print(f"Les nombres multiples de 9 sont : {multip_9}")
print("Nombre total de multiples de 9 : ", len(multip_9))
