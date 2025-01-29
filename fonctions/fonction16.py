# Construire une fonction fibonacci(n) qui, à partir d'un entier, retournera une liste contenant
# les n premiers entiers faisant partie de la suite de Fibonacci, n’étant l'entier passé à la fonction.
# Les deux premiers termes de la suite sont toujours donnés. Il s'agit de 0 et 1.

nombre = int(input("Entrer un nombre : "))

condition = 0

nb1 = 0
nb2= 1

while condition < nombre :
    
    new_nbr = nb1 + nb2

    nb2 = nb1
    nb1 = new_nbr

    condition += 1
    print(new_nbr, end=" ")