facturegsm = [25, 55, 20, 63, 120, 45, 67, 81, 96, 26, 56, 36]
mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

nombre_mois_sup_50 = 0
for depense in facturegsm:
    if depense > 50:
        nombre_mois_sup_50 += 1

print(f"Nombre de mois avec des dépenses supérieures à 50 : {nombre_mois_sup_50}")

print("Mois avec des dépenses supérieures à 50 :")
for i in range(len(facturegsm)):  
    if facturegsm[i] > 50:  
        print(mois[i]) 

moyenne_depenses = sum(facturegsm) / len(facturegsm)
print(f"Moyenne mensuelle des dépenses : {(round(moyenne_depenses), 2)} €")
