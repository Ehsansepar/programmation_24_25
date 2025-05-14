# dictionnaire : représente les réponse d une personn e
# fontionj poser des questions et mémoriser les r eponses dans le dictionnaire
# fontion corriger (attribuer des points sur bases des reponses)


# key = pseudo
# reponses = {pseudo : "charles",
#           questionnaire : {Q1 : 1,
#                            Q2 : 2,
#                            Q3 : 3,
#                            Q4 : 4,
#                            Q5 : 5},
#           resultat : 23
#           }
#
#
#
#

def poserQuestions(pseudo):
    return reponses  # dictionaire

def correction(pseudo):
    return resultat


def afficherResultat(pseudo):
    return

continuer = True
while continuer:
    print("-" * 150)

    print("1. Repondsre aux questions")
    print("2. calculer le resultat")
    print("3. statistique d'une question")
    print("4. quitter")
    print("-" * 150)

    choix = int(input("choisissez une option : "))
    if choix == 1:
        poserQuestions(pseudo)
    elif choix == 2:
        correction(pseudo)
    elif choix == 3:
        afficherResultat(pseudo)
    elif choix == 4:
        continuer = False


    # pseudo = input("Entrez votre pseudo : ")
    # repnses = poserQuestions(pseudo)
    # resultat = correction(pseudo)
    # continuer = False


    