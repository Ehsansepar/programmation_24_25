# Soit 1 liste de nombres
# nb=[25,89,65,99,13,78,12,33,68,17]
# Affichez le minimum (cf. Maximum)
# On initialise mini=nb[0] et pas mini=0
# Sauvez sous liste6.py

nb=[25,89,65,99,13,78,12,33,68,17]
mini=nb[0]

for i in range (1,len(nb)) :
    if nb[i]<mini :
        mini=nb[i]
        print(mini)