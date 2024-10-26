

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
    all_contacts.append([nom, numero, email])



ajouter_contact()

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
    nom = input("Entrez le nom du contact à rechercher : ")
    for  contact in all_contacts:
        if contact[0] == nom:
            print("Nom:", contact[0])
            print("Numéro de téléphone:", contact[1])
            print("Email:", contact[2])
            print("-----")
        else :  print("Contact non trouvé, reesayer")

