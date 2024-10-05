# 1) Réalise un programme qui compte le nombre de "e" dans une phrase

phrase = str(input("Entrer une phrase  : "))

compteur = 0 

for i in phrase : 
    if  i == "e" :
        compteur += 1
print("Le nombre de 'e' dans la phrase est de : ", compteur)

