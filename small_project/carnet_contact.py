

all_contacts = []

# all_contacts.append(["Nom du contact", "Numéro de téléphone", "Email"])
# all_contacts.append(["John Doe", "1234567890", "johndoe@example.com"])

# for contact in all_contacts:
#     print("Nom :", contact[0])
#     print("Numéro de téléphone :", contact[1])
#     print("Email :", contact[2])
#     print("-----")


def ajouter_contact() :
    nom = input("Entrez le nom du contact : ")
    numero = input("Entrez le numéro de téléphone du contact : ")
    email = input("Entrez l'email du contact : ")
    print("C'est bon  ! Le contact a été ajouté avec succès !")
    print("-----\n\n")

    all_contacts.append([nom, numero, email])

def afficher_contacts():
    if not all_contacts:
        print("Aucun contact trouvé.")
    else:
        for contact in all_contacts:
            print("Nom:", contact[0])
            print("Numéro de téléphone:", contact[1])
            print("Email:", contact[2])
            print("-----")

def  rechercher_contact():
    i = 1
    nom = input("Entrez le nom du contact à rechercher : ")
    trouve = False
    for  contact in all_contacts:
        if contact[0].lower() == nom.lower() :
            print("Id",  i)
            print("Nom:", contact[0])
            print("Numéro de téléphone:", contact[1])
            print("Email:", contact[2])
            print("-----")
            trouve = True
            i += 1
            break
        if not trouve :
            print("Aucun contact trouvé avec ce nom.")

def supprimer_contact():
    i = 1
    nom = input("Entrez le nom du contact à supprimer : ")
    trouve = False
    for contact in all_contacts:
        if contact[0].lower() == nom.lower():
            del all_contacts[i-1]
            print("Le contact a été supprimé avec succès !")
            trouve = True
            break
        i += 1


while True : 
    choisir  = input("Voulez-vous ajouter un contact (A), afficher tous les contacts (B), rechercher un contact (C) ou supprimer un contact (D) ? ")

    if choisir.upper() == "A" :
        ajouter_contact()
    elif choisir.upper() == "B" :
        afficher_contacts()
    elif choisir.upper() == "C" :
        rechercher_contact()
    elif  choisir.upper() == "D" :
        supprimer_contact()
    else :
        print("Option non valide.")
