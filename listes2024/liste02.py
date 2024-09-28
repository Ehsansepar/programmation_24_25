# Etablir un programme qui permet de construire une liste composée de 25 nombres tirés au hasard
# et compris entre 1 et 100. Partez d'une liste vide et utilisez la méthode .append()

from random import  randint


nombre_hasard = []

for i in range(25) : 
    hasard = randint(1, 100)
    nombre_hasard.append(hasard)
    
print(nombre_hasard)