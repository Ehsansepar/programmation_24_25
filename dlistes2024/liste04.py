# 4) Soit 1 liste de nombres
# nb=[25,89,65,99,13,78,12,33,68,17]
#  0 1 2 3 4 5 6 7 8 9
# Affichez la position !!! des nombres pairs. Ici ce sera 5 6 8
# Sauvez sous liste4.py

nb=[25,89,65,99,13,78,12,33,68,17]



for i in range(len(nb)) :
    if nb[i] % 2 == 0 :
        print(i, nb[i])