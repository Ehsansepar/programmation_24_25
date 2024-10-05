# 3) Soit 1 liste
# fruits=['pomme','poire','ananas','kiwi','banane','mangue','peche','prune']
# affichez les mots inférieurs ou égal à 5 lettres, combien y en a t-il ?
# Sauvez sous liste3.py

fruits=['pomme','poire','ananas','kiwi','banane','mangue','peche','prune']
compteur = 0

for i in range(len(fruits)) :
    if  len(fruits[i]) <= 5 :
        compteur += 1
        print(f"{fruits[i]}  ---> {len(fruits[i])} lettre")
print("Il y a ", compteur, "est égale ou plus petite que  5 lettres")
