# 2) Tirez 200 nombres au hasard compris entre 1 et 100, et ajoutez les dans la liste lst50 s'ils sont
# supérieurs à 50. Partez d'une liste vide et affichez à la fin la liste complète.
# Sauvez sous liste2.py

from random import randint


lst50 = []
for i in range (200):
    aletoir =  randint(1,100)
    if aletoir > 50 :
        lst50.append(aletoir)

print(lst50)