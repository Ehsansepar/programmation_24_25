# Etablir un programme qui permet d'introduire un numéro de compte bancaire européen et qui en
# extrait le n° banque, le digit
# ex : BE68001156575971
# n° banque : 68
# digit 71

nombre = input("Enter voter numéro  de compte bancaire européen : ")

print("N° banque :",nombre[-2:])
print("Pays :" ,nombre[:2])
print("Digit :",nombre[2:4])
