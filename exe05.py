# Ecrire un script qui permet à l'utilisateur d'introduire 5 nombres, d'en faire la somme et de
# l'afficher. Utilisez une boucle !! ( 1, 6, 2, 8, 4)
# utilise un accumulateur

somme = 0

for i in range(5) : 
    i  = int(input("Entrez un nombre : "))
    somme = somme + i
print("La somme est de : ", somme)  # La somme est de :
