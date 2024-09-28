# Ecrire un script qui permet de tirer 200 nombres au hasard, compris entre 0 et 100 et qui
# n'affiche que les impairs. (1,6, 9, 5, 4)

from random import randint 

for  i in range(200) :
    nmb =  randint(0, 100)
    if nmb % 2 != 0 :
        print(nmb)