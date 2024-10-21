# 4. Créez une matrice carrée de n sur n, n étant fourni par l'utilisateur et initialisez la avec des zéros.
# lst=[] #matrice de 3 lignes 4 colonnes
# for i in range(0,3):
# lst.append([0]*4)


n = int(input("Entrez la taille de la matrice carrée (n): "))

lst = []

for i in range(n) : 
    lst.append([0]*n)

for j in lst : 
    print(j)