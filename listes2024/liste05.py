# Soit 1 liste
# ventes=[ "Bruxelles",12897, "Charleroi",11782, "Namur", 17651,"Liège",17670]
# Faites la moyenne des ventes. Partez absolument de cette liste. Votre programme doit fonctionner
# si l'on ajoute une ville et un montant.

ventes=[ "Bruxelles",12897, "Charleroi",11782, "Namur", 17651,"Liège",17670]

ventes = ["Bruxelles", 12897, "Charleroi", 11782, "Namur", 17651, "Liège", 17670]

somme_ventes = 0
nombre_de_villes = 0

for i in range(1, len(ventes), 2):  # Commence à 1, saute de 2 en 2
    somme_ventes += ventes[i]  # Ajouter le montant de vente
    nombre_de_villes += 1  # Incrémenter le nombre de villes


moyenne = somme_ventes / nombre_de_villes

print(f"La moyenne des ventes est de : {moyenne:.2f}")
