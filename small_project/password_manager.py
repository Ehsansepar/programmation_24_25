def add() : 
    name = input("Account name : ")
    password = input("Password : ")
    website = input("Website : ")

    with open('password.txt', 'a') as fichier :
        fichier.write(name + "|" + password + "|" + website + "\n")
    
    print("Votre mot de passe a bien été enregistrer \n")