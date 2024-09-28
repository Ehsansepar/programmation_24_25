# Soit 1 liste de nombres
# nb=[15,89,5,99,23,78,12,33,68,16]
# Afficher les cotes supérieures à 30 et comptabiliser les (Sauvez sous liste1.py)

nb=[15,89,5,99,23,78,12,33,68,16]
compteur = 0

for nombre in nb :
    if nombre > 30 :
        compteur += 1

# Afficher le nombre total d'éléments supérieurs à 30
print(f"Nombre total de nombres supérieurs à 30 : {compteur}")
