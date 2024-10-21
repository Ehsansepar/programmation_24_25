# 5. Soit cette liste ventes=[['Marc',2600],['Julie',7800],['Paul',3600],['Luc',9500],['Lola',1100]] . 
# Ecrire un script qui permet d'afficher les pourcentages des ventes de chaque collaborateur.
# Marc 10,569 %
# ......................


ventes=[
    ['Marc',2600],
    ['Julie',7800],
    ['Paul',3600],
    ['Luc',9500],
    ['Lola',1100]
        ]
somme = 0
# pourcentage = 0
for vente in range (len(ventes)):
    somme += ventes[vente][1]
    pourcentage = round((ventes[vente][1] / somme ) * 100, 2)
    # round(pourcentage, 2)
    print(f"{ventes[vente][0]} =  {pourcentage} %")

# print(somme)