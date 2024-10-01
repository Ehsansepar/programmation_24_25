# 1°) Ajoute :
#  A : les deux derniers chiffres de ton année de naissance ;
#  B : l'entier juste en-dessous du quart de A ;
#  M : un nombre associé au mois de ta naissance
# (janv.=0, fév.=3 mars=3, avril=6, mai=1, juin=4, juill.=6, août=2, sept=5, oct.=0, nov.=3,
# déc.=5) ; (utilisez une liste)
#  J : le numéro du jour du mois de ta naissance.
# 2°) Divise le résultat par 7;
# 3°) Regarde le reste de la division : si c'est un 0, tu es né un dimanche ; si c'est un 1, tu es né un
# lundi ; si c'est un 2, tu es né un mardi ; ... etc (utilisez une liste)
# Exemple : Si tu es né le 16 mai 1979.
# A = 79 ; B = 19 ; M = 1 ; J = 16 ; A +B + M + J = 115 .
# 115 divisé par 7, il reste 3.
# Tu es né un mercredi !
# Remarque : Cet algorithme ne passe pas l'an 2000 !!!
# Il faut alors retrancher 2 au reste de la division ou ajouter 5 si le reste est plus petit que 2
# (Exemple : Le 1er janvier 2000 était un samedi et donne 1 comme reste au lieu de 6).

annee = 1979
mois = 5
jour = 16

A = annee % 100
B = A // 4

mois_valeurs = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]  
M =  mois_valeurs[mois - 1]

J = jour

somme = A + B + M + J
somme = somme % 7

jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
jour_de_naissance = jours[somme]

print(f"Tu es né(e) un {jour_de_naissance} !")