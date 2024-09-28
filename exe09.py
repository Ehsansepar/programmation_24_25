# Ecrire un script qui permet de tirer 200 nombres au hasard, compris entre 0 et 100 et qui
# affiche ces nombres s'ils ne sont pas des multiples de 3. (1, 6, 9, 5, 4)

from random import randint

import math
# On définit la fonction qui génère les nombres au hasard

nombres = []

for i in  range(200):
    nombre = randint(0, 100)
    
    if nombre % 3 != 0 :
        nombres.append(nombre)
    else :
        continue

print(nombres)