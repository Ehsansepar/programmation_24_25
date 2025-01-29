# 1) Soit 1 liste de nombres
# Afficher les cotes supérieures à 30 et comptabiliser les (Sauvez sous liste1.py)

# nb=[15,89,5,99,23,78,12,33,68,16]

# nouvelle_liste = []
# compteur = 0

# for i in nb :
#     if i > 30 :
#         nouvelle_liste.append(i)
#         compteur += 1

# print(nouvelle_liste)
# print(compteur)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 3) Soit 1 liste de nombres
# nb=[25,89,65,99,13,78,12,33,68,17]
# # Trouver et afficher le maximum de la liste

# maximum = 0

# for i in range(len(nb)) :
#     if nb[i] > maximum :
#         maximum = nb[i]
# print(maximum)

# ************************************************************************************************************************

# 4) Soit 1 liste de nombres
# Trouver la moyenne
# Indiquer combien il y a de cotes supérieures à 30. (Sauvez sous liste1.py)
# nb=[15,89,5,99,23,78,12,33,68,16]
# somme = 0
# compteur = 0

# for i in range(len(nb)) :
#     somme += nb[i]
#     if nb[i] > 30 : 
#         compteur += 1

# moyenne = (somme / len(nb)) 

# print(somme)
# print(moyenne)

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

# 5) Soit 1 liste
# Faites la moyenne des ventes. Partez absolument de cette liste. Votre programme doit fonctionner
# si l'on ajoute une ville et un montant.

# ventes = ["Bruxelles", 12897, "Charleroi", 11782, "Namur", 17651, "Liège", 17670]

# # Calcul de la somme des ventes
# somme = 0
# for i in range(1, len(ventes), 2):  # On prend les indices impairs (ventes)
#     somme += ventes[i]  # On additionne les ventes à la somme

# # Calcul de la moyenne
# moyenne = somme / (len(ventes) // 2)  # On divise par le nombre d'éléments numériques (ventes)

# # Affichage des résultats
# print("Somme des ventes:", somme)
# print("Moyenne des ventes:", moyenne)


# -------------------------------------------------------------------------------------------------------------------------------
# 6) Soit 1 liste
# Afficher les mots et leur longueur (il faut utiliser 2 len un pour la liste et un pour le mot)
# Ex Bruxelles 9
# Paris 5

# capitales=['Bruxelles','Paris','Londres','Berlin','Luxembourg','Madrid','Rome']

# for i in range(len(capitales)) : 
#     print(capitales[i], len(capitales[i]))

# ------------------------------------------------------------------------------------------------------------------------------

# 7) Soit 1 liste de nombres
# afficher l'indice du plus grand nombre, la réponse ici est 3

# nb=[25,89,65,99,13,78,12,33,68,17]

# maximum = 0

# for i in range(len(nb)) : 
#     if nb[i] > maximum : 
#         maximum = nb[i]

# print(nb.index(maximum))

# -------------------------------------------------------------------------------------------------------------------------------------

# 8) Soit une liste
# Echangez les valeurs au sein de la liste. => vecteur devient [62,27]
# vecteur=[27,62]

# vecteur[0], vecteur[1] = vecteur[1], vecteur[0]

# print(vecteur)

# -------------------------------------------------------------------------------------------------------------------------------------
# facturegsm = [25, 55, 20, 63, 120, 45, 67, 81, 96, 26, 56, 36]
# mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

# mois_sup_50 = 0

# for i in range(len(facturegsm)) : 
#     if facturegsm[i] > 50 :
#         mois_sup_50 += 1

# for i in range(len(facturegsm)) :
#     if facturegsm[i] > 50 :
#         print(mois[i])

# moyenne = sum(facturegsm) / len(facturegsm)

# print(moyenne)

# -------------------------------------------------------------------------------------------------------------------------------------------

# 2) Tirez 200 nombres au hasard compris entre 1 et 100, et ajoutez les dans la liste lst50 s'ils sont
# supérieurs à 50. Partez d'une liste vide et affichez à la fin la liste complète.

# from random import randrange

# lst50 = []

# for i in range(200) : 
#     hasard = randrange(1, 101)
#     if hasard > 50 :
#         lst50.append(hasard)
# print(lst50)


# -------------------------------------------------------------------------------------------------------------------------------------------
# 3) Soit 1 liste
# affichez les mots inférieurs ou égal à 5 lettres, combien y en a t-il ?
# fruits=['pomme','poire','ananas','kiwi','banane','mangue','peche','prune']

# for i in range(len(fruits)) : 
#     if len(fruits[i]) <= 5 :
#         print(fruits[i])

# -------------------------------------------------------------------------------------------------------------------------------------------

# # 4) Soit 1 liste de nombres
# nb=[25,89,65,99,13,78,12,33,68,17]
# #     0  1  2  3  4  5  6  7  8  9
# # Affichez la position !!! des nombres pairs. Ici ce sera 5 6 8
# # Sauvez sous liste4.py

# for i in range(len(nb)) : 
#     if nb[i] % 2 == 0 : 
#         print(i, nb[i])

# 5) Soit 1 liste de nombres
# Affichez le minimum (cf. Maximum)
# On initialise mini=nb[0] et pas mini=0
# Sauvez sous liste6.py
# nb=[25,89,65,99,13,78,12,33,68,17]
# mini = nb[0]

# for i in range(1, len(nb)) : 
#     if nb[i] < mini : 
#         mni = nb[i]
# print(mini)


# ----------------------------------------------------------------------------------
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

    ...