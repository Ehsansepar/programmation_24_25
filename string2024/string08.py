# 8) Etablir un programme qui permet d'introduire un mot et qui teste s'il s'agit d'un palindrome.
# Ex RADAR

mot = input("Enterz un mot : ")
mot = mot.lower()
mot = mot.replace(" ", "")
if mot == mot[::-1] : # mot[::-1] pour l'inverser les mots
    print("C'est un palindrome")
else :
    print("C'est pas un palindrome")