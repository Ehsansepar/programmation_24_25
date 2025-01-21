def somme(liste) : 
    total = 0
    for nbr in range(len(liste)) :
        total += liste[nbr]
    return total


l = [5, 8, 9, 47, 36, 123, 5, 3, 1]

print(somme(l))