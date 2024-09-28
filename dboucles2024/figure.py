# Étape 1: Demander la largeur et la hauteur
largeur = int(input("Introduisez la largeur svp : "))
hauteur = int(input("Introduisez la hauteur svp : "))

print("X" * largeur)

for i in range(hauteur - 3):
    print("X" + (" " * (largeur - 2)) + "X")


print("X" * largeur)
