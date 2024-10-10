nb_ordi = int(input("Entrez le nombre de l'ordinateur que vous voulez dans le réseau : "))
premiere_nbr = int(input("Entrez le numéro dans ordre du premier ordinateur : "))

list_ordi = []
list_ip = []

for i in range(premiere_nbr, nb_ordi + premiere_nbr) : # Si numero_debut = 14 et nombre_ordinateurs = 5, alors range(14, 14 + 5) donnera les nombres suivants : 14, 15, 16, 17, 18.
    if i == 0 or i == 255:
        print(f"L'adresse IP '192.168.0.{i}' ne peut pas être utilisée. Ajustez le numéro de départ.")
        break
    list_ordi.append(f"ordi{i}")
    list_ip.append(f"192.168.0.{i}")

print("Listes des noms des ordinatuer : ",list_ordi)
print("Liste des adresse IP correspondantes : ", list_ip)
