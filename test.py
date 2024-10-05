# facturegsm =[25,55,20,63,120,45,67,81,96,26,56,36]
# mois=[‘janvier’,’février’,’mars’,....]
# établir un programme qui permet
# ● de compter le nombre de mois où les dépenses sont supérieures à 50 (ici 7)
# ● d’afficher les mois ou les dépenses sont supérieures à 50
# ● moyenne mensuelle des dépenses de communication

facturegsm = [25, 55, 20, 63, 120, 45, 67, 81, 96, 26, 56, 36]
mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
mois_superieurs_50 = []

compteur_superieur_50 = 0
for superieur in range(len(facturegsm)) :
    if facturegsm[superieur] > 50:
        mois_superieurs_50.append(mois[superieur])

        compteur_superieur_50 += 1


print(f"les dépenses sont supérieures à 50 en {mois_superieurs_50}", end=" ")
print(compteur_superieur_50)
