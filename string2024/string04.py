#  Réalise un programme qui compte les voyelles dans une phrase
# voy="aeiouy"
# et on regarde si une lettre de la phrase est dans (instruction in) voy .

mot =  input("Entrez une phrase : ")
voy="aeiouy"
compteur = 0

for i in mot:
    if i in voy :
        compteur += 1
print(f"Nombre voyelle : {compteur}")
