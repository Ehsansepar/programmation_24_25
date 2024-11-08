# fichier = open('./txt_files/test.txt', 'w')  # ouvre le fichier en mode écriture
# for marque in range(4):
#     marque = input('Introduisez une marque: ')
#     fichier.write(marque + "\n")  # ajoute la marque et un saut de ligne
    
#     if marque == "quitte" :
#         break
# fichier.close()  # ferme le fichier


fichier = open('./txt_files/test.txt', 'r')
for marque in range(4):  # on suppose qu'on connaît le nombre de lignes
    marque = fichier.readline()
    print(marque.strip())  # affiche la ligne sans le caractère de saut de ligne
fichier.close()
