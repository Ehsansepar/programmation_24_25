# Ecrire un script qui permet d'afficher les 10 premiers termes de n'importe quelle table de
# multiplication, utilisez i dans votre multiplication. (1, 2, 6, 3, 4)


nombre = int(input("Entrer un nombre pour multiplication : "))

for i in range(10) :
    print(f"{i} X  3 = {i * nombre}")  # Affiche les 10 premiers termes