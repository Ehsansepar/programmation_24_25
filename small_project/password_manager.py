def add() : 
    name = input("Account name : ")
    password = input("Password : ")
    website = input("Website : ")

    with open('password.txt', 'a') as fichier :
        fichier.write(name + "|" + password + "|" + website + "\n")
    
    print("Votre mot de passe a bien été enregistrer \n")

def view() : 
    print(" ----- Vos Comptes et mots de passe  -----")
    
    with open('password.txt', 'r') as fichier :
        lignes = fichier.readlines()
        for i, ligne in lignes :
            data = ligne.rstrip()
            name, password, website = data.split("|")
            print(f"ID : {i}\nName Account : {name}\nPassword : {password}\nWebsite : {website}\n\n")

while True :
    try : 
        choix = int(input(
            """ ----- Chose Option below -----
       1 - Add 
       2 - View
       3 - Quitter
       
       -> """))
        
        if choix == 1 :
            add()
        elif choix == 2 : 
            view()
        elif choix == 3 :
            break
    except ValueError :
        print("Essaye de choisir avec des nombre svp! \n\n")