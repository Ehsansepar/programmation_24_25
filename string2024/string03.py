# 2) Réalise un programme python qui épelle ton nom
# Exemple 
# Quel est ton nom? : PAUL
# Ton nom s'écrit donc:
# P
# A
# U
# L
# 3) Idem mais ton nom s'affiche en commençant par la fin
# L U A P (sans passer à la ligne)

nom = str(input("Quel est ton nom : "))

for i in nom :
    print(i, end=" ")