import random
import string

def motPasse(n):

    if n < 1:
        return "Erreur : n doit être au moins 1."
    
    # n lettres aléatoires
    lettres = ''.join(random.choices(string.ascii_lowercase, k=n))
    
    # 2chiffres aléatoires
    chiffres = ''.join(random.choices(string.digits, k=2))
    
    mot_de_passe = lettres + chiffres
    
    # mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))
    
    return mot_de_passe

if __name__ == "__main__":
    passwd = motPasse(5)
    print(passwd)
