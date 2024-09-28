#Ecrire un script qui permet à l'utilisateur d'introduire des nombres et qui les additionne au
#fur et à mesure. Le script s'arrête lorsque l'utilisateur introduit un nombre négatif. A ce
#moment l'ordinateur affiche la somme. (1, 6, 2, 8, 4)

somme = 0

while True :
    nombre = int(input("Entrez un nombre : "))
    
    if  nombre < 0 :
        print(f"La somme de vos nombres est  {somme}")

        break
    else : 
        somme +=  nombre
